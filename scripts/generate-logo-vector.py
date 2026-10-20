#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ube Latte Theme — vector logo candidates, v2 (SVG rendered by headless Chromium).

v2 focuses on artwork quality rather than new concepts: every mark now carries a
gradient fill, a soft drop shadow, highlight streaks and a consistent 24–232
safe box, so it reads like a designed icon instead of flat clip-art.

Playwright screenshots each SVG cell with omit_background=True (true
transparency); PIL only composes the contact sheets, the inline strip and the
official logo/logo.png exported from SELECTED.

Colours come from manifest.json. Change SELECTED and re-run; never hand-copy PNGs.
"""
import json
import math
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))                      # relative paths only (non-ASCII path safety)

SIZE = 128
CELL = 512
PREVIEW = 256
SELECTED = "02"
CAND_DIR = Path("logo/candidates")
LOGO_OUT = Path("logo/logo.png")

with open("manifest.json", "r", encoding="utf-8") as f:
    _m = json.load(f)
_C, _P = _m["theme"]["colors"], _m["theme"]["properties"]


def hx(vals):
    return "#%02X%02X%02X" % tuple(vals)


LILAC = hx(_C["frame"])                            # #B3A8E8
PINK = hx(_C["toolbar"])                           # #F2C9E0
CREAM = hx(_C["ntp_background"])                   # #F6EBF0
PINK_DEEP = hx(_C["button_background_secondary"])  # #E68BC8
MAUVE = hx(_C["ntp_link"])                         # #7B4C93
INK = hx(_C["ntp_text"])                           # #3A2A45

SHADOW = """
  <filter id="ds" x="-35%%" y="-35%%" width="170%%" height="170%%">
    <feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="%s" flood-opacity=".20"/>
  </filter>""" % INK


def svg_open(body, defs=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 256 256">%s%s</svg>' % (CELL, CELL, defs, body))


def spiral_path(cx, cy, r0, r1, turns, steps=300):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        th = 2 * math.pi * turns * t
        r = r0 + (r1 - r0) * t
        pts.append("%.2f %.2f" % (cx + r * math.cos(th), cy - r * math.sin(th)))
    return "M" + " L".join(pts)


# ------------------------------------------------------------------ candidates
SVG_01 = svg_open("""
<defs>
  <radialGradient id="lq1" cx="38%%" cy="30%%" r="78%%">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </radialGradient>
  %s
</defs>
<circle cx="128" cy="128" r="96" fill="%s" filter="url(#ds)"/>
<circle cx="128" cy="128" r="82" fill="%s"/>
<circle cx="128" cy="128" r="71" fill="url(#lq1)"/>
<path d="M128 72 C164 98 164 156 128 190 C92 156 92 98 128 72 Z" fill="%s" fill-opacity=".96"/>
<path d="M128 84 V178" stroke="%s" stroke-opacity=".55" stroke-width="4" stroke-linecap="round"/>
<g stroke="%s" stroke-opacity=".45" stroke-width="3.4" stroke-linecap="round" fill="none">
  <path d="M128 104 C118 110 112 118 110 126"/>
  <path d="M128 104 C138 110 144 118 146 126"/>
  <path d="M128 128 C116 134 110 142 108 150"/>
  <path d="M128 128 C140 134 146 142 148 150"/>
  <path d="M128 152 C120 156 116 162 114 168"/>
  <path d="M128 152 C136 156 140 162 142 168"/>
</g>
<ellipse cx="108" cy="96" rx="16" ry="9" fill="#FFFFFF" opacity=".35" transform="rotate(-28 108 96)"/>
""" % (LILAC, MAUVE, SHADOW, PINK_DEEP, CREAM, CREAM, MAUVE, MAUVE))

SVG_02 = svg_open("""
<defs>
  <linearGradient id="gl2" x1="0" y1="0" x2="0.4" y2="1">
    <stop offset="0" stop-color="#FFFFFF"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  <linearGradient id="ub2" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<ellipse cx="128" cy="216" rx="62" ry="12" fill="%s" opacity=".16"/>
<path d="M82 64 h96 l-10 140 q-1 14 -16 14 h-44 q-15 0 -16 -14 z" fill="url(#gl2)" filter="url(#ds)"/>
<g clip-path="none">
  <path d="M88 104 h88 l-7 98 q-1 12 -14 12 h-46 q-13 0 -14 -12 z" fill="url(#ub2)"/>
  <path d="M88 104 h88 l-2 26 h-84 z" fill="%s" fill-opacity=".55"/>
</g>
<path d="M82 64 h96 l-10 140 q-1 14 -16 14 h-44 q-15 0 -16 -14 z" fill="none" stroke="%s"
      stroke-opacity=".55" stroke-width="4"/>
