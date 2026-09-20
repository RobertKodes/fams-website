#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genereaza paginile HTML din `continut.py`.

Site-ul are 12 pagini care impart acelasi antet, subsol si aceleasi tipare de
sectiune. Scrise de mana, orice schimbare in meniu ar insemna 12 editari si,
inevitabil, o pagina uitata. Aici se scrie o singura data.

Iesirea este HTML static obisnuit, comis in depozit - Netlify si GitHub Pages
il servesc ca atare, fara pas de build.

Caile sunt relative la adancimea fiecarei pagini ("assets/..." in radacina,
"../assets/..." in subdirectoare), ca site-ul sa mearga si in radacina unui
domeniu, si sub o subcale (GitHub Pages), si local. Exceptie: 404.html, care e
servit pentru orice adresa, la orice adancime, deci pastreaza cai absolute.

Rulare:  python3 construieste.py
"""

import hashlib
import json
from datetime import date
from pathlib import Path

import continut as C

RADACINA = Path(__file__).resolve().parent
MANIFEST = RADACINA / "assets" / "foto" / "dimensiuni.json"

with open(MANIFEST, encoding="utf-8") as f:
    DIMENSIUNI = json.load(f)

def amprenta(cale_relativa):
    """Primele 8 caractere din md5-ul fisierului, pentru ?v= in URL.

    Numele fisierului ramane acelasi (nu vrem gunoi vechi in assets/), dar
    URL-ul se schimba cand se schimba continutul, si cache-ul se rupe singur.
    """
    date_ = (RADACINA / cale_relativa).read_bytes()
    return hashlib.md5(date_).hexdigest()[:8]


V_CSS = amprenta("assets/styles.css")
V_JS = amprenta("assets/site.js")

DOMENIU = ""
_d = RADACINA / "domeniu.txt"
if _d.exists():
    DOMENIU = _d.read_text(encoding="utf-8").strip().rstrip("/")


# --------------------------------------------------------------- ajutoare --

def prefix_pentru(cale):
    """"" pentru paginile din radacina, "../" pentru cele dintr-un subdirector."""
    if cale in ("", "404.html"):
        return ""
    return "../" * cale.strip("/").count("/") if "/" in cale.strip("/") else "../"


def absolut(cale):
    """URL complet, cand stim domeniul (vezi unelte/configureaza.py)."""
    if not DOMENIU:
        return None
    if cale == "404.html":
        return f"{DOMENIU}/404.html"
    return f"{DOMENIU}/{cale}"


def poza(cheie, p, sizes, clasa="", lazy=True, legenda=None):
    """<img> cu srcset.

    Sursele reale au ~560px latime. `sizes` trebuie sa declare latimea reala de
    afisare, ca browserul sa aleaga fisierul potrivit si sa nu intinda imaginea.
    """
    nume, alt = C.FOTO[cheie]
    dim = DIMENSIUNI[nume]
    latimi = dim["latimi"]
    srcset = ", ".join(f"{p}assets/foto/{nume}-{w}.webp {w}w" for w in latimi)
    incarcare = ' loading="lazy"' if lazy else ""
    img = (f'<img src="{p}assets/foto/{nume}-{latimi[-1]}.webp" srcset="{srcset}" '
           f'sizes="{sizes}" width="{dim["w"]}" height="{dim["h"]}" alt="{alt}"'
           f'{incarcare} decoding="async">')
    cls = f"placa {clasa}".strip()
    if legenda:
        return (f'<figure class="{cls}">{img}'
                f'<figcaption>{legenda}</figcaption></figure>')
    return f'<figure class="{cls}">{img}</figure>'


def buton(p, tinta, text, stil="plin"):
    href = tinta if tinta.startswith("#") else p + tinta
    if stil == "plin":
        return f'<a class="buton" href="{href}">{text}</a>'
    return f'<a class="legatura" href="{href}">{text}</a>'


# ---------------------------------------------------------------- blocuri --

def bloc_deschidere(b, p):
    actiuni = " ".join(buton(p, *a) for a in b["actiuni"])
    foto = poza(b["foto"], p, "(max-width: 860px) 62vw, 320px",
                clasa="placa--ridicata", lazy=False, legenda=b.get("legenda"))
    return f"""<section class="deschidere">
  <div class="container deschidere__grid">
    <div class="deschidere__text">
      <p class="eticheta">{b["eticheta"]}</p>
      <h1>{b["titlu"]}</h1>
      <p class="lede">{b["lede"]}</p>
      <div class="actiuni">{actiuni}</div>
    </div>
    <div class="deschidere__foto">{foto}</div>
  </div>
