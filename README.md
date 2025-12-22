# Matcha-Whisk-Dash (Mini-Spiel zum Gutschein)

Dieses Paket ist ein **kleines Mobile-Webspiel (HTML5)**. Nach dem Ziel (15 Punkte in 30 Sekunden) wird der Gutschein angezeigt.
Nach **3 Fehlversuchen** wird automatisch freigeschaltet (damit niemand Weihnachten frustriert endet 😄).

## 1) Schnell online stellen (ohne Programmieren)

### Option A: GitHub Pages (gratis)
1. Erstelle ein neues Repository (z.B. `matcha-theresa`).
2. Lade `index.html` hoch (im Repo-Root).
3. In GitHub: **Settings → Pages** → Source: `Deploy from a branch` → Branch: `main` / `/root`.
4. Du bekommst eine URL wie `https://DEINNAME.github.io/matcha-theresa/`

### Option B: Netlify Drop (gratis, super schnell)
1. Gehe zu Netlify Drop (Drag & Drop).
2. Zieh den ganzen Ordner rein.
3. Du bekommst sofort eine URL (kannst du auch customizen).

## 2) QR-Link mit Name
Häng an die URL einfach `?name=Theresa` an, z.B.:
`https://.../matcha-theresa/?name=Theresa`

## 3) QR-Code erstellen
- Am einfachsten: Online QR-Generator nutzen und die URL reinkopieren.
- Oder: den beiliegenden PDF-Gutschein/Weihnachtsbillet neu erzeugen (siehe `make_card.py`), sobald du die finale URL hast.

## Dateien
- `index.html` – das Spiel (enthält den Gutschein bereits eingebettet)
- `weihnachtsbillet_qr_placeholder.pdf` – Druckvorlage mit QR (Platzhalter-URL)
- `qr_placeholder.png` – QR als PNG (Platzhalter-URL)

