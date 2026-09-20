#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import urlparse
from datetime import date
import argparse
p=argparse.ArgumentParser()
p.add_argument("--domain",required=True)
a=p.parse_args()
domain=a.domain.rstrip("/")
u=urlparse(domain)
if u.scheme not in {"http","https"} or not u.netloc: raise SystemExit("Use a full domain, e.g. https://example.co.uk")
root=Path(__file__).resolve().parent
paths=["/","/about/","/weddings/","/private-parties/","/corporate-events/","/special-occasions/","/gallery/","/faq/","/contact/","/privacy/"]
xml=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for x in paths: xml += ["  <url>",f"    <loc>{domain}{x}</loc>",f"    <lastmod>{date.today().isoformat()}</lastmod>","  </url>"]
xml.append("</urlset>")
(root/"sitemap.xml").write_text("\n".join(xml)+"\n",encoding="utf-8")
robots="\n".join(line for line in (root/"robots.txt").read_text(encoding="utf-8").splitlines() if not line.startswith("Sitemap:"))
(root/"robots.txt").write_text(robots.rstrip()+f"\n\nSitemap: {domain}/sitemap.xml\n",encoding="utf-8")
for html in root.rglob("*.html"):
    txt=html.read_text(encoding="utf-8")
    txt=txt.replace('rel="canonical" href="/',f'rel="canonical" href="{domain}/')
    txt=txt.replace('property="og:image" content="/',f'property="og:image" content="{domain}/')
    html.write_text(txt,encoding="utf-8")
print("Production SEO configured for",domain)
