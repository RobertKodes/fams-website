# F.A.M.s Mobile Catering — site

Site static, fara framework si fara pas de build pe server: HTML-ul generat e
comis in depozit, iar Netlify si GitHub Pages il servesc ca atare.

## Ce se editeaza

| vrei sa schimbi | fisierul |
|---|---|
| orice text de pe site | `continut.py` |
| structura unei sectiuni | `construieste.py` |
| culori, tipografie, spatii | `assets/styles.css` |
| fotografiile | `surse/` + `unelte/pregateste_imagini.py` |

**Paginile `.html` nu se editeaza de mana** — sunt generate si se suprascriu.
Dupa orice modificare in `continut.py`, `construieste.py` sau in imagini:

```sh
python3 construieste.py
```

## Imaginile

Sursele reale stau in `surse/`. Sunt patru cadre cu duba, taiate dintr-un colaj
de 1152x1536 — adica ~560x750 px fiecare. Atat exista; nu se pot inventa pixeli.

Consecinta, respectata peste tot in CSS: **nicio fotografie nu se afiseaza mai
lata de ~320px logici** (`--foto-max`). Asa fiecare imagine ajunge pe ecran la
1.8x–2.3x densitate, adica se vede clara. Daca maresti o placa peste valoarea
asta, imaginea redevine moale — nu e o preferinta de design, e aritmetica.

```sh
python3 unelte/pregateste_imagini.py      # retaie, corecteaza tonul, scrie assets/foto/
```

Scriptul scoate fiecare fotografie in 280 / 420 / 560 px (`srcset`), rozeta
rotunda a logo-ului si cartela de partajare de 1200x630.

**Cand apar fotografii noi** (mancare, evenimente, familia) — si sunt lucrul de
care site-ul are cea mai mare nevoie — pune-le in `surse/`, adauga-le in
`CADRANE`/`DECUPAJE` sau trateaza-le ca fisiere separate, si ridica `--foto-max`
daca rezolutia noua permite.

## Domeniul

Fara domeniu declarat, paginile nu au `canonical` si nu exista `sitemap.xml`.
Site-ul merge, dar partea de SEO e incompleta:

```sh
python3 unelte/configureaza.py --domeniu https://adresa-reala
```

## Preview local

```sh
python3 -m http.server 8080        # din acest director
```

Caile sunt relative, deci site-ul merge si in radacina unui domeniu (Netlify),
si sub o subcale (`.../fams-website/` pe GitHub Pages), si local. Singura
exceptie e `404.html`, care foloseste cai absolute: e servit pentru orice
adresa, la orice adancime, iar o cale relativa s-ar rezolva fata de adresa
ceruta, nu fata de radacina.

## Formularul de cerere de oferta

Cand clientul apasa *Send enquiry*:

1. **se deschide WhatsApp** cu toata cererea scrisa frumos (titluri pe grupe,
   data in clar, doar campurile completate), catre numarul din
   `continut.py` → `SITE["whatsapp"]`. Clientul doar apasa *send*. Numarul nu
   apare nicaieri in pagina — F.A.M.s nu vrea apeluri.
2. **in paralel** cererea pleaca la **Netlify Forms** (`data-netlify="true"`).
   In Netlify: *Forms → Form notifications → Email* catre
   `fams.company2021@gmail.com`, ca sa ajunga si pe e-mail.
3. formularul e inlocuit de un panou cu buton *Send on WhatsApp* (daca
   telefonul a blocat deschiderea) si adresa de e-mail.

Fara JavaScript, formularul se trimite clasic la Netlify si duce la `thank-you/`.
Pe GitHub Pages pasul 2 nu are unde sa trimita, dar WhatsApp merge oricum.

Campurile (si deci si randurile din mesaj) se editeaza in `continut.py` → `FORMULAR`.

## Jurnalul (blog)

Articolele sunt fisiere Markdown in `jurnal/`, cu antet `title` / `description`
/ `date` / `keywords` — vezi `jurnal/_exemplu.md`. `python3 construieste.py` le
transforma in `journal/<nume-fisier>/`, cu date structurate `BlogPosting`, le
pune in sitemap si in `llms.txt`. Pagina *Journal* si linkul din meniu apar
abia cand exista primul articol. Legaturile interne se scriu de la radacina
(`/contact/`); generatorul le face relative.

## llms.txt

Generat la fiecare constructie: rezumatul firmei (cine e, unde lucreaza, motto,
e-mail, retele) si lista paginilor, pentru asistentii AI care recomanda
furnizori. Cu domeniu configurat, linkurile devin absolute.

## Date de contact

Pe site apar: e-mailul, Instagram, Facebook, TikTok (`SITE` in `continut.py`).
Nu apar: telefon, adresa, recenzii, preturi — nu ne-au fost date sau nu se
vor publice. Galeria spune sincer ca are doar duba, pana apar poze cu mancare.

## Capturi de ecran

Nu e Chrome pe masina de dezvoltare, deci nu merge `--headless --screenshot`.
`unelte/captura.swift` randeaza o pagina intr-un WKWebView si salveaza PNG:

```sh
swift unelte/captura.swift http://localhost:8080/ /tmp/acasa.png 1440 0
#                                                              lat  inalt (0 = toata pagina)
```
