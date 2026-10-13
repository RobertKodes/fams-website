// F.A.M.s — tot JavaScript-ul site-ului.
//
// Deliberat putin: meniul de telefon, trimiterea formularului pe WhatsApp si
// linia de sub antet. Restul (acordeonul de la intrebari, starea paginii
// curente) e facut in HTML si CSS, ca sa mearga si daca fisierul asta nu se
// incarca.

(function () {
  "use strict";

  // meniul de pe telefon
  var buton = document.querySelector("[data-meniu]");
  var meniu = document.getElementById("meniu");

  if (buton && meniu) {
    buton.addEventListener("click", function () {
      var deschis = buton.getAttribute("aria-expanded") === "true";
      buton.setAttribute("aria-expanded", String(!deschis));
      meniu.hidden = deschis;
    });

    // Escape inchide meniul si muta focusul inapoi pe buton
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && buton.getAttribute("aria-expanded") === "true") {
        buton.setAttribute("aria-expanded", "false");
        meniu.hidden = true;
        buton.focus();
      }
    });

    // daca ecranul se lateste peste pragul din CSS, meniul trebuie inchis:
    // altfel ramane deschis sub antetul de desktop
    var prag = window.matchMedia("(min-width: 881px)");
    var laPrag = function (e) {
      if (e.matches) {
        buton.setAttribute("aria-expanded", "false");
        meniu.hidden = true;
      }
    };
    if (prag.addEventListener) prag.addEventListener("change", laPrag);
    else prag.addListener(laPrag);
  }

  // Formularul de oferta: la trimitere se deschide WhatsApp cu toata cererea
  // scrisa frumos, si in paralel cererea pleaca si la Netlify (e-mail).
  // Fara JavaScript, formularul se trimite normal la Netlify si duce la thank-you/.
  var formular = document.querySelector("form[data-whatsapp]");
  var trimis = document.querySelector("[data-trimis]");

  if (formular && trimis) {
    var eticheta = function (camp) {
      var label = camp.querySelector("label");
      if (!label) return "";
      // la bife textul e dupa input, la restul e primul nod din eticheta
      return camp.classList.contains("camp--bifa")
        ? label.textContent.trim()
        : label.firstChild.textContent.trim();
    };

    var valoare = function (control) {
      if (control.type === "checkbox") return control.checked ? "Yes" : "";
      var v = control.value.trim();
      if (!v) return "";
      if (control.type === "date") {
        var d = new Date(v + "T12:00:00");
        return d.toLocaleDateString("en-GB", {
          weekday: "long", day: "numeric", month: "long", year: "numeric"
        });
      }
      return v;
    };

    var mesaj = function () {
      var randuri = ["*New enquiry from the F.A.M.s website*"];
      formular.querySelectorAll("fieldset").forEach(function (grup) {
        var bucati = [];
        grup.querySelectorAll(".camp").forEach(function (camp) {
          var control = camp.querySelector("input, select, textarea");
          var v = control && valoare(control);
          if (!v) return;
          // textele lungi pe rand nou, ca sa nu se lipeasca de eticheta
          bucati.push(control.tagName === "TEXTAREA"
            ? eticheta(camp) + ":\n" + v
            : eticheta(camp) + ": " + v);
        });
        if (bucati.length) {
          randuri.push("", "*" + grup.querySelector("legend").textContent.trim() + "*");
          randuri = randuri.concat(bucati);
        }
      });
      return randuri.join("\n");
    };

    formular.addEventListener("submit", function (e) {
      e.preventDefault();
      var legatura = "https://wa.me/" + formular.getAttribute("data-whatsapp") +
                     "?text=" + encodeURIComponent(mesaj());

      // deschis direct din click, altfel browserul il blocheaza ca popup
      window.open(legatura, "_blank", "noopener");

      fetch(formular.action, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams(new FormData(formular)).toString()
      }).catch(function () { /* WhatsApp ramane calea principala */ });

      trimis.querySelector("[data-trimis-wa]").href = legatura;
      formular.hidden = true;
      trimis.hidden = false;
      trimis.focus();
      trimis.scrollIntoView({ block: "start" });
    });
  }

  // linia de sub antet apare doar cand pagina e derulata
  var antet = document.querySelector(".antet");
  if (antet) {
    var santinela = document.createElement("div");
    santinela.setAttribute("aria-hidden", "true");
    santinela.style.cssText = "position:absolute;top:0;height:1px;width:1px";
    document.body.prepend(santinela);

    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (intrari) {
        if (intrari[0].isIntersecting) antet.removeAttribute("data-lipit");
        else antet.setAttribute("data-lipit", "");
      }).observe(santinela);
    }
  }
})();
