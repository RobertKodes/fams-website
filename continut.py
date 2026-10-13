# -*- coding: utf-8 -*-
"""Tot textul site-ului, intr-un singur loc.

Regula pe care o respecta continutul de aici: nu se inventeaza nimic.
E-mailul, retelele sociale, numarul de WhatsApp si motto-ul vin de la client
(discutia din septembrie 2026). Nu exista adresa, recenzii, numar de evenimente
sau preturi, pentru ca nu le-am primit. Numarul de WhatsApp NU se afiseaza pe
site: e doar destinatia mesajului generat de formular (clientul nu vrea apeluri).

Dupa orice modificare aici: python3 construieste.py
"""

SITE = {
    "nume": "F.A.M.s",
    "nume_lung": "F.A.M.s Mobile Catering",
    "domeniu": "",  # se completeaza cu unelte/configureaza.py --domeniu https://...
    "zona": "Surrey",
    "an": 2021,
    "slogan": "Good food. Great people. Lasting memories.",
    "motto": "Creating memories",
    "email": "fams.company2021@gmail.com",
    # Destinatia mesajului de WhatsApp de dupa formular, in format international
    # fara + si fara spatii. Nu apare nicaieri in pagina.
    "whatsapp": "447944643757",
    "social": [
        ("Instagram", "https://www.instagram.com/fams.company2021"),
        ("Facebook", "https://www.facebook.com/share/1DTDHNFWVt/"),
        ("TikTok", "https://www.tiktok.com/@fams.company2021"),
    ],
}

# Datele legale ale firmei. Le cer Electronic Commerce Regulations 2002 si,
# pentru Ltd, Companies Act: cine sta in spatele site-ului si unde poate fi
# gasit. Ce e gol nu apare pe site; ce se completeaza apare in subsol si pe
# pagina de confidentialitate. NU se inventeaza - se cer de la client.
FIRMA = {
    # "Ion Popescu" (sole trader) sau "F.A.M.s Catering Ltd" (companie)
    "nume_legal": "",
    "forma": "",            # "sole trader", "partnership" sau "limited company"
    "adresa": "",           # adresa geografica a afacerii (nu e obligatoriu acasa)
    "nr_companie": "",      # doar pentru Ltd, ex. "12345678"
    "tva": "",              # doar daca sunt platitori de TVA, ex. "GB123456789"
    "fhrs_id": "",          # id-ul din ratings.food.gov.uk, daca vor sa arate ratingul
}

# Cat tinem cererile care nu devin rezervari. Decizia clientului, nu a noastra;
# 12 luni e o valoare obisnuita si o spunem ca atare pe pagina de confidentialitate.
PASTRARE_CERERI = "12 months"

# Povestea numelui: initialele familiei. Apare pe prima pagina si la About.
FAMILIA = [("F", "Florin"), ("A", "Alexandra"), ("M", "Mirela"), ("s", "Sofia")]

# Ordinea din meniu. (cale, eticheta)
NAV = [
    ("about/", "About"),
    ("weddings/", "Weddings"),
    ("private-parties/", "Parties"),
    ("corporate-events/", "Corporate"),
    ("special-occasions/", "Occasions"),
    ("gallery/", "Gallery"),
    ("faq/", "FAQ"),
]

FOTO = {
    "fata": ("van-front", "The FAMs van from the front, matte black with gold lettering"),
    "lateral": ("van-side", "The side of the FAMs van, showing the F.A.M.s 2021 logo"),
    "spate": ("van-rear", "The back of the FAMs van: Mobile Catering, Creating Memories"),
    "unghi": ("van-rear-angle", "The FAMs van from the rear three-quarter, parked under a tree"),
}

# ------------------------------------------------- confidentialitate (UK GDPR)
# Continutul cerut de articolele 13 UK GDPR: cine e operatorul, ce date, de ce,
# pe ce temei, cui ajung, transferuri, cat se tin, drepturi, plangere la ICO.

def _cine_suntem():
    f = FIRMA
    if f["nume_legal"]:
        cine = (f"F.A.M.s Mobile Catering is run by {f['nume_legal']}"
                + (f", a {f['forma']}" if f["forma"] else "") + ". ")
    else:
        cine = "F.A.M.s Mobile Catering is a family business based in Surrey. "
    if f["nr_companie"]:
        cine += f"Registered in England and Wales, company number {f['nr_companie']}. "
    if f["adresa"]:
        cine += f"Our address is {f['adresa']}. "
    cine += ("We decide how the details you send us are used, which makes us the "
             f"“controller” under UK data protection law. Contact: {SITE['email']}.")
    return cine


def _cine_suntem_scurt():
    f = FIRMA
    text = "F.A.M.s Mobile Catering"
    if f["nume_legal"]:
        text += f", run by {f['nume_legal']}"
    if f["nr_companie"]:
        text += f" (company number {f['nr_companie']})"
    if f["adresa"]:
        text += f", {f['adresa']}"
    return (text + ". You can reach us at " + SITE["email"] + ". In these terms, "
            "“we” and “us” means F.A.M.s, and “you” means the person making the booking.")


