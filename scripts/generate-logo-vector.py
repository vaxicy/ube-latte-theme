#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ube Latte Theme — vector logo candidates (SVG rendered by headless Chromium).

Each candidate is inline SVG in its own 512px cell; Playwright screenshots every
cell with omit_background=True (true transparency) and PIL only composes the
contact sheets, the inline strip and the official logo/logo.png exported from
the SELECTED candidate.

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
SELECTED = "01"
CAND_DIR = Path("logo/candidates")
LOGO_OUT = Path("logo/logo.png")

with open("manifest.json", "r", encoding="utf-8") as f:
    _m = json.load(f)
_C, _P = _m["theme"]["colors"], _m["theme"]["properties"]


def hx(vals):
    return "#%02X%02X%02X" % tuple(vals)


LILAC = hx(_C["frame"])                   # #B3A8E8
PINK = hx(_C["toolbar"])                  # #F2C9E0
CREAM = hx(_C["ntp_background"])          # #F6EBF0
PINK_DEEP = hx(_C["button_background_secondary"])  # #E68BC8
MAUVE = hx(_C["ntp_link"])                # #7B4C93
INK = hx(_C["ntp_text"])                  # #3A2A45


def svg_open(body, defs=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 256 256">%s%s</svg>' % (CELL, CELL, defs, body))


def spiral_path(cx, cy, r0, r1, turns, steps=280):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        th = 2 * math.pi * turns * t
        r = r0 + (r1 - r0) * t
        pts.append("%.2f %.2f" % (cx + r * math.cos(th), cy - r * math.sin(th)))
    return "M" + " L".join(pts)


# ------------------------------------------------------------------ candidates
SVG_01 = svg_open("""
<circle cx="128" cy="128" r="99" fill="%s"/>
<circle cx="128" cy="128" r="83" fill="%s"/>
<circle cx="128" cy="128" r="71" fill="%s"/>
<path d="%s" fill="none" stroke="%s" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="128" cy="128" r="9" fill="%s"/>
""" % (PINK_DEEP, CREAM, LILAC, spiral_path(128, 128, 22, 62, 2.15), MAUVE, MAUVE))

SVG_02 = svg_open("""
<defs>
  <linearGradient id="ss2" x1="0" y1="0" x2="0.6" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
</defs>
<path d="M92 188 L164 188 L128 236 Z" fill="%s"/>
<g fill="url(#ss2)">
  <ellipse cx="128" cy="170" rx="40" ry="23"/>
  <ellipse cx="128" cy="144" rx="33" ry="20"/>
  <ellipse cx="128" cy="120" rx="26" ry="16"/>
  <path d="M128 106 Q115 86 128 70 Q141 86 128 106 Z"/>
</g>
<path d="M98 190 L158 190" stroke="%s" stroke-opacity=".45" stroke-width="4" stroke-linecap="round"/>
""" % (MAUVE, LILAC, PINK_DEEP, INK))

SVG_03 = svg_open("""
<g stroke="%s" stroke-width="8" stroke-linecap="round" fill="none" stroke-opacity=".85">
  <path d="M104 106 q-13 -15 0 -28 q13 -13 0 -26"/>
  <path d="M142 102 q-13 -15 0 -28 q13 -13 0 -26"/>
</g>
<path d="M72 130 h112 l-14 68 q-3 12 -16 12 h-52 q-13 0 -16 -12 z" fill="%s" stroke="%s" stroke-width="6"
      stroke-linejoin="round"/>
<path d="M72 130 h112 l-3 15 h-106 z" fill="%s"/>
<path d="M182 138 q31 -4 31 27 q0 28 -35 30" fill="none" stroke="%s" stroke-width="9" stroke-linecap="round"/>
""" % (LILAC, CREAM, MAUVE, PINK_DEEP, MAUVE))

SVG_04 = svg_open("""
<defs>
  <linearGradient id="ym4" x1="0" y1="0" x2="0.7" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
</defs>
<g transform="rotate(-27 128 132)">
  <ellipse cx="122" cy="134" rx="82" ry="46" fill="url(#ym4)"/>
  <path d="M200 128 q16 -2 20 -14" stroke="%s" stroke-width="8" stroke-linecap="round" fill="none"/>
  <g stroke="%s" stroke-opacity=".22" stroke-width="5" stroke-linecap="round" fill="none">
    <path d="M84 108 q12 26 2 52"/>
    <path d="M110 104 q13 30 3 58"/>
    <path d="M138 104 q12 28 3 56"/>
  </g>
</g>
""" % (LILAC, MAUVE, MAUVE, INK))

SVG_05 = svg_open("""
<circle cx="128" cy="128" r="102" fill="%s"/>
<circle cx="128" cy="128" r="102" fill="none" stroke="%s" stroke-opacity=".25" stroke-width="4"/>
<path d="%s" fill="none" stroke="%s" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="128" cy="128" r="13" fill="%s"/>
""" % (MAUVE, CREAM, spiral_path(128, 128, 26, 74, 2.0), CREAM, PINK_DEEP))

SVG_06 = svg_open("""
<path d="M96 60 C120 104 140 128 140 148 C140 174 122 192 96 192 C70 192 52 174 52 148
         C52 128 72 104 96 60 Z" fill="%s" fill-opacity=".92"/>
<path d="M168 74 C190 114 208 136 208 154 C208 176 192 192 168 192 C144 192 128 176 128 154
         C128 136 146 114 168 74 Z" fill="%s" fill-opacity=".88"/>
<circle cx="140" cy="152" r="16" fill="%s" fill-opacity=".55"/>
""" % (LILAC, PINK_DEEP, MAUVE))

CANDIDATES = [
    ("01", "latte-top", "Top-down latte with swirl art — most on-name", SVG_01),
    ("02", "ube-softserve", "Purple soft-serve cone — playful and bold", SVG_02),
    ("03", "steam-cup", "Steaming cup in side view — cosy and familiar", SVG_03),
    ("04", "ube-yam", "Ube tuber with texture lines — most literal", SVG_04),
    ("05", "swirl-badge", "Swirl in a mauve badge — clearest at 32px", SVG_05),
    ("06", "two-drops", "Two overlapping drops — milk meeting ube", SVG_06),
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
            # bundled headless shell may be missing after a Playwright update
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
            assert bbox[0] > 8 and bbox[1] > 8 and bbox[2] < PREVIEW - 8 and bbox[3] < PREVIEW - 8, \
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
                  CAND_DIR / "contact-light.png", "Ube Latte — vector logo candidates (light)")
    contact_sheet(rendered, (48, 34, 58), (246, 235, 240), (186, 162, 186),
                  CAND_DIR / "contact-dark.png", "Ube Latte — vector logo candidates (dark)")
    inline_strip(rendered, CAND_DIR / "inline-strip.png")
    sel = [c for c in CANDIDATES if c[0] == SELECTED][0]
    icon = rendered[sel[0]].resize((SIZE, SIZE), Image.LANCZOS)
    icon.save(LOGO_OUT)
    print("official icon from SELECTED=%s (%s):" % (sel[0], sel[1]), LOGO_OUT, icon.size)


if __name__ == "__main__":
    main()