""" % (PINK, MAUVE, LILAC, SHADOW, INK, LILAC, MAUVE))

SVG_03 = svg_open("""
<defs>
  <linearGradient id="sf3" x1="0" y1="0" x2="0.7" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  <linearGradient id="cn3" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="M92 176 L164 176 L128 232 Z" fill="url(#cn3)"/>
<g fill="url(#sf3)" filter="url(#ds)">
  <ellipse cx="128" cy="162" rx="40" ry="23"/>
  <ellipse cx="128" cy="136" rx="33" ry="20"/>
  <ellipse cx="128" cy="112" rx="26" ry="16"/>
  <path d="M128 98 Q114 78 128 58 Q142 78 128 98 Z"/>
</g>
<path d="M96 140 q32 -14 64 0" stroke="#FFFFFF" stroke-opacity=".30" stroke-width="6"
      stroke-linecap="round" fill="none"/>
<path d="M104 118 q24 -10 48 0" stroke="#FFFFFF" stroke-opacity=".22" stroke-width="5"
      stroke-linecap="round" fill="none"/>
""" % (MAUVE, LILAC, PINK_DEEP, PINK, SHADOW))

SVG_04 = svg_open("""
<defs>
  <linearGradient id="tl4" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="0.55" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<rect x="34" y="34" width="188" height="188" rx="54" fill="url(#tl4)" filter="url(#ds)"/>
