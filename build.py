#!/usr/bin/env python3
"""Generates the static site. Edit the data below, then run:  python3 build.py

Everything is plain HTML + one stylesheet, so GitHub Pages serves it as-is (no build step there).
Pages written:
  /index.html                      app list
  /about/index.html                about + LinkedIn
  /apps/<slug>/index.html          app page (also works as the App Store "Support URL")
  /apps/<slug>/privacy/index.html  privacy policy (App Store "Privacy Policy URL"),
                                   skipped when the app sets "privacy_url" to an external policy
  /404.html
"""
import re
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
HAS_PHOTO = True
POLICY_DATE = "November 20, 2026"

APPS = [
    {
        "slug": "tacklerow",
        "name": "Tacklerow",
        "subtitle": "Handmade fishing lures from US makers",
        "accent": "#7FA7C9",
        "store": "https://apps.apple.com/us/app/tacklerow/id6773102741",
        "website": "https://tacklerow.com",
        "contact_email": "support@tacklerow.com",
        "privacy_url": "https://tacklerow.com/privacy",  # uses its own policy; no page generated here
        "shots": 6,
        "summary": "A US marketplace for handmade fishing tackle. Every bait is hand-poured, painted, tied, or "
                   "built by a real maker, and you buy it straight from them.",
        "features": [
            ("Baits for your fish", "Every listing is tagged by species. Browse and search soft plastics, "
                                    "crankbaits, jigs, spinnerbaits, and flies."),
            ("Meet the maker", "Real photos of every bait, the person who made it, and their full shop. "
                               "Message a maker about colors, sizes, or a custom order."),
            ("Buy with confidence", "Secure checkout through Stripe, with tracking from paid to shipped to "
                                    "delivered. Fill one cart from several makers."),
            ("Sell your baits", "Open a storefront, list your baits, ship with tracking, and get paid to your "
                                "bank through secure payouts."),
        ],
    },
    {
        "slug": "topside",
        "name": "Topside",
        "subtitle": "ARC Raiders map conditions & alerts",
        "accent": "#F1AA1C",
        "store": "https://apps.apple.com/us/app/arc-raiders-topside/id6836196364",
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
        "policy_date": "November 27, 2026",
        "subtitle": "Halo Infinite multiplayer stats",
        "accent": "#45AAF2",
        "store": "https://apps.apple.com/us/app/infinite-spartan-stats/id1638806689",
        "shots": 6,
        "summary": "Built for the competitive Halo Infinite player. Sign in with Xbox and get your Spartan, your "
                   "ranks, and every match you've played, live from Halo Waypoint.",
        "features": [
            ("Your Spartan", "Career rank and XP, your last 20 results and streak, and a full service record: "
                             "win rate, K/D, KDA, accuracy, damage, and more."),
            ("Ranked", "Your CSR in every ranked playlist this season, with a trend for your recent ranked "
                       "matches."),
            ("Every mode, every stat", "Your totals in Capture the Flag, Oddball, Zones, Elimination, "
                                       "Extraction, and more."),
            ("Match history", "Every match with map, mode, K/D/A, and CSR won or lost. Filter by matchmade, "
                              "custom, and local games."),
            ("Match detail", "How you did against what Halo expected, your medals and damage, and both teams' "
                             "full scoreboards with every player's rank."),
            ("Loadout", "Your equipped armor on one gear sheet, from helmet and visor to coating, emblem, and "
                        "effects."),
            ("Medals", "Every medal you've earned, from mythic down, with counts."),
            ("Search any Spartan", "Look up any gamertag or pick from your Xbox friends, and see their record, "
                                   "ranks, loadout, and matches."),
        ],
        "note": "Infinite Spartan Stats is an unofficial app and is not affiliated with, endorsed by, or "
                "sponsored by Microsoft, Xbox, or 343 Industries / Halo Studios. Halo is a trademark of "
                "Microsoft Corporation.",
        "privacy": [
            ("The short version", [
                "Infinite Spartan Stats has no servers of its own, and it contains no analytics, ads, or "
                "tracking. Nothing about you is collected or stored off your device.",
            ]),
            ("Signing in with Xbox", [
                "You sign in through Microsoft's own sign-in page. The app never sees your password. "
                "Microsoft returns sign-in tokens, which are stored in your device's keychain and used only to "
                "request Halo Infinite and Xbox data from Microsoft, Xbox Live, and Halo Waypoint services.",
                "Your use of those services is covered by the Microsoft Privacy Statement.",
            ]),
            ("Stats and Xbox friends", [
                "Stats, matches, ranks, and loadouts are requested directly from Halo Waypoint. Nothing goes "
                "through any other server.",
                "When you search, the app asks Xbox Live for matching gamertags and for your Xbox friends list, "
                "so you can pick a friend to look up. The friends list is only shown in the app; it isn't "
                "saved or sent anywhere else. Gamertags and Halo stats are public game information.",
            ]),
            ("Data stored on your device", [
                "Your sign-in, the Spartans you've recently looked up, and saved matches, maps, and pictures "
                "are kept on your device so the app opens quickly. Clear Saved Data in the app's settings "
                "removes the saved matches and pictures, signing out removes your sign-in, and deleting the "
                "app removes everything.",
            ]),
        ],
    },
    {
        "slug": "beach-time",
        "name": "Beach Time",
        "policy_date": "November 23, 2026",
        "subtitle": "Tides for your next beach day",
        "accent": "#FF8A6B",
        "store": "https://apps.apple.com/us/app/beach-time/id1469329051",
        "shots": 6,
        "summary": "Know the tide before you go. Live tides, the week ahead, and sunrise to sunset for every "
                   "NOAA tide station in the U.S.",
        "features": [
            ("Your beaches, at a glance", "Favorite and nearby beaches, each with its live tide."),
            ("Know when the tide turns", "Live height, rising or falling, and the whole day's tide curve."),
            ("Plan the perfect beach day", "The week ahead, sunrise and sunset, and the best low tide for "
                                           "tide pools."),
            ("Every NOAA tide station", "Browse by state, or search by beach name, city, or ZIP code."),
            ("Favorites", "A one-time unlock to keep your beaches close, shared with Family Sharing."),
            ("Morning tide reports", "Wake up to a notification with each favorite beach's highs and lows."),
        ],
        "privacy": [
            ("The short version", [
                "Beach Time doesn't have accounts, and it contains no analytics, ads, or tracking. Nothing "
                "about you is collected or stored off your device.",
            ]),
            ("Tide data", [
                "Tide predictions are downloaded directly from NOAA's public tide service. The app only asks "
                "for the tide station you're viewing; nothing about you is sent. Like any website, NOAA's "
                "servers can see your IP address.",
            ]),
            ("Location", [
                "If you allow it, your location is used to find the tide stations closest to you. The list of "
                "stations is built into the app, so that match happens entirely on your device and your "
                "location is never sent anywhere. You can turn location off at any time in Settings.",
            ]),
            ("Search and maps", [
                "When you search by city or ZIP code, that search text is sent to Apple's MapKit service to "
                "find the place, and station maps are shown with Apple Maps. Both are covered by Apple's "
                "privacy policy.",
            ]),
            ("Tide reports", [
                "Morning tide reports are local notifications scheduled on your device. The app refreshes tide "
                "data in the background so each report is current. No push notification service or server is "
                "involved, and no device token is collected.",
            ]),
            ("Purchases", [
                "The Favorites unlock is handled entirely by Apple. We never receive your payment "
                "information.",
            ]),
            ("Data stored on your device", [
                "Your favorite beaches, tide report settings, and a cache of recent tide data are saved on "
                "your device. Deleting the app removes them.",
            ]),
        ],
    },
    {
        "slug": "getup",
        "name": "GetUp Jump Higher",
        "policy_date": "November 23, 2026",
        "subtitle": "Plyometrics for a higher vertical",
        "accent": "#3478F6",
        "store": "https://apps.apple.com/us/app/getup-jump-higher/id895973682",
        "shots": 6,
        "summary": "Jump higher in 13 weeks. The GetUp plyometric program builds your endurance first, then your "
                   "power, with every workout planned for you and a video for every exercise.",
        "features": [
            ("Build the base, then the power", "An 8-week Endurance phase, then a 5-week Power phase."),
            ("Every workout, on schedule", "Two workouts a week, every third day, dated for you and added to "
                                           "your calendar if you like."),
            ("Check off every rep", "Sets, reps and rest for each exercise, plus added weight and your "
                                    "vertical."),
            ("Learn the right form", "A video for all seven exercises, with the coaching cue for each."),
            ("See how high you've gone", "Every phase you finish, with your best vertical jump."),
            ("Unlock the full program", "The first three workouts of each phase are free. A one-time purchase "
                                        "unlocks the rest, every exercise video, and the calendar."),
        ],
        "privacy": [
            ("The short version", [
                "GetUp Jump Higher doesn't have accounts, and it contains no analytics, ads, or tracking. "
                "Nothing about you is collected or stored off your device.",
            ]),
            ("Exercise videos", [
                "The form videos are hosted by Apple with the app and downloaded from Apple's servers the first "
                "time you play each one. Nothing about you is sent with that download, and Apple handles it "
                "under its own privacy policy.",
            ]),
            ("Calendar", [
                "If you choose to add workouts to your calendar, the app asks for calendar access and creates "
                "its own GetUp Jump Higher calendar with your workout dates. It doesn't read or upload your "
                "other events, and you can delete that calendar from the app's settings at any time.",
            ]),
            ("Purchases", [
                "The unlock is handled entirely by Apple. We never receive your payment information.",
            ]),
            ("Data stored on your device", [
                "Your phases, workout progress, weights, verticals, and notes are saved on your device, along "
                "with any videos you've downloaded. Deleting the app removes them.",
            ]),
        ],
    },
]

