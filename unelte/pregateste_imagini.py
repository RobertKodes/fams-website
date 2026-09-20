#!/usr/bin/env python3
"""Pregateste fotografiile site-ului din sursele originale.

De ce exista scriptul:

Singurele fotografii reale sunt patru cadre cu duba, exportate candva ca un
colaj de 1152x1536 (`surse/fams-van-collage.webp`). Decupajele individuale
livrate in arhiva erau taiate neglijent din acel colaj - `van-rear.webp` avea
lipita in partea de sus o fasie de 50px de asfalt din cadrul de deasupra, plus
linia alba dintre cadre. Aici retaiem totul din colaj, pe cadrane curate.

Rezolutia sursei este mica (~560x750 per cadran) si nu poate fi inventata.
Consecinta de design, respectata de CSS: nicio fotografie nu se afiseaza mai
lata de 340px logici. Asa fiecare imagine ajunge pe ecran la 1.6x-2x densitate,
adica se vede clara, in loc sa fie intinsa si moale.

Rulare:  python3 unelte/pregateste_imagini.py
"""

import json
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont

RADACINA = Path(__file__).resolve().parent.parent
SURSE = RADACINA / "surse"
IESIRE = RADACINA / "assets" / "foto"

# Cadranele colajului, masurate: linia alba dintre ele cade pe x=564..573 si
# y=747..752, deci taiem pana la ea, nu prin ea.
CADRANE = {
    "fata":        (0, 0, 564, 747),
    "lateral":     (574, 0, 1152, 747),
    "spate":       (0, 753, 564, 1536),
    "spate-unghi": (574, 753, 1152, 1536),
}

# Decupaj final in cadran, normalizat la 4:5 portret ca sa se alinieze in pagina.
# Valorile taie cerul in plus de sus si asfaltul mort de jos.
DECUPAJE = {
    "fata":        (4, 25, 564, 725),
    "lateral":     (0, 12, 578, 734),
    "spate":       (0, 40, 564, 745),
    "spate-unghi": (0, 30, 578, 752),
}

# Numele publice ale fisierelor (site-ul e in engleza, scripturile in romana).
NUME_PUBLIC = {
    "fata": "van-front",
    "lateral": "van-side",
    "spate": "van-rear",
    "spate-unghi": "van-rear-angle",
}

LATIMI = [280, 420, 560]

NEGRU = (10, 9, 8)
IVORIU = (243, 238, 229)
AUR = (201, 164, 92)
GRI = (148, 139, 126)


def curata(im):
    """Corectie de ton discreta: cadre britanice innorate, ies cenusii.

    Nimic agresiv - un filtru vizibil ar arata mai rau decat poza originala.
    """
    im = ImageEnhance.Contrast(im).enhance(1.06)
    im = ImageEnhance.Color(im).enhance(1.05)
    im = ImageEnhance.Brightness(im).enhance(1.02)
    return coboara_luminile(im)


def coboara_luminile(im, prag=168, factor=.58):
    """Comprima doar luminile, lasand umbrele neatinse.

    Pe fundal negru, cerul alb-albastru al pozelor tipa si trage ochiul de pe
    duba. Scazand luminozitatea intregii imagini, duba (deja aproape neagra)
    s-ar inchide de tot. Curba asta atinge doar valorile peste prag: cerul
    coboara de la 255 la ~219, duba ramane cum e.
    """
    lut = [v if v < prag else round(prag + (v - prag) * factor) for v in range(256)]
    return im.point(lut * len(im.getbands()))


def redimensioneaza(im, latime):
    """Micsorare Lanczos + unsharp usor.

    Micsorarea aduna detaliu pe pixel; unsharp-ul recupereaza muchiile pierdute
    la reesantionare. Pragul 3 tine zgomotul din cer nemodificat.
    """
    if latime >= im.width:
        out = im.copy()
    else:
        inalt = round(im.height * latime / im.width)
        out = im.resize((latime, inalt), Image.LANCZOS)
    return out.filter(ImageFilter.UnsharpMask(radius=0.8, percent=55, threshold=3))


def font(nume, marime):
    for cale in (f"/System/Library/Fonts/Supplemental/{nume}",):
        p = Path(cale)
        if p.exists():
            try:
                return ImageFont.truetype(str(p), marime)
            except OSError:
                pass
    return ImageFont.load_default()


def spatiat(desen, xy, text, f, culoare, spatiu):
    """Scrie text cu tracking (Pillow nu are letter-spacing)."""
    x, y = xy
    for ch in text:
        desen.text((x, y), ch, font=f, fill=culoare)
        x += desen.textlength(ch, font=f) + spatiu
    return x - spatiu


def latime_spatiata(desen, text, f, spatiu):
    return sum(desen.textlength(c, font=f) for c in text) + spatiu * (len(text) - 1)


