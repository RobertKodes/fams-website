// F.A.M.s — tot JavaScript-ul site-ului.
//
// Deliberat putin: meniul de telefon si linia de sub antet. Restul (acordeonul
// de la intrebari, starea paginii curente) e facut in HTML si CSS, ca sa mearga
// si daca fisierul asta nu se incarca.

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