</section>"""


def bloc_titlu_pagina(b, p):
    return f"""<section class="titlu-pagina">
  <div class="container">
    <p class="eticheta">{b["eticheta"]}</p>
    <h1>{b["titlu"]}</h1>
    <p class="lede">{b["lede"]}</p>
  </div>
</section>"""


def bloc_banda(b, p):
    itemi = "".join(f"<li>{t}</li>" for t in b["text"])
    return f'<section class="banda"><div class="container"><ul>{itemi}</ul></div></section>'


def bloc_servicii(b, p):
    randuri = []
    for cale, nume, desc in b["randuri"]:
        randuri.append(f"""    <a class="serviciu" href="{p}{cale}">
      <h3>{nume}</h3>
      <p>{desc}</p>
      <span class="serviciu__sageata" aria-hidden="true">&#8594;</span>
    </a>""")
    ident = f' id="{b["id"]}"' if b.get("id") else ""
    return f"""<section class="sectiune"{ident}>
  <div class="container">
    <header class="cap">
      <p class="eticheta">{b["eticheta"]}</p>
      <h2>{b["titlu"]}</h2>
    </header>
    <div class="servicii">
{chr(10).join(randuri)}
    </div>
  </div>
</section>"""


def bloc_cerneala(b, p):
    return f"""<section class="cerneala">
  <div class="container">
    <img class="pecete" src="{p}assets/foto/fams-mark-192.webp"
         srcset="{p}assets/foto/fams-mark-96.webp 96w, {p}assets/foto/fams-mark-192.webp 192w, {p}assets/foto/fams-mark-288.webp 288w"
         sizes="96px" width="96" height="96" alt="" loading="lazy" decoding="async">
    <p class="cerneala__titlu">{b["titlu"]}</p>
    <p class="eticheta eticheta--clara">{b["subsol"]}</p>
  </div>
</section>"""


def bloc_trio(b, p):
    poze = "".join(poza(k, p, "(max-width: 760px) 44vw, 260px", legenda=leg)
                   for k, leg in b["foto"])
    leg = b.get("legatura")
    link = buton(p, leg[0], leg[1], "text") if leg else ""
    return f"""<section class="sectiune sectiune--alt">
  <div class="container">
    <header class="cap cap--doua">
      <div>
        <p class="eticheta">{b["eticheta"]}</p>
        <h2>{b["titlu"]}</h2>
      </div>
      <div class="cap__aparte">
        <p>{b["text"]}</p>
        {link}
      </div>
    </header>
    <div class="trio">{poze}</div>
  </div>
</section>"""


def bloc_pasi(b, p):
    itemi = []
    for i, (titlu, text) in enumerate(b["pasi"], 1):
        itemi.append(f'      <li><span class="pas__nr">{i:02d}</span>'
                     f'<h3>{titlu}</h3><p>{text}</p></li>')
    return f"""<section class="sectiune">
  <div class="container">
    <header class="cap">
      <p class="eticheta">{b["eticheta"]}</p>
      <h2>{b["titlu"]}</h2>
    </header>
    <ol class="pasi">
{chr(10).join(itemi)}
    </ol>
  </div>
</section>"""


def bloc_puncte(b, p):
    itemi = "".join(f'<div class="punct"><h3>{t}</h3><p>{d}</p></div>'
                    for t, d in b["puncte"])
    return f"""<section class="sectiune sectiune--alt">
  <div class="container">
    <header class="cap">
      <p class="eticheta">{b["eticheta"]}</p>
      <h2>{b["titlu"]}</h2>
    </header>
    <div class="puncte">{itemi}</div>
  </div>
</section>"""


def bloc_proza(b, p):
    para = "".join(f"<p>{t}</p>" for t in b["paragrafe"])
    return f"""<section class="sectiune">
  <div class="container proza">
    <div class="proza__cap">
      <p class="eticheta">{b["eticheta"]}</p>
      <h2>{b["titlu"]}</h2>
    </div>
    <div class="proza__text">{para}</div>
  </div>
