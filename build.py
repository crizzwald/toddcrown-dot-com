#!/usr/bin/env python3
"""Generates the static site. Edit the data below, then run:  python3 build.py

Everything is plain HTML + one stylesheet, so GitHub Pages serves it as-is (no build step there).
Pages written:
  /index.html                      app list
  /about/index.html                about + LinkedIn
  /apps/<slug>/index.html          app page (also works as the App Store "Support URL")
  /apps/<slug>/privacy/index.html  privacy policy (App Store "Privacy Policy URL")
  /404.html
"""
from datetime import date
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent

SITE_NAME = "Todd Crown"
TAGLINE = "Small, focused apps for iPhone."
LINKEDIN = "https://www.linkedin.com/in/toddcrown/"
GITHUB = "https://github.com/crizzwald"
# Shown on every app/support/privacy page. Leave empty to point people at LinkedIn instead.
CONTACT_EMAIL = ""
# Optional: drop a square photo at assets/img/me.jpg and set this to True.
HAS_PHOTO = False
POLICY_DATE = "November 20, 2026"

APPS = [
    {
        "slug": "topside",
        "name": "Topside",
        "subtitle": "ARC Raiders map conditions & alerts",
        "accent": "#F1AA1C",
        "store": "",  # fill in once the App Store listing is live
        "status": "Coming soon",
        "shots": 4,
        "summary": "Know what's live before you drop. Live map conditions for every region, countdowns to "
                   "what's next, and alerts the moment Night Raid hits.",
        "features": [
            ("Live now", "Every active condition with a countdown to when it ends and which maps it's on."),
            ("Coming up", "The next occurrence of every condition, with one-tap alerts."),
            ("Watch", "Follow a condition or a whole map and get notified before every occurrence."),
            ("Regions", "Europe, North America, South America, Asia, and Oceania schedules."),
            ("Widgets", "Home Screen and Lock Screen widgets, each with its own region."),
        ],
        "note": "Topside is an unofficial fan-made companion app and is not affiliated with, endorsed by, or "
                "sponsored by Embark Studios. ARC Raiders is a trademark of Embark Studios AB.",
        "privacy": [
            ("The short version", [
                "Topside doesn't collect, store, or share any personal information. There are no accounts, "
                "no analytics, no ads, and no tracking.",
            ]),
            ("Map condition data", [
                "To show the schedule, the app downloads the publicly available map conditions page from "
                "arcraiders.com. That request is made directly from your device, the same as visiting the "
                "website in a browser. Like any website, that server can see your IP address; Topside sends "
                "nothing else.",
            ]),
            ("Notifications", [
                "Alerts are local notifications scheduled on your device. No push notification service or "
                "server is involved, and no device token is collected.",
            ]),
            ("Data stored on your device", [
                "Your region, alert settings, and watched conditions and maps are saved on your device only. "
                "A copy of the latest schedule is cached so the app and widgets load quickly. Deleting the "
                "app removes all of it.",
            ]),
        ],
    },
    {
        "slug": "infinite-spartan-stats",
        "name": "Infinite Spartan Stats",
        "subtitle": "Halo Infinite multiplayer stats",
        "accent": "#4FC3F7",
        "store": "https://apps.apple.com/us/app/infinite-spartan-stats/id1638806689",
        "shots": 4,
        "summary": "Track your Halo Infinite multiplayer stats: rank and CSR by playlist, kill/death ratio, "
                   "medals, custom games, and match history. Search for other Spartans and see theirs too.",
        "features": [
            ("Your stats", "CSR by playlist, core stats, K/D, and medals earned."),
            ("Match history", "Recent matchmaking and custom games."),
            ("Search Spartans", "Look up any gamertag and view their stats and matches."),
        ],
        "note": "Infinite Spartan Stats is an unofficial app and is not affiliated with, endorsed by, or "
                "sponsored by Microsoft, Xbox, or 343 Industries / Halo Studios. Halo is a trademark of "
                "Microsoft Corporation.",
        "privacy": [
            ("The short version", [
                "Infinite Spartan Stats has no servers of its own that store your data, and it contains no "
                "analytics, ads, or tracking.",
            ]),
            ("Signing in with Xbox", [
                "You sign in through Microsoft's own sign-in page. The app never sees your password. "
                "Microsoft returns access tokens, which are stored on your device and used only to request "
                "your Halo Infinite data from Microsoft, Xbox Live, and Halo Waypoint services.",
                "Your use of those services is covered by the Microsoft Privacy Statement.",
            ]),
            ("Stats and clips", [
                "Stats are requested directly from Halo Waypoint services. To show game clips, the gamertag "
                "you're viewing is sent to a small proxy that retrieves them from a third-party Halo stats "
                "service (HaloDotAPI). Gamertags and stats are public game information.",
            ]),
            ("Data stored on your device", [
                "Sign-in tokens and your recent searches are stored on your device. Signing out, turning on the "
                "reset option in the app's section of the iOS Settings app, or deleting the app removes them.",
            ]),
        ],
    },
    {
        "slug": "beach-time",
        "name": "Beach Time",
        "subtitle": "Tides for your next beach day",
        "accent": "#5ED6C8",
        "store": "https://apps.apple.com/us/app/beach-time/id1469329051",
        "shots": 3,
        "summary": "The exact tide information you need to make the most of your time on the beach. Low tide "
                   "means more beach, fewer crowds, and a better day.",
        "features": [
            ("Nearby stations", "Find tide stations near you as soon as you arrive."),
            ("Favorites", "Save the beaches you visit and see their latest tides at a glance."),
            ("Simple search", "Slide to a location and browse nearby stations."),
        ],
        "privacy": [
            ("The short version", [
                "Beach Time doesn't have accounts, and it contains no analytics, ads, or tracking.",
            ]),
            ("Location", [
                "If you allow it, your approximate location is used to find nearby tide stations. The "
                "coordinates are sent to the tide data service only to look up stations and are not tied to "
                "you or stored by the app. You can turn location off at any time in Settings.",
            ]),
            ("Purchases", [
                "Optional in-app purchases are handled entirely by Apple. We never receive your payment "
                "information.",
            ]),
            ("Data stored on your device", [
                "Your favorite stations are saved on your device. Deleting the app removes them.",
            ]),
        ],
    },
    {
        "slug": "getup",
        "name": "GetUp Jump Higher",
        "subtitle": "Plyometrics for a higher vertical",
        "accent": "#FF7043",
        "store": "https://apps.apple.com/us/app/getup-jump-higher/id895973682",
        "shots": 4,
        "summary": "A plyometric program to build your vertical jump. Seven exercises build endurance first, "
                   "then power, with videos for form and a schedule that keeps you on track.",
        "features": [
            ("Workout log", "Easily log progress through the program."),
            ("Schedule", "Workout dates are calculated for you, and can be added to your calendar."),
            ("Form videos", "Watch every exercise done correctly."),
        ],
        "privacy": [
            ("The short version", [
                "GetUp Jump Higher doesn't collect, store, or share any personal information. There are no "
                "accounts, analytics, ads, or tracking.",
            ]),
            ("Calendar", [
                "If you choose to add workouts to your calendar, the app asks for calendar access and only "
                "creates those workout events. It does not read or upload your calendar.",
            ]),
            ("Data stored on your device", [
                "Your workout progress is saved on your device. Deleting the app removes it.",
            ]),
        ],
    },
]

