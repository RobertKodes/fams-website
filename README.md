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

E pregatit pentru **Netlify Forms** (`data-netlify="true"` plus campul ascuns
`form-name`). Pe Netlify, cererile apar in tabul *Forms* al site-ului.
**Pe GitHub Pages formularul nu are unde sa trimita** — acolo trebuie legat la
un serviciu extern (Formspree, Basin) sau la un backend propriu.

## Ce nu e inventat

Nu exista pe site telefon, e-mail, adresa, recenzii, numar de evenimente sau ani
de experienta, pentru ca nu ne-au fost date. Unde lipseste ceva, pagina spune
sincer ca lipseste — vezi galeria. Cand apar datele reale de contact, se adauga
in `continut.py` (`SITE`) si in subsol, si se completeaza pagina de
confidentialitate cu furnizorul formularului si cu o adresa pentru cereri GDPR.

## Capturi de ecran

Nu e Chrome pe masina de dezvoltare, deci nu merge `--headless --screenshot`.
`unelte/captura.swift` randeaza o pagina intr-un WKWebView si salveaza PNG:

```sh
swift unelte/captura.swift http://localhost:8080/ /tmp/acasa.png 1440 0
#                                                              lat  inalt (0 = toata pagina)
```
