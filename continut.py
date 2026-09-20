# -*- coding: utf-8 -*-
"""Tot textul site-ului, intr-un singur loc.

Regula pe care o respecta continutul de aici: nu se inventeaza nimic.
Nu exista telefon, e-mail, adresa, recenzii, numar de evenimente sau ani de
experienta, pentru ca nu le-am primit. Unde lipseste ceva, pagina spune
sincer ca lipseste (vezi galeria) in loc sa umple locul cu vorbe.

Dupa orice modificare aici: python3 construieste.py
"""

SITE = {
    "nume": "F.A.M.s",
    "nume_lung": "F.A.M.s Mobile Catering",
    "domeniu": "",  # se completeaza cu unelte/configureaza.py --domeniu https://...
    "zona": "Surrey",
    "an": 2021,
    "slogan": "Good food. Great people. Lasting memories.",
}

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
         "eticheta": "Mobile catering · Surrey · since 2021",
         "titlu": "Family food,<br>beautifully served.",
         "lede": "F.A.M.s is Florin, Alexandra, Mirela and Sofia. We cook fresh, we "
                 "bring the kitchen with us, and we cater weddings, parties and "
                 "events across Surrey.",
         "actiuni": [("contact/", "Start an enquiry", "plin"),
                     ("#catering", "What we cater", "text")],
         "foto": "unghi",
         "legenda": "The van, parked up between jobs"},

        {"tip": "banda",
         "text": ["Family-run", "Est. 2021", "Cooked fresh on the day", "Surrey & beyond"]},

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
         "subsol": "F.A.M.s · Creating Memories"},

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
    "titlu_tab": "About F.A.M.s | The Family Behind the Van",
    "descriere": "F.A.M.s is Florin, Alexandra, Mirela and Sofia — a family-run "
                 "mobile catering business working across Surrey since 2021.",
    "blocuri": [
        {"tip": "deschidere",
         "eticheta": "About",
         "titlu": "Four names on<br>the side of a van.",
         "lede": "F.A.M.s is Florin, Alexandra, Mirela and Sofia. The initials came "
                 "first. The van came in 2021.",
         "actiuni": [("contact/", "Start an enquiry", "plin")],
         "foto": "lateral",
         "legenda": "F.A.M.s · 2021"},

        {"tip": "proza",
         "eticheta": "Who you’re dealing with",
         "titlu": "A family that cooks,<br>for other people’s occasions.",
         "paragrafe": [
             "We cater across Surrey and, by arrangement, further out. Food is "
             "prepared fresh for the event, and the person you speak to when you "
             "enquire is one of the people who turns up on the day.",
             "There is no office, no account manager and no fixed package. You tell "
             "us about the occasion; we tell you what we would do with it, and what "
             "it would cost.",
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
         "subsol": "F.A.M.s · Creating Memories"},

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
         "legenda": "Mobile Catering · Creating Memories"},

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
              "Tell us when you enquire, in full. If there is an allergy involved we "
              "will be specific with you about what we can safely offer, and about "
              "anything we cannot."),
             ("How far ahead should we book?",
              "As early as you can, especially for summer weekends. If your event is "
              "soon, ask anyway — sometimes a date is free."),
             ("How do we get a price?",
              "Use the enquiry form with your date, location, guest numbers and what "
              "you have in mind. That is enough for us to come back with something "
              "useful rather than a vague range."),
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
         "lede": "The more you put in, the more useful our reply will be. Nothing "
                 "here is a commitment."},

        {"tip": "formular"},
    ],
},

# --------------------------------------------------------------- privacy ---
{
    "cale": "privacy/",
    "titlu_tab": "Privacy | F.A.M.s Mobile Catering",
    "descriere": "How the details you send through the F.A.M.s enquiry form are used.",
    "indexare": False,
    "blocuri": [
        {"tip": "titlu_pagina",
         "eticheta": "Privacy",
         "titlu": "What happens to<br>what you send us.",
         "lede": "Short version: we use it to answer your enquiry, and nothing else."},

        {"tip": "text_lung",
         "sectiuni": [
             ("What you give us",
              ["When you submit the enquiry form you may give us your name, contact "
               "details, event date, location, guest numbers, dietary information and "
               "anything else you choose to add."]),
             ("What we use it for",
              ["To reply to you, discuss the event, prepare a quote, and talk about "
               "catering you have asked us to consider. Nothing else. We do not sell "
               "it and we do not send marketing to it."]),
             ("Allergy and dietary details",
              ["Please give us only what is relevant to planning the catering. Where "
               "you tell us about an allergy, we use that to discuss what we can "
               "safely offer you."]),
             ("Where the form goes",
              ["The enquiry form is handled by the site’s hosting provider and "
               "delivered to us. Before launch, the final provider and how long "
               "enquiries are kept should be written here."]),
             ("Your choices",
              ["You can ask what you have sent us, and ask for it to be corrected or "
               "deleted. A direct contact address for privacy requests should be "
               "added to this page before launch."]),
             ("Changes",
              ["This page should be reviewed whenever the contact form, hosting or "
               "any analytics on the site change."]),
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
                 "as we can. If anything changes in the meantime, send it through again."},

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
FORMULAR = [
    ("Your details", [
        ("first-name", "First name", "text", True, None),
        ("last-name", "Last name", "text", True, None),
        ("email", "Email", "email", True, None),
        ("phone", "Phone", "tel", True, None),
        ("company", "Company", "text", False, None),
        ("postcode", "Event postcode", "text", True, None),
    ]),
    ("The event", [
        ("event-type", "Type of event", "select", True,
         ["Wedding", "Private party", "Corporate", "Birthday", "Anniversary", "Other"]),
        ("guests", "Number of guests", "number", True, None),
        ("date", "Event date", "date", True, None),
        ("serving-time", "Preferred serving time", "time", True, None),
        ("venue", "Venue or location", "text", True, None),
        ("dietary", "Allergies and dietary requirements", "textarea", False, None),
    ]),
    ("Anything else", [
        ("heard", "How did you hear about us?", "select", False,
         ["Google", "Instagram", "TikTok", "Facebook", "Recommendation",
          "Saw the van", "Other"]),
        ("notes", "What do you have in mind?", "textarea", False, None),
    ]),
]
