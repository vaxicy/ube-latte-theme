<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/ube-latte-theme/main/logo/logo.png?v=2" width="128" alt="Ube Latte Theme logo">
</p>

<h1 align="center">Ube Latte Theme</h1>

<p align="center">
  A creamy lavender-purple Chrome theme inspired by ube latte — soft lilac chrome over a milky pink page.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/manifest-v3-b39ee8" alt="Manifest V3">
  <img src="https://img.shields.io/badge/version-1.0.0-d8a7bd" alt="Version 1.0.0">
  <img src="https://img.shields.io/badge/chrome-light-b3a8e8" alt="Light chrome">
  <img src="https://img.shields.io/badge/license-non--commercial-7b4c93" alt="Non-commercial license">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/ube-latte-theme/main/store-assets/promo/1400x560.png?v=4" alt="Ube Latte Theme promo" width="700">
</p>

## Overview

Ube Latte pairs a soft lilac frame with a blush-pink toolbar, then opens onto a milky New Tab Page with a plum Google logo that matches the palette. Deep plum ink keeps every tab, bookmark and toolbar icon crisp on the light chrome, links take a deeper ube purple, and a single-row shortcut layout keeps the New Tab Page clean.

This is the lightest theme in the set: nothing is dark, nothing is saturated, and contrast is carried entirely by ink.

## Design Concept

Ube Latte comes from a lavender-to-pink palette: a soft lilac, a whisper-pink base, a blush toolbar and two deeper purples for links and accents. Because the chrome is pale, readability depends on the ink rather than on a dark frame — every text surface uses the same deep plum.

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
- Soft lilac-and-blush chrome with a milky page — the lightest theme in the set
- Deep plum ink on every surface, so text stays readable without a dark frame
- Tab text, bookmark text and toolbar icons all share the same plum ink
- Single-row shortcut row and a color-matched Google logo for a clean New Tab Page
- No configuration needed — install and enjoy

## Screenshots

| Browser | Palette |
|:-:|:-:|
| <img src="https://raw.githubusercontent.com/vaxicy/ube-latte-theme/main/store-assets/screenshots/en/screenshot-1-browser.png" width="420" alt="Ube Latte New Tab"> | <img src="https://raw.githubusercontent.com/vaxicy/ube-latte-theme/main/store-assets/screenshots/en/screenshot-2-palette.png?v=2" width="420" alt="Ube Latte palette"> |

## Installation

### Load unpacked (development)

1. Download or clone this repository.
2. Open `chrome://extensions` in Chrome.
3. Enable **Developer mode** in the top right.
4. Click **Load unpacked** and select this folder (`ube-latte-theme`).
5. The theme is active immediately.

### Package for the Chrome Web Store

```
chrome://extensions → Pack extension → select this folder → ube-latte-theme.zip
```

Upload the resulting `.zip` to the [Chrome Web Store developer dashboard](https://chrome.google.com/webstore/devconsole).

## Store listing copy

Ready to paste into the store listing (also kept in `store-assets/store-description.txt`):

> Ube Latte is a creamy lavender-purple Chrome theme: a soft lilac frame, a blush-pink toolbar, and a milky New Tab Page with a plum Google logo that matches the palette. Deep plum ink keeps every tab, bookmark and toolbar icon readable on the light chrome. Solid colors only, no wallpaper — soft, sweet, and easy on the eyes.

## Project structure

| File | Purpose |
|---|---|
| `manifest.json` | Theme definition (single-file, inlined `theme` field) |
| `logo/logo.png` | 128×128 store icon (transparent background) |
| `store-assets/promo/440x280.png` | Small promo tile |
| `store-assets/promo/1400x560.png` | Marquee promo tile |
| `store-assets/screenshots/en/screenshot-1-browser.png` | Browser mockup screenshot (1280×800) |
| `store-assets/screenshots/en/screenshot-2-palette.png` | Palette introduction screenshot (1280×800) |
| `store-assets/store-description.txt` | Store listing description |
| `scripts/generate-logo-vector.py` | Render all SVG logo candidates with headless Chromium, build contact sheets, export `logo/logo.png` from `SELECTED` |
| `scripts/generate-screenshot-headless.py` | Regenerate the browser mockup via Playwright |
| `scripts/generate-screenshot-2-palette.py` | Regenerate the palette screenshot |
| `scripts/generate-promo.py` | Regenerate both promo tiles |
| `logo/candidates/` | Candidate previews and light/dark contact sheets |
| `LICENSE` | Non-Commercial License (English / 中文) |

## Regenerating assets

Every asset is code-generated, so nothing here is hand-drawn or hand-copied:

```bash
py -3 scripts/generate-logo-vector.py        # candidates + contact sheets + logo/logo.png
py -3 scripts/generate-screenshot-headless.py # store screenshot 1 (browser mockup)
py -3 scripts/generate-screenshot-2-palette.py # store screenshot 2 (palette)
py -3 scripts/generate-promo.py              # promo 440x280 + 1400x560
```

To ship a different icon candidate, change `SELECTED` at the top of `generate-logo-vector.py` and re-run, then re-run the three asset scripts so the promo and screenshots pick up the new logo.

## License

Ube Latte Theme is released under the Non-Commercial License. See `LICENSE` for full text (English / 中文).