# ---------------------------------------------------------------------------------------------

def contact_html() -> str:
    if CONTACT_EMAIL:
        return f'<a href="mailto:{escape(CONTACT_EMAIL)}">{escape(CONTACT_EMAIL)}</a>'
    return f'<a href="{LINKEDIN}">LinkedIn</a>'


def page(title: str, body: str, depth: int, description: str = "", accent: str = "#F1AA1C") -> str:
    up = "../" * depth
    full_title = f"{title} · {SITE_NAME}" if title != SITE_NAME else SITE_NAME
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full_title)}</title>
<meta name="description" content="{escape(description or TAGLINE)}">
<link rel="stylesheet" href="{up}assets/css/site.css">
<link rel="icon" href="{up}assets/img/apps/topside/icon.png">
</head>
<body style="--accent: {accent}">
<header class="top">
  <a class="brand" href="{up}index.html">{SITE_NAME}</a>
  <nav><a href="{up}index.html#apps">Apps</a><a href="{up}about/index.html">About</a></nav>
</header>
<main>
{body}
</main>
<footer class="foot">
  <span>© {date.today().year} {SITE_NAME}</span>
  <span><a href="{LINKEDIN}">LinkedIn</a> · <a href="{GITHUB}">GitHub</a></span>
</footer>
</body>
</html>
"""


def store_button(app: dict, depth: int) -> str:
    if app.get("store"):
        return f'<a class="button" href="{app["store"]}">View on the App Store</a>'
    return f'<span class="button disabled">{escape(app.get("status", "Coming soon"))}</span>'


def write(path: str, html: str):
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", path)


def build_index():
    cards = []
    for a in APPS:
        cards.append(f"""
  <article class="card" style="--accent: {a['accent']}">
    <a class="card-link" href="apps/{a['slug']}/index.html" aria-label="{escape(a['name'])}"></a>
    <img class="icon" src="assets/img/apps/{a['slug']}/icon.png" alt="" width="88" height="88">
    <div>
      <h3>{escape(a['name'])}</h3>
      <p class="sub">{escape(a['subtitle'])}</p>
      <p>{escape(a['summary'])}</p>
      <p class="links"><a href="apps/{a['slug']}/index.html">Details</a> · <a href="apps/{a['slug']}/privacy/index.html">Privacy</a>{' · <a href="' + a['store'] + '">App Store</a>' if a.get('store') else ' · <span class="muted">' + escape(a.get('status', 'Coming soon')) + '</span>'}</p>
    </div>
  </article>""")
    body = f"""