</section>"""


def bloc_citat(b, p):
    return f"""<section class="citat">
  <div class="container">
    <blockquote>{b["text"]}</blockquote>
    <p class="eticheta">{b["sursa"]}</p>
  </div>
</section>"""


def bloc_galerie(b, p):
    poze = "".join(poza(k, p, "(max-width: 620px) 84vw, (max-width: 980px) 40vw, 300px",
                        legenda=leg) for k, leg in b["foto"])
    return f"""<section class="sectiune">
  <div class="container"><div class="galerie">{poze}</div></div>
</section>"""


def bloc_intrebari(b, p):
    itemi = []
    for q, a in b["intrebari"]:
        itemi.append(f"""      <details>
        <summary><span>{q}</span></summary>
        <div class="raspuns"><p>{a}</p></div>
      </details>""")
    return f"""<section class="sectiune">
  <div class="container">
    <div class="intrebari">
{chr(10).join(itemi)}
    </div>
  </div>
</section>"""


def bloc_text_lung(b, p):
    parti = []
    for titlu, paragrafe in b["sectiuni"]:
        para = "".join(f"<p>{t}</p>" for t in paragrafe)
        parti.append(f"<section><h2>{titlu}</h2>{para}</section>")
    return f"""<div class="sectiune">
  <div class="container"><div class="text-lung">{"".join(parti)}</div></div>
</div>"""


def bloc_final(b, p):
    cale, text = b["actiune"]
    return f"""<section class="final">
  <div class="container">
    <h2>{b["titlu"]}</h2>
    <p>{b["text"]}</p>
    <a class="buton" href="{p}{cale}">{text}</a>
  </div>
</section>"""


def camp(nume, eticheta, tip, oblig, optiuni):
    cerut = ' required aria-required="true"' if oblig else ""
    marca = ' <abbr title="required">*</abbr>' if oblig else ' <span class="optional">optional</span>'
    if tip == "textarea":
        control = f'<textarea id="{nume}" name="{nume}" rows="4"{cerut}></textarea>'
    elif tip == "select":
        opt = "".join(f'<option value="{o}">{o}</option>' for o in optiuni)
        control = (f'<select id="{nume}" name="{nume}"{cerut}>'
                   f'<option value="" disabled selected>Choose one</option>{opt}</select>')
    else:
        extra = ' min="1"' if tip == "number" else ""
        control = f'<input id="{nume}" name="{nume}" type="{tip}"{extra}{cerut}>'
    lat = ' camp--lat' if tip in ("textarea",) else ""
    return (f'<p class="camp{lat}"><label for="{nume}">{eticheta}{marca}</label>'
            f'{control}</p>')


def bloc_formular(b, p):
    grupuri = []
    for titlu, campuri in C.FORMULAR:
        c = "".join(camp(*x) for x in campuri)
        grupuri.append(f'<fieldset><legend>{titlu}</legend><div class="campuri">{c}</div></fieldset>')
    return f"""<section class="sectiune">
  <div class="container formular-grid">
    <form class="formular" name="quote" method="POST" action="{p}thank-you/"
          data-netlify="true" netlify-honeypot="bot-field">
      <input type="hidden" name="form-name" value="quote">
      <p class="ascuns"><label>Leave this empty: <input name="bot-field"></label></p>
{chr(10).join("      " + g for g in grupuri)}
      <p class="camp camp--lat consimtamant">
        <label><input type="checkbox" name="consent" required>
          <span>I’m happy for F.A.M.s to use these details to reply to my enquiry.
          <a href="{p}privacy/">How we handle it</a>.</span></label>
      </p>
      <button class="buton" type="submit">Send enquiry</button>
      <p class="nota">Fields marked <abbr title="required">*</abbr> are required.</p>
    </form>
    <aside class="alaturi">
      <h2>What happens next</h2>
      <ol class="alaturi__pasi">
        <li><strong>We read it.</strong> Every enquiry is read by one of us, not by a system.</li>
        <li><strong>We come back to you.</strong> With questions if we have them, and with options if we don’t.</li>
        <li><strong>You decide.</strong> Nothing you send here commits you to anything.</li>
      </ol>
      <p class="alaturi__zona"><span class="eticheta">Where we work</span>
        Surrey, the surrounding areas, and further afield by arrangement.</p>
    </aside>
  </div>