SECTIUNI_CONFIDENTIALITATE = [
    ("Who we are", [_cine_suntem()]),
    ("What you give us",
     ["Through the enquiry form: your name, email, phone number, company (if any), "
      "and the details of your event — type, date, times, guest numbers, location, "
      "the food you have in mind, allergies and dietary requirements, how you heard "
      "about us, and anything else you add.",
      "If you message or email us directly, we receive whatever you choose to send."]),
    ("Why we use it, and on what basis",
     ["To reply to your enquiry, prepare a quote and, if you book, plan and deliver "
      "the catering. The legal basis is that you have asked us to take these steps "
      "before entering into a contract, and then to perform it.",
      "Allergy and dietary details can count as health information. We use them "
      "only to plan food that is safe for your guests, on the basis of your "
      "explicit consent, which you give with the tick box on the form. Please give "
      "us only what is relevant to the catering.",
      "We do not sell your details, we do not use them for marketing, and we do not "
      "use them to make automated decisions about you."]),
    ("Who else sees it",
     ["Netlify, Inc., which hosts this site and stores form submissions. Netlify is "
      "based in the United States and certified under the UK Extension to the "
      "EU–US Data Privacy Framework, which UK law recognises as an adequate "
      "safeguard for transfers to the US.",
      "Google (Gmail), which receives the email copy of your enquiry.",
      "WhatsApp (Meta). When you send the form, your details are written into a "
      "WhatsApp message on your own device. Nothing reaches WhatsApp unless you "
      "press send there yourself; if you do, WhatsApp’s own privacy policy applies "
      "to that message.",
      "Beyond these, we share your details only if the law requires it."]),
    ("How long we keep it",
     [f"Enquiries that don’t become bookings are deleted within {PASTRARE_CERERI}. "
      "For bookings, we keep what we need to deliver the event, and invoices and "
      "accounting records for as long as HMRC requires (normally six years)."]),
    ("Your rights",
     ["You can ask for a copy of what we hold about you, ask us to correct it, "
      "delete it or stop using it, and withdraw your consent for allergy details at "
      "any time. Write to " + SITE["email"] + ". We will reply within one month.",
      "If you are unhappy with how we have handled your details, please tell us "
      "first so we can put it right. You can also complain to the Information "
      "Commissioner’s Office: <a href=\"https://ico.org.uk/make-a-complaint/\">"
      "ico.org.uk/make-a-complaint</a>, 0303 123 1113."]),
    ("Cookies and tracking",
     ["This site sets no cookies and uses no analytics, advertising or tracking "
      "tools. Fonts and images are served from this site itself, so visiting it "
      "does not send your details to Google or anyone else. If that ever changes, "
      "this page will change first."]),
    ("Links to other sites",
     ["Our Instagram, Facebook and TikTok links open those platforms, which have "
      "their own privacy policies."]),
]

# ----------------------------------------------------------------- paginile