<section class="hero">
  <h1>Apps by {SITE_NAME}.</h1>
  <p class="lead">{TAGLINE} Built natively, without accounts or tracking wherever possible.</p>
</section>
<section id="apps" class="cards">{''.join(cards)}
</section>"""
    write("index.html", page(SITE_NAME, body, 0))


def build_app(a: dict):
    shots = "".join(
        f'<img src="../../assets/img/apps/{a["slug"]}/shot-{i}.jpg" alt="{escape(a["name"])} screenshot {i}" loading="lazy">'
        for i in range(1, a["shots"] + 1))
    feats = "".join(f"<li><strong>{escape(t)}</strong> {escape(d)}</li>" for t, d in a["features"])
    note = f'<p class="fine">{escape(a["note"])}</p>' if a.get("note") else ""
    body = f"""
<section class="app-hero">
  <img class="icon big" src="../../assets/img/apps/{a['slug']}/icon.png" alt="" width="128" height="128">
  <div>
    <h1>{escape(a['name'])}</h1>
    <p class="sub">{escape(a['subtitle'])}</p>
    <p class="lead">{escape(a['summary'])}</p>
    <p>{store_button(a, 2)}</p>
  </div>
</section>
<section class="shots">{shots}</section>
<section class="prose">
  <h2>Features</h2>
  <ul class="features">{feats}</ul>
  <h2 id="support">Support</h2>
  <p>Questions, bugs, or ideas? Reach me on {contact_html()}. Include your device and iOS version if something's broken.</p>
  <p><a href="privacy/index.html">Privacy policy</a></p>
  {note}
</section>"""
    write(f"apps/{a['slug']}/index.html", page(a["name"], body, 2, a["summary"], a["accent"]))


def build_privacy(a: dict):
    sections = "".join(
        f"<h2>{escape(h)}</h2>" + "".join(f"<p>{escape(p)}</p>" for p in paras) for h, paras in a["privacy"])
    body = f"""
<section class="prose policy">
  <p class="crumb"><a href="../index.html">{escape(a['name'])}</a></p>
  <h1>Privacy Policy</h1>
  <p class="muted">Last updated {POLICY_DATE}</p>
  {sections}
  <h2>Children</h2>
  <p>The app doesn't knowingly collect any information from anyone, including children under 13.</p>
  <h2>Changes</h2>
  <p>If this policy changes, the updated version will be posted on this page with a new date.</p>
  <h2>Contact</h2>
  <p>Questions about this policy? Reach me on {contact_html()}.</p>
</section>"""
    write(f"apps/{a['slug']}/privacy/index.html",
          page(f"{a['name']} Privacy Policy", body, 3, f"Privacy policy for {a['name']}.", a["accent"]))


def build_about():
    photo = ('<img class="avatar" src="../assets/img/me.jpg" alt="Todd Crown" width="160" height="160">'
             if HAS_PHOTO else '<div class="avatar initials">TC</div>')
    body = f"""
<section class="about">
  {photo}
  <div class="prose">
    <h1>About</h1>
    <p class="lead">I'm Todd, an iOS engineer who builds small apps for things I actually use, from tide
    tables for the beach to stats and schedules for the games I play.</p>
    <p>Find me on <a href="{LINKEDIN}">LinkedIn</a> or <a href="{GITHUB}">GitHub</a>.</p>
  </div>
</section>"""
    write("about/index.html", page("About", body, 1))


def build_404():
    body = """
<section class="hero">
  <h1>Not found.</h1>
  <p class="lead">That page doesn't exist. <a href="/">Head back to the apps.</a></p>
</section>"""
    write("404.html", page("Not found", body, 0))


if __name__ == "__main__":
    build_index()
    for app in APPS:
        build_app(app)
        build_privacy(app)
    build_about()
    build_404()