</section>"""


BLOCURI = {
    "deschidere": bloc_deschidere,
    "titlu_pagina": bloc_titlu_pagina,
    "banda": bloc_banda,
    "servicii": bloc_servicii,
    "cerneala": bloc_cerneala,
    "trio": bloc_trio,
    "pasi": bloc_pasi,
    "puncte": bloc_puncte,
    "proza": bloc_proza,
    "citat": bloc_citat,
    "galerie": bloc_galerie,
    "intrebari": bloc_intrebari,
    "text_lung": bloc_text_lung,
    "final": bloc_final,
    "formular": bloc_formular,
}


# ------------------------------------------------------ antet si subsol ----

def antet(p, cale_curenta):
    legaturi = []
    for cale, eticheta in C.NAV:
        curent = ' aria-current="page"' if cale == cale_curenta else ""
        legaturi.append(f'<a href="{p}{cale}"{curent}>{eticheta}</a>')
    nav = "".join(legaturi)
    acasa = ' aria-current="page"' if cale_curenta == "" else ""
    return f"""<a class="sari" href="#continut">Skip to content</a>
<header class="antet">
  <div class="container antet__interior">
    <a class="marca" href="{p}"{acasa} aria-label="F.A.M.s — home">
      <img src="{p}assets/foto/fams-mark-96.webp"
           srcset="{p}assets/foto/fams-mark-96.webp 96w, {p}assets/foto/fams-mark-192.webp 192w"
           sizes="46px" width="46" height="46" alt="F.A.M.s" decoding="async">
      <span class="marca__text">F.A.M.s</span>
    </a>
    <nav class="nav" aria-label="Primary">{nav}</nav>
    <a class="buton buton--mic" href="{p}contact/">Enquire</a>
    <button class="meniu-buton" type="button" aria-expanded="false"
            aria-controls="meniu" data-meniu>
      <span class="meniu-buton__linii" aria-hidden="true"></span>
      <span class="sr">Menu</span>
    </button>
  </div>
  <nav class="meniu" id="meniu" aria-label="Menu" hidden>
    <div class="container">
      {nav}
      <a class="buton" href="{p}contact/">Enquire</a>
    </div>
  </nav>
</header>"""


def subsol(p):
    legaturi = "".join(f'<a href="{p}{c}">{e}</a>' for c, e in C.NAV)
    an = date.today().year
    return f"""<footer class="subsol">
  <div class="container subsol__grid">
    <div class="subsol__marca">
      <img src="{p}assets/foto/fams-mark-192.webp" width="72" height="72"
           alt="" loading="lazy" decoding="async">
      <p class="subsol__slogan">{C.SITE["slogan"]}</p>
    </div>
    <nav class="subsol__nav" aria-label="Footer">
      <p class="eticheta">Pages</p>
      {legaturi}
      <a href="{p}contact/">Enquire</a>
    </nav>
    <div class="subsol__info">
      <p class="eticheta">Where we work</p>
      <p>Surrey, the surrounding areas,<br>and further afield by arrangement.</p>
      <p class="subsol__nota">Contact details are added as soon as they are confirmed.
      Until then, the enquiry form is the way to reach us.</p>
    </div>
  </div>
  <div class="container subsol__jos">
    <p>&copy; {an} {C.SITE["nume_lung"]}</p>
    <p><a href="{p}privacy/">Privacy</a></p>
  </div>
</footer>"""


# ------------------------------------------------------------ date structurate

def date_structurate(pag, p):
    org = {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "FoodEstablishment"],
        "@id": (absolut("") + "#business") if DOMENIU else "#business",
        "name": C.SITE["nume_lung"],
        "alternateName": "F.A.M.s 2021",
        "description": "Family-run mobile catering for weddings, private parties and "
                       "corporate events across Surrey.",
        "foundingDate": str(C.SITE["an"]),
        "servesCuisine": "Event catering",
        "areaServed": [
            {"@type": "AdministrativeArea", "name": "Surrey"},
            {"@type": "Country", "name": "United Kingdom"},
        ],
    }
    if DOMENIU:
        org["url"] = absolut("")
        org["image"] = f"{DOMENIU}/assets/foto/social-preview.webp"
    bucati = [org]

    if pag["cale"] == "faq/":
        intrebari = next(b for b in pag["blocuri"] if b["tip"] == "intrebari")
        bucati.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in intrebari["intrebari"]
            ],
        })
    return "\n".join(
        '<script type="application/ld+json">' + json.dumps(b, ensure_ascii=False) + "</script>"
        for b in bucati)


# ---------------------------------------------------------------- pagina ---

SABLON = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titlu}</title>
<meta name="description" content="{descriere}">
{robots}{canonic}
<meta property="og:type" content="website">
<meta property="og:site_name" content="F.A.M.s Mobile Catering">
<meta property="og:title" content="{titlu}">
<meta property="og:description" content="{descriere}">
<meta property="og:image" content="{og_imagine}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f6f1e8">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{p}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Jost:wght@300;400;500&display=swap">
<link rel="stylesheet" href="{p}assets/styles.css?v={v_css}">
{structurate}
</head>
<body{clasa_body}>
{antet}
<main id="continut">
{corp}
</main>
{subsol}
<script src="{p}assets/site.js?v={v_js}" defer></script>
</body>
</html>
"""