PAGINI = [

# ---------------------------------------------------------------- acasa ----
{
    "cale": "",
    "titlu_tab": "F.A.M.s Mobile Catering | Weddings, Parties & Events in Surrey",
    "descriere": "Family-run mobile catering for weddings, private parties and "
                 "corporate events across Surrey. Cooked fresh, brought to you.",
    "blocuri": [
        {"tip": "deschidere",
         "eticheta": "Family-run mobile catering in Surrey, since 2021",
         "titlu": "Family food,<br>beautifully served.",
         "lede": "F.A.M.s is Florin, Alexandra, Mirela and Sofia. We cook fresh, we "
                 "bring the kitchen with us, and we cater weddings, parties and "
                 "events across Surrey.",
         "actiuni": [("contact/", "Start an enquiry", "plin"),
                     ("#catering", "What we cater", "text")],
         "foto": "unghi",
         "legenda": "The van, parked up between jobs"},

        {"tip": "nume",
         "titlu": "One family, four initials.",
         "text": "The name on the van is us. F.A.M.s is a family business, and "
                 "every event we cater gets the four of us.",
         "legatura": ("about/", "Read our story")},

        {"tip": "servicii",
         "id": "catering",
         "eticheta": "What we cater",
         "titlu": "Four kinds of day,<br>one way of working.",
         "randuri": [
             ("weddings/", "Weddings",
              "We work to your timings, your venue and your guest list — not to a fixed package."),
             ("private-parties/", "Private parties",
              "Birthdays, anniversaries, christenings, or a garden full of people on a Saturday."),
             ("corporate-events/", "Corporate events",
              "Launches, open days and staff days. We bring our own kitchen, so you don’t need one."),
             ("special-occasions/", "Special occasions",
              "Anything that doesn’t fit a category. Tell us what you’re planning."),
         ]},

        {"tip": "cerneala",
         "titlu": "Good food.<br>Great people.<br>Lasting memories.",
         "subsol": "Creating memories, since 2021"},

        {"tip": "trio",
         "eticheta": "On the road",
         "titlu": "The kitchen comes to you.",
         "text": "A black-and-gold VW Crafter, and the reason we can cater a village "
                 "hall, a marquee or a garden with no kitchen in it.",
         "legatura": ("gallery/", "See the gallery"),
         "foto": [("unghi", "Rear three-quarter"),
                  ("lateral", "Nearside"),
                  ("fata", "Front")]},

        {"tip": "pasi",
         "eticheta": "How it works",
         "titlu": "Three steps,<br>then a good day.",
         "pasi": [
             ("Tell us about it",
              "The date, the place, and roughly how many people you need fed."),
             ("We talk it through",
              "Menu, serving times, and how the food actually reaches your guests."),
             ("We park and cook",
              "You spend the day with your guests instead of in a kitchen."),
         ]},

        {"tip": "final",
         "titlu": "Tell us what<br>you’re planning.",
         "text": "A date, a rough guest number, a postcode. Send whatever you have "
                 "and we’ll take it from there.",
         "actiune": ("contact/", "Start an enquiry")},
    ],
},

# ---------------------------------------------------------------- about ----
{
    "cale": "about/",
    "titlu_tab": "About F.A.M.s | A Family Catering Business in Surrey",
    "descriere": "F.A.M.s is a family business: Florin, Alexandra, Mirela and Sofia. "
                 "Mobile catering across Surrey since 2021, with one motto: creating memories.",
    "blocuri": [
        {"tip": "deschidere",
         "eticheta": "About us",
         "titlu": "Four names on<br>the side of a van.",
         "lede": "F.A.M.s is Florin, Alexandra, Mirela and Sofia. The initials came "
                 "first. The van came in 2021.",
         "actiuni": [("contact/", "Start an enquiry", "plin")],
         "foto": "lateral",
         "legenda": "The F.A.M.s 2021 logo on the nearside"},

        {"tip": "nume",
         "titlu": "Where the name comes from.",
         "text": "Put our first initials side by side and you get F.A.M.s. Say it "
                 "out loud and it is also what we are: a fam."},

        {"tip": "proza",
         "eticheta": "A family business",
         "titlu": "A family that cooks,<br>for other people’s occasions.",
         "paragrafe": [
             "F.A.M.s started in 2021 as a family business, and it still is one. "
             "We cater weddings, private parties, corporate events and special "
             "occasions across Surrey and, by arrangement, further out.",
             "Food is prepared fresh for the event, and the person you speak to when "
             "you enquire is one of the people who turns up on the day. There is no "
             "office, no account manager and no fixed package. You tell us about the "
             "occasion; we tell you what we would do with it, and what it would cost.",
         ]},

        {"tip": "proza",
         "eticheta": "Our motto",
         "titlu": "Creating memories.",
         "paragrafe": [
             "It’s written on the back of the van, and it’s the test we hold every "
             "job to. Nobody remembers the catering at a good event — they remember "
             "the day. The food is there to help that happen: on time, generous, and "
             "good enough that people go back for seconds.",
             "A wedding, a fortieth, a christening, a team finally in one place: these "
             "are days people talk about years later. We would like to be a small part "
             "of why.",
         ]},

        {"tip": "puncte",
         "eticheta": "What matters to us",
         "titlu": "Three things we<br>don’t compromise on.",
         "puncte": [
             ("Cooked fresh",
              "Prepared for your event, on the day, not pulled out of a freezer the week before."),
             ("You deal with us",
              "The family handles the enquiry, the menu and the service. Nobody hands you over."),
             ("Shaped to the day",
              "Guests, venue and timings come first. The menu is built after that, not before."),
         ]},

        {"tip": "cerneala",
         "titlu": "Good food.<br>Great people.<br>Lasting memories.",
         "subsol": "Creating memories, since 2021"},

        {"tip": "final",
         "titlu": "Come and meet<br>the van.",
         "text": "Tell us about your event and we’ll tell you honestly whether we’re "
                 "the right fit for it.",
         "actiune": ("contact/", "Start an enquiry")},
    ],
},

# -------------------------------------------------------------- weddings ---
{
    "cale": "weddings/",
    "titlu_tab": "Wedding Catering in Surrey | F.A.M.s Mobile Catering",
    "descriere": "Family-run mobile wedding catering across Surrey. We bring the "
                 "kitchen, work to your timings and cook fresh on the day.",
    "blocuri": [
        {"tip": "deschidere",
         "eticheta": "Weddings",
         "titlu": "Wedding catering,<br>without the<br>fixed package.",
         "lede": "Mobile catering for weddings across Surrey and beyond — built "
                 "around your day rather than around a menu card.",
         "actiuni": [("contact/", "Ask about your date", "plin")],
         "foto": "unghi",
         "legenda": "The van travels to the venue"},

        {"tip": "proza",
         "eticheta": "How we plan it",
         "titlu": "Weddings run<br>on timings.",
         "paragrafe": [
             "Tell us when your guests arrive, when they sit down, and when the "
             "evening food should appear. We build the catering backwards from those "
             "three moments, because that is what decides everything else.",
             "Then we talk about the food itself: what you want, what your guests "
             "need, and what will still be good an hour after it leaves the van.",
         ]},

        {"tip": "puncte",
         "eticheta": "What we’ll ask you",
         "titlu": "The details that<br>actually matter.",
         "puncte": [
             ("Your venue",
              "Marquee, barn, garden or hall. We bring the kitchen, so the venue doesn’t need one."),
             ("Access and parking",
              "Where the van can stand, how far it is to your guests, and what the ground is like."),
             ("Your guest list",
              "Numbers, children, and any allergies or dietary requirements, in full."),
         ]},

        {"tip": "citat",
         "text": "Family food. Beautifully served. Memories made.",
         "sursa": "F.A.M.s"},

        {"tip": "final",
         "titlu": "Is your date<br>still free?",
         "text": "Send the date and the postcode first — everything else can follow.",
         "actiune": ("contact/", "Ask about your date")},
    ],
},

# ------------------------------------------------------- private parties ---
{
    "cale": "private-parties/",
    "titlu_tab": "Private Party Catering in Surrey | F.A.M.s Mobile Catering",
    "descriere": "Mobile catering for birthdays, anniversaries, christenings and "
                 "private celebrations across Surrey. Family-run, cooked fresh.",
    "blocuri": [
        {"tip": "deschidere",
         "eticheta": "Private parties",
         "titlu": "Parties that<br>need feeding.",
         "lede": "Birthdays, anniversaries, christenings — and the ones with no "
                 "particular reason behind them.",
         "actiuni": [("contact/", "Start an enquiry", "plin")],
         "foto": "lateral",
         "legenda": "Nearside, with the full logo"},

        {"tip": "proza",
         "eticheta": "At your place",
         "titlu": "Your garden doesn’t<br>need a kitchen.",
         "paragrafe": [
             "The van is the kitchen. It parks up, we cook, and your own kitchen "
             "stays free for the things you actually want it for — drinks, ice, and "
             "somewhere to put the cake.",
             "Small gatherings and large ones are both fine. What we need to know is "
             "how many people, what time they eat, and where we can stand.",
         ]},

        {"tip": "puncte",
         "eticheta": "Worth mentioning",
         "titlu": "Three things to<br>tell us early.",
         "puncte": [
             ("Numbers",
              "A rough figure is enough to start with. We’ll firm it up closer to the day."),
             ("Timing",
              "One sitting or food out across the evening — it changes how we plan."),
             ("Dietary requirements",
              "Allergies especially. Give us the full detail so we can be straight with you."),
         ]},

        {"tip": "final",
         "titlu": "Got a date<br>in the diary?",
         "text": "Tell us what you’re planning and we’ll come back with options.",
         "actiune": ("contact/", "Start an enquiry")},
    ],
},

# ------------------------------------------------------ corporate events ---
{
    "cale": "corporate-events/",
    "titlu_tab": "Corporate Event Catering in Surrey | F.A.M.s Mobile Catering",
    "descriere": "Mobile catering for launches, open days, staff days and client "
                 "events across Surrey. We bring our own kitchen and work to your schedule.",
    "blocuri": [
        {"tip": "deschidere",
         "eticheta": "Corporate",
         "titlu": "Catering that<br>turns up on time.",
         "lede": "Launches, open days, staff days and client events across Surrey — "
                 "run to your schedule, not ours.",
         "actiuni": [("contact/", "Start an enquiry", "plin")],
         "foto": "fata",
         "legenda": "Front three-quarter"},

        {"tip": "proza",
         "eticheta": "How it works on site",
         "titlu": "We don’t need<br>your kitchen.",
         "paragrafe": [
             "We arrive with everything, set up outside, and work in whatever window "
             "you give us. Offices, yards, sites and venues without catering "
             "facilities are all straightforward.",
             "What we need from you is a headcount, the window your people need to be "
             "fed in, and somewhere the van can stand.",
         ]},

        {"tip": "puncte",
         "eticheta": "Before you enquire",
         "titlu": "Have these<br>three to hand.",
         "puncte": [
             ("Headcount",
              "Approximate is fine. Tell us if it might move, and by how much."),
             ("The window",
              "A fixed lunch hour and an all-day open day are very different jobs."),
             ("Access",
              "Where we can park, what the surface is like, and who lets us in."),
         ]},

        {"tip": "final",
         "titlu": "Feeding a team,<br>or a whole open day?",
         "text": "Send the date, the headcount and the postcode, and we’ll come back to you.",
         "actiune": ("contact/", "Start an enquiry")},
    ],
},

# ----------------------------------------------------- special occasions ---
{
    "cale": "special-occasions/",
    "titlu_tab": "Special Occasion Catering in Surrey | F.A.M.s Mobile Catering",
    "descriere": "Christenings, engagements, anniversaries, wakes and street parties "
                 "— mobile catering for occasions that don’t come with a template.",
    "blocuri": [
        {"tip": "deschidere",
         "eticheta": "Special occasions",
         "titlu": "Everything else.",
         "lede": "Christenings, engagements, anniversaries, wakes, street parties — "
                 "occasions that don’t come with a template.",
         "actiuni": [("contact/", "Start an enquiry", "plin")],
         "foto": "spate",
         "legenda": "Mobile Catering, Creating Memories"},

        {"tip": "proza",
         "eticheta": "No template",
         "titlu": "Tell us the occasion<br>before the menu.",
         "paragrafe": [
             "Some days need feeding quietly and well; others need to feel like a "
             "celebration from the first plate. The food follows from that, so we ask "
             "about the day before we ask about the menu.",
             "If you are arranging something difficult — a wake, or a gathering at "
             "short notice — say so when you enquire. We will keep it simple and "
             "handle the details.",
         ]},

        {"tip": "trio",
         "eticheta": "The van",
         "titlu": "Wherever it needs to be.",
         "text": "Surrey is home. Further out is possible by arrangement — send the "
                 "postcode and we’ll tell you straight away.",
         "legatura": ("gallery/", "See the gallery"),
         "foto": [("spate", "Rear"),
                  ("unghi", "Rear three-quarter"),
                  ("fata", "Front")]},

        {"tip": "final",
         "titlu": "Whatever<br>the occasion.",
         "text": "Tell us what’s happening and when, and we’ll tell you what we can do.",
         "actiune": ("contact/", "Start an enquiry")},
    ],
},

# --------------------------------------------------------------- gallery ---
{
    "cale": "gallery/",
    "titlu_tab": "Gallery | F.A.M.s Mobile Catering",
    "descriere": "Photographs of the F.A.M.s mobile catering van. Food and event "
                 "photography will be added as we collect it.",
    "blocuri": [
        {"tip": "titlu_pagina",
         "eticheta": "Gallery",
         "titlu": "The van, for now.",
         "lede": "These are the photographs we actually have. Food and event pictures "
                 "will go up here as we collect them — we would rather show you "
                 "nothing than show you somebody else’s stock photos."},

        {"tip": "galerie",
         "foto": [("unghi", "Rear three-quarter"),
                  ("lateral", "Nearside"),
                  ("spate", "Rear"),
                  ("fata", "Front")]},

        {"tip": "final",
         "titlu": "Want it parked<br>at your event?",
         "text": "Tell us the date and the place.",
         "actiune": ("contact/", "Start an enquiry")},
    ],
},

# ------------------------------------------------------------------- faq ---
{
    "cale": "faq/",
    "titlu_tab": "FAQ | F.A.M.s Mobile Catering",
    "descriere": "Answers to the questions people ask first: where we cater, how "
                 "menus work, dietary requirements, notice period and quotes.",
    "blocuri": [
        {"tip": "titlu_pagina",
         "eticheta": "FAQ",
         "titlu": "The things<br>people ask first.",
         "lede": "If yours isn’t here, put it in the enquiry form and we’ll answer it "
                 "properly."},

        {"tip": "intrebari",
         "intrebari": [
             ("What does F.A.M.s stand for?",
              "Our first initials: Florin, Alexandra, Mirela and Sofia. F.A.M.s is "
              "a family-run mobile catering business, working across Surrey since 2021."),
             ("What sort of events do you cater?",
              "Weddings, private parties, birthdays, anniversaries, christenings, "
              "corporate events and one-off occasions. If you are not sure whether "
              "yours fits, ask."),
             ("Where do you cover?",
              "Surrey is our home patch. We travel to surrounding areas, and further "
              "afield by arrangement. Send your postcode and we will tell you "
              "straight away whether it works."),
             ("Can the menu be changed for our event?",
              "Yes. We start from your guests, venue and timings, then build the menu "
              "to fit. There is no fixed package you have to squeeze into."),
             ("Can you handle allergies and dietary requirements?",
              "Tell us when you enquire, in full. Once your menu is agreed, we give "
              "you written allergen information for every dish, covering the 14 "
              "major allergens, and we talk it through with you. If there is an "
              "allergy we cannot cater for safely, we will tell you plainly."),
             ("How far ahead should we book?",
              "As early as you can, especially for summer weekends. If your event is "
              "soon, ask anyway — sometimes a date is free."),
             ("How do we get a price?",
              "Use the enquiry form with your date, location, guest numbers and what "
              "you have in mind. That is enough for us to come back with something "
              "useful rather than a vague range."),
             ("Can I contact you by email or WhatsApp?",
              "Yes. Email us at fams.company2021@gmail.com, or fill in the enquiry "
              "form: when you send it, WhatsApp opens with your details already "
              "written out, so all you have to do is press send."),
         ]},

        {"tip": "final",
         "titlu": "Still deciding?",
         "text": "Send the question with your enquiry — we’d rather answer it than have you guess.",
         "actiune": ("contact/", "Start an enquiry")},
    ],
},

# --------------------------------------------------------------- contact ---
{
    "cale": "contact/",
    "titlu_tab": "Get a Quote | F.A.M.s Mobile Catering",
    "descriere": "Tell us about your event — date, location, guest numbers and what "
                 "you have in mind — and we will come back to you with a quote.",
    "blocuri": [
        {"tip": "titlu_pagina",
         "eticheta": "Enquiries",
         "titlu": "Tell us about<br>your event.",
         "lede": "The more you put in, the more useful our quote will be. When you "
                 "send it, WhatsApp opens with everything written out for us. "
                 "Nothing here is a commitment."},

        {"tip": "formular"},
    ],
},

# --------------------------------------------------------------- privacy ---
{
    "cale": "privacy/",
    "titlu_tab": "Privacy & Cookies | F.A.M.s Mobile Catering",
    "descriere": "How F.A.M.s Mobile Catering uses the details you send us, who "
                 "sees them, how long we keep them, and your rights under UK GDPR.",
    "indexare": False,
    "blocuri": [
        {"tip": "titlu_pagina",
         "eticheta": "Privacy and cookies",
         "titlu": "What happens to<br>what you send us.",
         "lede": "Short version: we use it to answer your enquiry and run your "
                 "booking, nothing else. This site sets no cookies and has no "
                 "tracking. Last updated 13 October 2026."},

        {"tip": "text_lung",
         "sectiuni": SECTIUNI_CONFIDENTIALITATE},
    ],
},

# --------------------------------------------------------- booking terms ---
# Termenii nu inventeaza cifre (avans, termene, taxe de anulare): trimit la
# oferta scrisa, care le stabileste pentru fiecare eveniment. Asa raman
# adevarati pentru orice comanda, pana cand familia decide valori fixe.
{
    "cale": "booking-terms/",
    "titlu_tab": "Booking Terms | F.A.M.s Mobile Catering",
    "descriere": "The terms on which F.A.M.s Mobile Catering takes bookings: quotes, "
                 "deposits, changes, cancellations, allergies and access for the van.",
    "blocuri": [
        {"tip": "titlu_pagina",
         "eticheta": "Booking terms",
         "titlu": "The small print,<br>in plain English.",
         "lede": "These terms apply to every booking with F.A.M.s Mobile Catering. "
                 "Your written quote sets out the details for your event; where it "
                 "says something different from this page, the quote applies. "
                 "Last updated 13 October 2026."},

        {"tip": "text_lung",
         "sectiuni": [
             ("Who you are booking with",
              [_cine_suntem_scurt()]),
             ("Quotes",
              ["Enquiries and quotes are free and don’t commit you to anything. "
               "Every menu is built for the event, so every quote is written for "
               "you: it sets out the menu, the number of guests, the serving times, "
               "the price, any deposit, the payment dates and how long the quote "
               "stays open."]),
             ("Confirming a booking",
              ["Your date is booked once we have confirmed it to you in writing (by "
               "email or WhatsApp) and received any deposit stated in your quote. "
               "Until then, we can’t hold the date for you."]),
             ("Changes to numbers, menu or timings",
              ["Tell us about changes as early as you can. We will always try to "
               "accommodate them, and we will tell you before the event if a change "
               "affects the price. Final guest numbers and any allergy details are "
               "needed by the date given in your quote, so that we can buy and "
               "prepare the right food."]),
             ("Payment",
              ["Payments are due on the dates and by the methods set out in your "
               "quote or invoice."]),
             ("If you need to cancel",
              ["Please tell us in writing as soon as you know. Any cancellation "
               "charges, and how much of a deposit can be returned, are set out in "
               "your quote; they reflect the food we have bought, the work already "
               "done, and other bookings we have turned away for your date.",
               "Because our catering is booked for a specific date, the 14-day "
               "cancellation period in the Consumer Contracts Regulations 2013 does "
               "not apply to it. This does not affect your other legal rights."]),
             ("If we need to cancel",
              ["We will only cancel for reasons outside our control, such as "
               "serious illness, the van breaking down or dangerous weather. If that "
               "happens we will tell you straight away, help you find an alternative "
               "where we can, and refund everything you have paid us for that event."]),
             ("The venue and the van",
              ["You are responsible for making sure the van has permission to park at "
               "the venue, safe and suitable access, and a reasonably level space to "
               "work from, and for telling us about any rules the venue has. If the "
               "venue needs anything from us, such as insurance or food hygiene "
               "documents, let us know when you book."]),
             ("Allergies and dietary requirements",
              ["Tell us about every allergy and dietary requirement in full, before "
               "the date in your quote. Once your menu is agreed we give you written "
               "information on the 14 major allergens for every dish. Our food is "
               "prepared in a kitchen that handles many ingredients, so we can’t "
               "promise any dish is completely free from traces of an allergen. "
               "<a href=\"../allergens/\">How we handle allergens</a>."]),
             ("Food after service",
              ["Food is prepared to be eaten during the agreed serving times. For "
               "safety, we can’t be responsible for food kept and eaten after we "
               "have left."]),
             ("Our responsibility to you",
              ["We will prepare and serve your food with reasonable care and skill, "
               "as the law requires. Nothing in these terms limits our liability "
               "for death or personal injury caused by our negligence, for fraud, or "
               "for anything else the law does not allow us to limit. Otherwise, we "
               "are not responsible for losses that were not foreseeable when you "
               "booked, or that were caused by things outside our control."]),
             ("If something isn’t right",
              ["Tell us on the day if you can, so that we can put it right there and "
               "then; otherwise, email " + SITE["email"] + " as soon as possible "
               "after the event. We will look into it and reply properly."]),
             ("The law that applies",
              ["These terms are governed by the law of England and Wales. If you live "
               "elsewhere in the UK, you can also bring proceedings in your local "
               "courts."]),
         ]},

        {"tip": "final",
         "titlu": "Questions about<br>the terms?",
         "text": "Ask when you enquire. We would rather explain them than have you guess.",
         "actiune": ("contact/", "Start an enquiry")},
    ],
},

# ------------------------------------------------------------- allergens ---
{
    "cale": "allergens/",
    "titlu_tab": "Allergens & Dietary Requirements | F.A.M.s Mobile Catering",
    "descriere": "How F.A.M.s Mobile Catering handles allergies and dietary "
                 "requirements: written information on the 14 major allergens for "
                 "every dish on your menu.",
    "blocuri": [
        {"tip": "titlu_pagina",
         "eticheta": "Allergens",
         "titlu": "Allergies, taken<br>seriously.",
         "lede": "Every menu we cook is written for one event, so allergen "
                 "information is written for it too."},

        {"tip": "text_lung",
         "sectiuni": [
             ("Tell us early, and in full",
              ["Put every allergy and dietary requirement in your enquiry: who it is "
               "for, what they must avoid, and how severe it is. The earlier we know, "
               "the more we can plan around it."]),
             ("What you get from us",
              ["Once your menu is agreed, we give you written allergen information "
               "for every dish, and we talk it through with you. On the day, ask us "
               "about any dish before you eat it — we will always answer."]),
             ("The 14 major allergens",
              ["UK law names fourteen allergens that we must tell you about whenever "
               "they are in our food:",
               "<ul><li>Celery</li><li>Cereals containing gluten, such as wheat, rye, "
               "barley and oats</li><li>Crustaceans, such as prawns and crab</li>"
               "<li>Eggs</li><li>Fish</li><li>Lupin</li><li>Milk</li>"
               "<li>Molluscs, such as mussels and squid</li><li>Mustard</li>"
               "<li>Tree nuts, such as almonds, hazelnuts and cashews</li>"
               "<li>Peanuts</li><li>Sesame</li><li>Soya</li>"
               "<li>Sulphur dioxide and sulphites</li></ul>"]),
             ("What we can’t promise",
              ["Our food is prepared in a kitchen that handles many ingredients, so "
               "we can’t guarantee any dish is completely free from traces of an "
               "allergen. If an allergy is severe and we can’t cater for it safely, "
               "we will tell you plainly rather than take the risk."]),
             ("Your details",
              ["Allergy information is health information, so we use it only to plan "
               "safe food for your event. <a href=\"../privacy/\">How we handle it</a>."]),
         ]},

        {"tip": "final",
         "titlu": "Planning for<br>an allergy?",
         "text": "Put the details in your enquiry and we’ll come back to you on what "
                 "we can safely offer.",
         "actiune": ("contact/", "Start an enquiry")},
    ],
},

# --------------------------------------------------------- accessibility ---
{
    "cale": "accessibility/",
    "titlu_tab": "Accessibility | F.A.M.s Mobile Catering",
    "descriere": "How the F.A.M.s Mobile Catering website is built to be usable by "
                 "everyone, and how to reach us if something doesn’t work for you.",
    "indexare": False,
    "blocuri": [
        {"tip": "titlu_pagina",
         "eticheta": "Accessibility",
         "titlu": "A site that works<br>for everyone.",
         "lede": "We want anyone to be able to find out about us and send an "
                 "enquiry, however they use the web."},

        {"tip": "text_lung",
         "sectiuni": [
             ("What we have done",
              ["The site aims to meet the Web Content Accessibility Guidelines "
               "(WCAG) 2.2 at level AA. Text has strong contrast against the "
               "background, every page can be used with a keyboard alone, there is a "
               "link to skip straight to the content, images have text descriptions, "
               "and animation is switched off if your device asks for reduced motion.",
               "The text resizes with your browser, and the layout works on phones, "
               "tablets and computers."]),
             ("If something doesn’t work for you",
              ["If you find anything hard to use, or would rather not use the online "
               "form, email us at " + SITE["email"] + " with whatever details you "
               "have, and we will take it from there. Tell us what went wrong and we "
               "will fix it."]),
             ("Last reviewed",
              ["13 October 2026."]),
         ]},
    ],
},

# ------------------------------------------------------------- thank you ---
{
    "cale": "thank-you/",
    "titlu_tab": "Thank you | F.A.M.s Mobile Catering",
    "descriere": "Your enquiry has reached F.A.M.s Mobile Catering.",
    "indexare": False,
    "blocuri": [
        {"tip": "titlu_pagina",
         "eticheta": "Enquiry sent",
         "titlu": "That’s with us.",
         "lede": "Thank you — we have your enquiry and we’ll come back to you as soon "
                 "as we can. If anything changes in the meantime, email "
                 "fams.company2021@gmail.com."},

        {"tip": "final",
         "titlu": "While you wait.",
         "text": "The questions people usually ask next are answered here.",
         "actiune": ("faq/", "Read the FAQ")},
    ],
},

]