<path d="%s" fill="none" stroke="%s" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="128" cy="128" r="14" fill="%s"/>
<ellipse cx="92" cy="88" rx="42" ry="26" fill="#FFFFFF" opacity=".14" transform="rotate(-24 92 88)"/>
""" % (LILAC, MAUVE, INK, SHADOW, spiral_path(128, 128, 20, 56, 2.1), CREAM, PINK_DEEP))

SVG_05 = svg_open("""
<defs>
  <linearGradient id="dp5" x1="0.2" y1="0" x2="0.8" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="0.6" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="M128 34 C176 96 202 128 202 158 C202 198 169 226 128 226 C87 226 54 198 54 158
         C54 128 80 96 128 34 Z" fill="url(#dp5)" filter="url(#ds)"/>
<ellipse cx="104" cy="150" rx="20" ry="30" fill="#FFFFFF" opacity=".30" transform="rotate(-18 104 150)"/>
<ellipse cx="150" cy="182" rx="12" ry="8" fill="#FFFFFF" opacity=".18" transform="rotate(20 150 182)"/>
<path d="%s" fill="none" stroke="%s" stroke-opacity=".55" stroke-width="7" stroke-linecap="round"/>
""" % (LILAC, MAUVE, INK, SHADOW, spiral_path(128, 168, 8, 30, 1.5), CREAM))

SVG_06 = svg_open("""
<defs>
  <linearGradient id="sl6" x1="0" y1="0" x2="0.6" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="M40 176 A96 96 0 0 1 216 176 Z" fill="%s" filter="url(#ds)"/>
<path d="M56 176 A80 80 0 0 1 200 176 Z" fill="url(#sl6)"/>
<g fill="%s" opacity=".35">
  <circle cx="104" cy="150" r="7"/>
  <circle cx="128" cy="138" r="7"/>
  <circle cx="152" cy="150" r="7"/>
  <circle cx="118" cy="166" r="6"/>
  <circle cx="140" cy="166" r="6"/>
</g>
<path d="M40 176 H216" stroke="%s" stroke-opacity=".35" stroke-width="7" stroke-linecap="round"/>
""" % (LILAC, MAUVE, SHADOW, INK, MAUVE, INK))

CANDIDATES = [
    ("01", "latte-rosetta", "Top-view latte with leaf art + saucer — most on-name", SVG_01),
    ("02", "ube-glass", "Layered ube latte in a glass with straw — clearest story", SVG_02),
    ("03", "softserve-swirl", "Spiral soft-serve on a cone — playful, bold silhouette", SVG_03),
    ("04", "swirl-tile", "Swirl on a gradient tile — strongest at 32px", SVG_04),
    ("05", "milk-drop", "Glossy drop with a swirl — softest, most abstract", SVG_05),
    ("06", "ube-slice", "Sliced ube cross-section — most literal, earthy", SVG_06),
]


def font(size, bold=False):
    for name in (("segoeuib.ttf", "seguisb.ttf") if bold else ("segoeui.ttf", "segoeuisl.ttf")):
        p = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def render_cells():
    cells = "".join('<div id="cell%s" style="width:%dpx;height:%dpx">%s</div>' % (num, CELL, CELL, svg)
                    for num, _n, _d, svg in CANDIDATES)
    html = ('<!doctype html><html><head><meta charset="utf-8"><style>'
            'html,body{margin:0;padding:0;background:transparent}'
            '#grid{display:flex;flex-wrap:wrap;width:%dpx}div[id^=cell]{display:block}'
            '</style></head><body><div id="grid">%s</div></body></html>' % (CELL * 3, cells))
    out = {}
    with sync_playwright() as p:
        try:
            b = p.chromium.launch()
        except Exception:
            b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": CELL * 3, "height": CELL * 2})
        pg.set_content(html)
        for num, name, _d, _svg in CANDIDATES:
            path = CAND_DIR / ("%s-%s.png" % (num, name))
            pg.locator("#cell" + num).screenshot(path=str(path), omit_background=True)
            img = Image.open(path).convert("RGBA").resize((PREVIEW, PREVIEW), Image.LANCZOS)
            img.save(path)
            bbox = img.split()[3].getbbox()
            assert bbox, "candidate %s rendered empty" % name
            assert bbox[0] > 6 and bbox[1] > 6 and bbox[2] < PREVIEW - 6 and bbox[3] < PREVIEW - 6, \
                "candidate %s touches the canvas edge: %s" % (name, bbox)
            out[num] = img
            print("candidate %s %s -> alpha bbox %s" % (num, name, bbox))
        b.close()
    return out


def contact_sheet(rendered, bg, txt, sub, path, title):
    cols, rows = 3, 2
    cw, ch = 384, 374
    gap, margin = 28, 40
    W = margin * 2 + cols * cw + (cols - 1) * gap
    H = margin * 2 + 34 + rows * ch + (rows - 1) * gap
    sheet = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(sheet)
    f_title, f_name, f_desc, f_file = font(24, True), font(21, True), font(15), font(14)
    d.text((margin, margin), title, font=f_title, fill=txt)
    y0 = margin + 34
    for i, (num, name, desc, _svg) in enumerate(CANDIDATES):
        r, c = divmod(i, cols)
        x = margin + c * (cw + gap)
        y = y0 + r * (ch + gap)
        big = rendered[num].resize((220, 220), Image.LANCZOS)
        sheet.paste(big, (x + (cw - 220) // 2, y + 14), big)
        d.text((x + 18, y + 250), "%s · %s" % (num, name), font=f_name, fill=txt)
        d.text((x + 18, y + 280), desc, font=f_desc, fill=sub)
        thumb = rendered[num].resize((32, 32), Image.LANCZOS)
        sheet.paste(thumb, (x + 18, y + 330), thumb)
        d.text((x + 60, y + 339), "%s.png  256x256" % name, font=f_file, fill=sub)
        assert y + 300 <= y + 322, "text block collides with the thumbnail row"
    sheet.save(path)
    print("saved:", path, sheet.size)


def inline_strip(rendered, path):
    n, cell, gap, margin = len(CANDIDATES), 108, 22, 30
    W = margin * 2 + n * cell + (n - 1) * gap
    H = margin * 2 + cell + 30
    strip = Image.new("RGB", (W, H), (250, 243, 247))
    d = ImageDraw.Draw(strip)
    f = font(15, True)
    for i, (num, _n, _d, _s) in enumerate(CANDIDATES):
        x = margin + i * (cell + gap)
        img = rendered[num].resize((cell, cell), Image.LANCZOS)
        strip.paste(img, (x, margin), img)
        d.text((x + cell // 2 - 8, margin + cell + 8), num, font=f, fill=(58, 42, 69))
    strip.save(path)
    print("saved:", path, strip.size)


def main():
    CAND_DIR.mkdir(parents=True, exist_ok=True)
    rendered = render_cells()
    contact_sheet(rendered, (250, 243, 247), (58, 42, 69), (140, 110, 130),
                  CAND_DIR / "contact-light.png", "Ube Latte — logo candidates v2 (light)")
    contact_sheet(rendered, (48, 34, 58), (246, 235, 240), (186, 162, 186),
                  CAND_DIR / "contact-dark.png", "Ube Latte — logo candidates v2 (dark)")
    inline_strip(rendered, CAND_DIR / "inline-strip.png")
    sel = [c for c in CANDIDATES if c[0] == SELECTED][0]
    icon = rendered[sel[0]].resize((SIZE, SIZE), Image.LANCZOS)
    icon.save(LOGO_OUT)
    print("official icon from SELECTED=%s (%s):" % (sel[0], sel[1]), LOGO_OUT, icon.size)


if __name__ == "__main__":
    main()
