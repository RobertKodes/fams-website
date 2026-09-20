#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scrie domeniul de productie si reconstruieste site-ul cu el.

Fara domeniu, paginile nu pot declara `canonical` si nici nu se poate genera
`sitemap.xml`: amandoua cer URL-uri absolute. Iar imaginea de partajare
(Facebook, WhatsApp) trebuie sa fie tot un URL absolut, altfel unele retele o
ignora si linkul apare gol.

Site-ul merge si fara asta - doar partea de SEO ramane incompleta.

    python3 unelte/configureaza.py --domeniu https://fams-catering.netlify.app
    python3 unelte/configureaza.py --sterge     # inapoi la cai relative
"""

import argparse
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

RADACINA = Path(__file__).resolve().parent.parent
FISIER = RADACINA / "domeniu.txt"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--domeniu", help="ex. https://exemplu.co.uk")
    ap.add_argument("--sterge", action="store_true", help="renunta la domeniu")
    a = ap.parse_args()

    if a.sterge:
        FISIER.unlink(missing_ok=True)
        (RADACINA / "sitemap.xml").unlink(missing_ok=True)
        (RADACINA / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
        print("domeniu sters")
    elif a.domeniu:
        u = urlparse(a.domeniu)
        if u.scheme not in ("http", "https") or not u.netloc:
            sys.exit("Da domeniul intreg, de exemplu: https://exemplu.co.uk")
        FISIER.write_text(a.domeniu.rstrip("/") + "\n", encoding="utf-8")
        print("domeniu:", a.domeniu.rstrip("/"))
    else:
        sys.exit("Foloseste --domeniu <url> sau --sterge")

    subprocess.run([sys.executable, str(RADACINA / "construieste.py")], check=True)


if __name__ == "__main__":
    main()