# Pagina 404 e separata: nu apare in sitemap si are caile absolute.
PAGINA_404 = {
    "cale": "404.html",
    "titlu_tab": "Page not found | F.A.M.s Mobile Catering",
    "descriere": "That page does not exist.",
    "indexare": False,
    "blocuri": [
        {"tip": "titlu_pagina",
         "eticheta": "404",
         "titlu": "That page<br>isn’t here.",
         "lede": "It may have moved, or the link may be wrong. The pages below are "
                 "all still where they should be."},
        {"tip": "final",
         "titlu": "Back to<br>the beginning.",
         "text": "Or go straight to the enquiry form if that is what you came for.",
         "actiune": ("contact/", "Start an enquiry")},
    ],
}

# ------------------------------------------------------------- formularul --
# Campurile formularului de cerere de oferta. (nume, eticheta, tip, obligatoriu, optiuni)
# Etichetele sunt si etichetele din mesajul de WhatsApp, deci trebuie sa se
# inteleaga si scoase din formular.
FORMULAR = [
    ("Your details", [
        ("first-name", "First name", "text", True, None),
        ("last-name", "Last name", "text", True, None),
        ("email", "Email", "email", True, None),
        ("phone", "Phone (WhatsApp if you have it)", "tel", True, None),
        ("contact-by", "Best way to reach you", "select", True,
         ["WhatsApp", "Email", "Either"]),
        ("company", "Company", "text", False, None),
    ]),
    ("The event", [
        ("event-type", "Type of event", "select", True,
         ["Wedding breakfast", "Wedding reception", "Wedding anniversary",
          "Birthday party", "Private party", "Christening",
          "Bar or Bat Mitzvah", "Charity event", "Company event",
          "Company trade day", "Construction site", "Film or TV shoot",
          "Public event", "School event", "Student or university event",
          "Race night", "Funeral or wake", "Other"]),
        ("guests", "Number of guests", "number", True, None),
        ("date", "Event date", "date", True, None),
        ("serving-time", "Food served at (24-hour, e.g. 13:00)", "time", True, None),
        ("more-dates", "We need you for more than one date", "checkbox", False, None),
        ("start-time", "Event starts at", "time", False, None),
        ("town", "Town or city", "text", True, None),
        ("postcode", "Event postcode", "text", True, None),
        ("venue", "Venue name or address", "text", False, None),
        ("setting", "Indoors or outdoors?", "select", False,
         ["Indoors", "Outdoors", "Both", "Not sure yet"]),
        ("access", "Where can the van park?", "select", False,
         ["Right by the guests", "A short walk away", "Not sure yet"]),
    ]),
    # Fara preturi si fara meniu fix: totul se face la cerere, deci mancarea
    # se descrie liber, nu se alege dintr-o lista.
    ("The food", [
        ("menu", "What would you like us to cook?", "textarea", True, None),
        ("dietary", "Allergies and dietary requirements", "textarea", False, None),
    ]),
    ("Anything else", [
        ("heard", "How did you hear about us?", "select", False,
         ["Google", "Instagram", "TikTok", "Facebook", "Recommendation",
          "Saw the van", "Other"]),
        ("notes", "Anything else we should know?", "textarea", False, None),
    ]),
]
