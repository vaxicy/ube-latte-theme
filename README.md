<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/ube-latte-theme/main/logo/logo.png" width="128" alt="Ube Latte Theme logo">
</p>

<h1 align="center">Ube Latte Theme</h1>

<p align="center">
  A creamy lavender-purple Chrome theme inspired by ube latte — soft lilac chrome over a milky pink page.
</p>

Ube Latte pairs a soft lilac frame with a blush-pink toolbar, then opens onto a milky New Tab Page with a plum Google logo that matches the palette. Deep plum ink keeps every tab, bookmark and toolbar icon crisp on the light chrome, links take a deeper ube purple, and a single-row shortcut layout keeps the New Tab Page clean.

<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/ube-latte-theme/main/store-assets/promo/1400x560.png" alt="Ube Latte Theme promo" width="700">
</p>

## Design Concept

Ube Latte comes from a lavender-to-pink palette: a soft lilac, a whisper-pink base, a blush toolbar and two deeper purples for links and accents. This is the lightest theme in the set — the chrome stays pale and milky like a latte, and contrast comes from deep plum ink rather than from a dark frame. Everything is low-saturation so the purple never feels loud.

| Color | Hex | RGB | Role |
|---|---|---|---|
| Milk | `#F6EBF0` | 246, 235, 240 | New Tab background |
| Blush | `#F2C9E0` | 242, 201, 224 | Toolbar / New Tab header / buttons |
| Pink | `#E68BC8` | 230, 139, 200 | Secondary buttons / accent |
| Lilac | `#B3A8E8` | 179, 168, 232 | Frame |
| Mauve | `#B57FC4` | 181, 127, 196 | Deep accent |
| Plum | `#7B4C93` | 123, 76, 147 | New Tab links |
| Deep Plum Ink | `#3A2A45` | 58, 42, 69 | Tab, bookmark and New Tab text |

## Features

- Pure color, no wallpaper — fast and distraction-free
- Soft lilac-and-blush chrome, milky page — the lightest theme in the set
- Deep plum ink on every surface, so text stays readable without a dark frame
- Tab text, bookmark text and toolbar icons all share the same plum ink
- Single-row shortcut row and a color-matched Google logo for a clean New Tab Page
- No configuration needed — install and enjoy

## Preview

<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/ube-latte-theme/main/store-assets/screenshots/en/screenshot-1-browser.png" alt="Ube Latte New Tab preview" width="640">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/ube-latte-theme/main/store-assets/screenshots/en/screenshot-2-palette.png" alt="Ube Latte palette" width="640">
</p>

## Installation

### Load Unpacked (Development)

1. Download or clone this repository.
2. Open `chrome://extensions` in Chrome.
3. Enable "Developer mode" in the top right.
4. Click "Load unpacked" and select this folder (`ube-latte-theme`).
5. The theme is now active.

### Web Store Packaging

```
chrome://extensions → Pack extension → select this folder → ube-latte-theme.zip
```

Upload the resulting `.zip` to the Chrome Web Store developer dashboard.

## Files

| File | Purpose |
|---|---|
| `manifest.json` | Theme definition (single-file, inlined `theme` field) |
| `logo/logo.png` | 128×128 store icon (transparent background) |
| `store-assets/promo/440x280.png` | Small promo tile |
| `store-assets/promo/1400x560.png` | Marquee promo tile |
| `store-assets/screenshots/en/screenshot-1-browser.png` | Browser mockup screenshot (1280×800) |
| `store-assets/screenshots/en/screenshot-2-palette.png` | Palette introduction screenshot (1280×800) |
| `store-assets/store-description.txt` | Store listing description |
| `scripts/generate-logo-vector.py` | Render all SVG logo candidates with headless Chromium, build the contact sheets, and export `logo/logo.png` from the `SELECTED` candidate |
| `scripts/generate-screenshot-headless.py` | Regenerate the browser mockup via Playwright |
| `scripts/generate-screenshot-2-palette.py` | Regenerate the palette screenshot |
| `scripts/generate-promo.py` | Regenerate both promo tiles |
| `logo/candidates/` | Candidate previews and light/dark contact sheets |
| `LICENSE` | Non-Commercial License (English / 中文) |

## License

Ube Latte Theme is released under the Non-Commercial License. See `LICENSE` for full text (English / 中文).
