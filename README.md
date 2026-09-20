# FAMs Mobile Catering Website

## Included
- Responsive multi-page website: Home, About, Weddings, Private Parties, Corporate Events, Special Occasions, Gallery, FAQ, Contact, Privacy, Thank-you, 404.
- Real FAMs logo and van images supplied in the chat, optimized as WebP.
- Premium black/gold/ivory design with parallax and reduced-motion fallback.
- Detailed event quote form prepared for Netlify Forms.
- Semantic static HTML, unique metadata, internal linking and JSON-LD.
- Organization, LocalBusiness/FoodEstablishment, WebSite, Service, FAQPage and Breadcrumb structured data.
- robots.txt, llms.txt and production sitemap generator.
- No invented phone, email, address, reviews or ratings.

## Preview
Run inside the website folder:
python3 -m http.server 8080

Then open http://localhost:8080

## Before launch
A sitemap requires the real production domain. Run:
python3 configure.py --domain https://YOUR-REAL-DOMAIN.co.uk

That creates sitemap.xml, adds its absolute URL to robots.txt, and makes canonical/OpenGraph image URLs absolute.

## Contact form
The form is Netlify Forms compatible. If hosted on Netlify, submissions can appear in the site's Forms dashboard after deployment.
If hosted elsewhere, connect the form to your chosen endpoint/backend.

## Contact details
No email, phone, street address, social link, review count or company number was fabricated. Add the real business details when available.