def rozeta(logo, latime):
    """Logo-ul decupat rotund, ca o pecete.

    Sursa e un patrat negru cu inelul auriu in mijloc. Pe hartia ivoriu un
    patrat negru arata lipit; discul negru cu inel auriu arata intentionat.
    Cercul inelului, masurat pe pixelii aurii: centru (265, 322), raza 248.
    """
    cx, cy, raza = 265, 322, 250
    disc = logo.crop((cx - raza, cy - raza, cx + raza, cy + raza)).convert("RGBA")
    # masca la rezolutie 4x, apoi micsorata: margine curata, fara zimti
    m = Image.new("L", (disc.width * 4, disc.height * 4), 0)
    ImageDraw.Draw(m).ellipse((0, 0, m.width - 1, m.height - 1), fill=255)
    disc.putalpha(m.resize(disc.size, Image.LANCZOS))
    return disc.resize((latime, latime), Image.LANCZOS)


def granulatie(latura=128):
    """Dala de zgomot pentru fundalul negru.

    Negrul plat face benzi vizibile pe ecrane mari si arata ieftin. Peste el,
    3% zgomot (din CSS) da senzatia de hartie tiparita. Zgomotul e gri neutru
    si se repeta la 128px - la opacitatea folosita, repetitia nu se vede.
    """
    import random
    random.seed(7)  # aceeasi dala la fiecare rulare, ca sa nu se schimbe hash-ul
    im = Image.new("L", (latura, latura))
    im.putdata([random.randint(0, 255) for _ in range(latura * latura)])
    return im.convert("RGB")


def cartela_sociala(foto, logo):
    """Imaginea de 1200x630 pentru partajare (WhatsApp, Facebook, X).

    Sursa livrata era 1200x1462 - format portret, pe care retelele il taie prost.
    """
    W, H = 1200, 630
    card = Image.new("RGB", (W, H), NEGRU)
    d = ImageDraw.Draw(card)

    # fotografia, in dreapta, taiata la inaltimea cartelei
    lat_foto = 430
    f = foto.copy()
    scal = lat_foto / f.width
    f = f.resize((lat_foto, round(f.height * scal)), Image.LANCZOS)
    if f.height > H:
        sus = (f.height - H) // 2
        f = f.crop((0, sus, lat_foto, sus + H))
    else:
        f = f.resize((lat_foto, H), Image.LANCZOS)
    card.paste(f, (W - lat_foto, 0))

    lg = rozeta(logo, 150)
    card.paste(lg, (96, 92), lg)

    titlu = font("Didot.ttc", 68)
    eticheta = font("Futura.ttc", 21)
    d.text((96, 268), "Family food,", font=titlu, fill=IVORIU)
    d.text((96, 344), "beautifully served.", font=titlu, fill=IVORIU)
    d.line([(96, 452), (196, 452)], fill=AUR, width=2)
    spatiat(d, (96, 484), "MOBILE CATERING", eticheta, AUR, 5)
    spatiat(d, (96, 522), "SURREY", eticheta, GRI, 5)
    # linie aurie care separa fotografia de text
    d.line([(W - lat_foto - 1, 0), (W - lat_foto - 1, H)], fill=AUR, width=1)
    return card


def main():
    IESIRE.mkdir(parents=True, exist_ok=True)
    colaj = Image.open(SURSE / "fams-van-collage.webp").convert("RGB")

    taiate = {}
    manifest = {}
    for cheie, cadran in CADRANE.items():
        im = curata(colaj.crop(cadran).crop(DECUPAJE[cheie]))
        taiate[cheie] = im
        nume = NUME_PUBLIC[cheie]
        for lat in LATIMI:
            if lat > im.width:
                continue
            ies = redimensioneaza(im, lat)
            ies.save(IESIRE / f"{nume}-{lat}.webp", "WEBP", quality=88, method=6)
        disp = [l for l in LATIMI if l <= im.width]
        manifest[nume] = {"w": im.width, "h": im.height, "latimi": disp}
        print(f"{nume:16} sursa {im.width}x{im.height} -> " +
              ", ".join(str(l) for l in disp))

    # colajul intreg, pentru pagina de galerie (afisat la max 560px)
    for lat in (560, 840):
        redimensioneaza(colaj, lat).save(
            IESIRE / f"van-collage-{lat}.webp", "WEBP", quality=86, method=6)

    logo = Image.open(SURSE / "fams-logo.webp").convert("RGBA")
    for lat in (96, 192, 288):
        r = rozeta(logo, lat)
        r.save(IESIRE / f"fams-mark-{lat}.webp", "WEBP", quality=92, method=6)
    print(f"{'fams-mark':16} rozeta rotunda -> 96, 192, 288")

    for lat in (120, 240, 360):
        l = logo.copy()
        l.thumbnail((lat, lat * 2), Image.LANCZOS)
        l.save(IESIRE / f"fams-logo-{lat}.webp", "WEBP", quality=92, method=6)
    print(f"{'fams-logo':16} sursa {logo.width}x{logo.height} -> 120, 240, 360")

    (IESIRE / "dimensiuni.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    granulatie().save(IESIRE / "grain.png", "PNG", optimize=True)

    cartela_sociala(taiate["spate-unghi"], logo).save(
        IESIRE / "social-preview.webp", "WEBP", quality=88, method=6)
    print("social-preview   1200x630")


if __name__ == "__main__":
    main()