# ---------------------------------------------------------------------------------------------

def contact_html(app=None) -> str:
    email = (app or {}).get("contact_email") or CONTACT_EMAIL
    if email:
        return f'at <a href="mailto:{escape(email)}">{escape(email)}</a>'
    return f'on <a href="{LINKEDIN}">LinkedIn</a>'


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
<link rel="icon" type="image/png" href="{up}assets/img/favicon.png">
<link rel="apple-touch-icon" href="{up}assets/img/apple-touch-icon.png">
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


def privacy_href(app: dict, prefix: str) -> str:
    """External policy if the app has one, otherwise the generated page under prefix."""
    return app.get("privacy_url") or f"{prefix}privacy/index.html"


def store_button(app: dict, depth: int) -> str:
    if app.get("store"):
        return f'<a class="button" href="{app["store"]}">View on the App Store</a>'
    return f'<span class="button disabled">{escape(app.get("status", "Coming soon"))}</span>'


# External links (http/https) open in a new tab; internal and mailto links don't.
EXTERNAL_LINK = re.compile(r'<a ((?:(?!>)[^>])*?href="https?://[^"]*")')


def write(path: str, html: str):
    html = EXTERNAL_LINK.sub(r'<a \1 target="_blank" rel="noopener"', html)
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
      <p class="links"><a href="apps/{a['slug']}/index.html">Details</a> · <a href="{privacy_href(a, f"apps/{a['slug']}/")}">Privacy</a>{' · <a href="' + a['store'] + '">App Store</a>' if a.get('store') else ' · <span class="muted">' + escape(a.get('status', 'Coming soon')) + '</span>'}</p>
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
    website = (f'<a href="{a["website"]}">{escape(a["website"].split("//")[-1])}</a> · '
               if a.get("website") else "")
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
  <p>Questions, bugs, or ideas? Reach me {contact_html(a)}. Include your device and iOS version if something's broken.</p>
  <p>{website}<a href="{privacy_href(a, "")}">Privacy policy</a></p>
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
  <p class="muted">Last updated {a.get('policy_date', POLICY_DATE)}</p>
  {sections}
  <h2>Children</h2>
  <p>The app doesn't knowingly collect any information from anyone, including children under 13.</p>
  <h2>Changes</h2>
  <p>If this policy changes, the updated version will be posted on this page with a new date.</p>
  <h2>Contact</h2>
  <p>Questions about this policy? Reach me {contact_html(a)}.</p>
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
        if not app.get("privacy_url"):
            build_privacy(app)
    build_about()
    build_404()
