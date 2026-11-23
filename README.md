# toddcrown.com

Static site for my iOS apps: app pages (App Store **Support URL**), privacy policies
(App Store **Privacy Policy URL**), and an about page. Plain HTML/CSS, hosted on GitHub Pages.

## Editing

All content lives in `build.py` (app list, descriptions, features, privacy policy text, links).

```sh
python3 build.py      # regenerates the HTML
open index.html       # preview locally
git commit -am "Update site" && git push
```

- Add an app: add an entry to `APPS`, put `icon.png` and `shot-1.jpg`… in `assets/img/apps/<slug>/`.
- Contact email: set `CONTACT_EMAIL` (otherwise pages point to LinkedIn). An app can override it with `contact_email`.
- Privacy page date: `POLICY_DATE`, or set `policy_date` on an app that changed its policy.
- External privacy policy: set `privacy_url` on an app; links point there and no privacy page is generated.
- Photo: add `assets/img/me.jpg` (square) and set `HAS_PHOTO = True`.

## URLs for App Store Connect

| App | Support / Marketing URL | Privacy Policy URL |
|---|---|---|
| Tacklerow | `/apps/tacklerow/` | `https://tacklerow.com/privacy` (external) |
| Topside | `/apps/topside/` | `/apps/topside/privacy/` |
| Infinite Spartan Stats | `/apps/infinite-spartan-stats/` | `/apps/infinite-spartan-stats/privacy/` |
| Beach Time | `/apps/beach-time/` | `/apps/beach-time/privacy/` |
| GetUp Jump Higher | `/apps/getup/` | `/apps/getup/privacy/` |