def construieste_pagina(pag, absolute=False):
    p = "/" if absolute else prefix_pentru(pag["cale"])
    corp = "\n".join(BLOCURI[b["tip"]](b, p) for b in pag["blocuri"])

    indexare = pag.get("indexare", True)
    robots = "" if indexare else '<meta name="robots" content="noindex,follow">\n'
    canonic = ""
    if DOMENIU and indexare:
        canonic = f'<link rel="canonical" href="{absolut(pag["cale"])}">\n'

    og = (f'{DOMENIU}/assets/foto/social-preview.webp' if DOMENIU
          else f"{p}assets/foto/social-preview.webp")

    # paginile fara deschidere mare incep direct sub antet
    prima = pag["blocuri"][0]["tip"]
    clasa_body = ' class="pagina-simpla"' if prima == "titlu_pagina" else ""

    return SABLON.format(
        titlu=pag["titlu_tab"], descriere=pag["descriere"], robots=robots,
        canonic=canonic, og_imagine=og, p=p, structurate=date_structurate(pag, p),
        antet=antet(p, pag["cale"]), corp=corp, subsol=subsol(p),
        clasa_body=clasa_body, v_css=V_CSS, v_js=V_JS)


def scrie(pag, absolute=False):
    cale = pag["cale"]
    fisier = RADACINA / (cale + "index.html" if cale != "404.html" else "404.html")
    fisier.parent.mkdir(parents=True, exist_ok=True)
    fisier.write_text(construieste_pagina(pag, absolute), encoding="utf-8")
    return fisier.relative_to(RADACINA)


def sitemap():
    if not DOMENIU:
        return None
    azi = date.today().isoformat()
    randuri = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for pag in C.PAGINI:
        if not pag.get("indexare", True):
            continue
        randuri += ["  <url>", f"    <loc>{absolut(pag['cale'])}</loc>",
                    f"    <lastmod>{azi}</lastmod>", "  </url>"]
    randuri.append("</urlset>")
    (RADACINA / "sitemap.xml").write_text("\n".join(randuri) + "\n", encoding="utf-8")

    robots = RADACINA / "robots.txt"
    text = "User-agent: *\nAllow: /\n"
    text += f"\nSitemap: {DOMENIU}/sitemap.xml\n"
    robots.write_text(text, encoding="utf-8")
    return len([p for p in C.PAGINI if p.get("indexare", True)])


def main():
    for pag in C.PAGINI:
        print("  ", scrie(pag))
    print("  ", scrie(C.PAGINA_404, absolute=True))

    manifest = RADACINA / "site.webmanifest"
    manifest.write_text(json.dumps({
        "name": C.SITE["nume_lung"], "short_name": "F.A.M.s",
        "start_url": "./", "display": "standalone",
        "background_color": "#f6f1e8", "theme_color": "#f6f1e8",
        "icons": [{"src": "assets/foto/fams-mark-192.webp", "sizes": "192x192",
                   "type": "image/webp"},
                  {"src": "assets/foto/fams-mark-288.webp", "sizes": "288x288",
                   "type": "image/webp"}],
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    n = sitemap()
    if n:
        print(f"   sitemap.xml ({n} pagini), robots.txt -> {DOMENIU}")
    else:
        print("   fara domeniu: nu s-au scris canonical/sitemap")
        print("   ruleaza: python3 unelte/configureaza.py --domeniu https://...")


if __name__ == "__main__":
    main()
