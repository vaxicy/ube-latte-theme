#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ube Latte Theme — promo tiles (440x280 + 1400x560), all English.

Colours are read from manifest.json. Each canvas has its own geometry and font
scale; the layout is redrawn from scratch every run, with bounds assertions so
overflow fails loudly at generation time.
"""
import json
import os
import time
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))                      # relative paths only (non-ASCII path safety)

OUT_DIR = "store-assets/promo"


def save_png(img, path, tries=5):
    """PIL intermittently raises OSError [Errno 22] on this non-ASCII project path.

    Observed on Windows: the very same save() succeeds on one run and fails on the
    next, so retry a few times instead of crashing the whole generation.
    """
    last = None
    for i in range(tries):
        try:
            img.save(path)
            return
        except OSError as exc:            # pragma: no cover - environment specific
            last = exc
            time.sleep(0.35 * (i + 1))
    raise last


def rgb(vals):
    return tuple(vals)


def font(size, bold=False):
    for name in (("segoeuib.ttf", "seguisb.ttf") if bold else ("segoeui.ttf", "segoeuisl.ttf")):
        p = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def text_w(d, s, f):
    return d.textbbox((0, 0), s, font=f)[2]


def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def bg_gradient(size, top, bottom):
    w, h = size
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        d.line([(0, y), (w, y)], fill=lerp(top, bottom, y / max(1, h - 1)))
    return img


def draw_chip(d, x, y, h, label, f, fill, txt, pad=18):
    w = text_w(d, label, f) + pad * 2
    d.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, fill=fill)
    d.text((x + pad, y + (h - f.size) // 2 - 3), label, font=f, fill=txt)
    return w


def compose(size, geom, colors, props):
    W, H = size
    M = geom["margin"]
    RIGHT = W - M

    img = bg_gradient(size, rgb(colors["ntp_background"]), rgb(colors["button_background"]))
    d = ImageDraw.Draw(img)

    ink = rgb(colors["ntp_text"])
    sub = lerp(ink, rgb(colors["ntp_background"]), 0.34)
    chip_bg = rgb(colors["ntp_header"])
    cta_bg = rgb(colors["frame"])
    cta_txt = rgb(colors["tab_text"])

    # palette strip: one long band across the full width, split into segments
    # (user request 2026-10-20: long strips instead of a tile grid, so the
    #  composition no longer leaves the left side empty)
    # tall vertical palette strips on the right (user request 2026-10-20):
    # five distinct colours, pale -> deep, running nearly the full canvas height
    # so the composition stays balanced against the text column.
    strip_colors = [rgb(colors["ntp_background"]), rgb(colors["button_background"]),
                    rgb(colors["button_background_secondary"]), rgb(colors["frame"]),
                    rgb(colors["ntp_link"])]
    n = len(strip_colors)
    block_w, sgap = geom["block_w"], geom["strip_gap"]
    sw = (block_w - sgap * (n - 1)) / n
    top, bottom = geom["strip_top"], geom["strip_bottom"]
    assert sw > 0, "invalid strip width"
    assert top >= 24 and bottom <= H - 24, "strips too close to the canvas edge"
    bx = int(round(RIGHT - block_w))
    assert bx >= M + 180, "strips would overlap the text column"

    # a very soft shadow keeps the palest strips readable against a same-hue
    # background without drawing an outline
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    x = bx
    for _ in strip_colors:
        sd.rounded_rectangle([x, top + 4, x + sw, bottom + 4], radius=sw / 2, fill=ink + (28,))
        x += sw + sgap
    shadow = shadow.filter(ImageFilter.GaussianBlur(6))
    img = Image.alpha_composite(img.convert("RGBA"), shadow).convert("RGB")
    d = ImageDraw.Draw(img)

    x = bx
    for col in strip_colors:
        d.rounded_rectangle([x, top, x + sw, bottom], radius=sw / 2, fill=col)
        x += sw + sgap
    assert x - sgap <= RIGHT + 0.5, "palette strips overflow the right margin"

    lsize = geom["logo"]
    logo = Image.open("logo/logo.png").convert("RGBA").resize((lsize, lsize), Image.LANCZOS)
    img.paste(logo, (M, geom["logo_y"]), logo)

    f_title, f_sub = font(geom["title_size"], True), font(geom["sub_size"])
    tx = M + (lsize + geom["logo_gap"] if geom["title_beside_logo"] else 0)
    ty = geom["title_y"] if geom["title_beside_logo"] else geom["logo_y"] + lsize + geom["logo_gap"]
    d.text((tx, ty), geom["title"], font=f_title, fill=ink)
    sub_y = ty + geom["title_size"] + geom["title_sub_gap"]
    d.text((tx if geom["title_beside_logo"] else M, sub_y), geom["subtitle"], font=f_sub, fill=sub)
    assert geom["title_sub_gap"] >= 8, "title/subtitle gap too tight"

    f_chip = font(geom["chip_size"])
    cx, cy = (tx if geom["title_beside_logo"] else M), sub_y + geom["sub_size"] + geom["chip_gap"]
    for label in geom["chips"]:
        w = draw_chip(d, cx, cy, geom["chip_h"], label, f_chip, chip_bg, ink)
        cx += w + geom["chip_gap_x"]
    assert cx - geom["chip_gap_x"] <= RIGHT, "chip row overflows the right margin"

    f_cta = font(geom["cta_size"], True)
    btn_w, btn_h = geom["cta_w"], geom["cta_h"]
    btn_x = M
    btn_y = geom["cta_y"] if geom["cta_beside"] else cy + geom["chip_h"] + geom["cta_gap"]
    d.rounded_rectangle([btn_x, btn_y, btn_x + btn_w, btn_y + btn_h], radius=btn_h // 2, fill=cta_bg)
    tw = text_w(d, geom["cta"], f_cta)
    d.text((btn_x + (btn_w - tw) // 2, btn_y + (btn_h - f_cta.size) // 2 - 3),
           geom["cta"], font=f_cta, fill=cta_txt)
    assert btn_y + btn_h <= H - 12, "CTA button too close to the canvas bottom"
    assert btn_x + btn_w <= RIGHT, "CTA button overflows the right margin"
    return img, {"btn": (btn_x, btn_y, btn_w, btn_h),
                 "strips": (bx, top, block_w, bottom - top)}


LARGE = {
    "margin": 70,
    "logo": 104, "logo_y": 82, "logo_gap": 26, "title_beside_logo": True,
    "title": "Ube Latte", "title_size": 58, "title_y": 98,
    "title_sub_gap": 14, "subtitle": "A creamy purple Chrome theme", "sub_size": 21,
    "chips": ["Solid colors", "Lilac & plum", "Easy on the eyes"],
    "chip_size": 15, "chip_h": 34, "chip_gap": 34, "chip_gap_x": 12,
    "cta": "Try It Now", "cta_size": 20, "cta_w": 210, "cta_h": 54,
    "cta_y": 366, "cta_beside": True,
    "block_w": 300, "strip_gap": 10, "strip_top": 104, "strip_bottom": 456,
}

SMALL = {
    "margin": 28,
    "logo": 46, "logo_y": 22, "logo_gap": 10, "title_beside_logo": False,
    "title": "Ube Latte", "title_size": 26, "title_y": 0,
    "title_sub_gap": 8, "subtitle": "A creamy purple Chrome theme", "sub_size": 12,
    "chips": ["Solid colors", "Lilac & plum"],
    "chip_size": 10, "chip_h": 22, "chip_gap": 12, "chip_gap_x": 8,
    "cta": "Try It Now", "cta_size": 13, "cta_w": 118, "cta_h": 36,
    "cta_y": 0, "cta_gap": 16, "cta_beside": False,
    "block_w": 132, "strip_gap": 6, "strip_top": 56, "strip_bottom": 224,
}


def main():
    with open("manifest.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        c = data["theme"]["colors"]
        p = data["theme"]["properties"]
    os.makedirs(OUT_DIR, exist_ok=True)
    for size, geom in (((1400, 560), LARGE), ((440, 280), SMALL)):
        img, boxes = compose(size, geom, c, p)
        out = "%s/%dx%d.png" % (OUT_DIR, size[0], size[1])
        save_png(img, out)
        print("saved:", out, img.size, img.mode, "cta:", boxes["btn"], "strips:", boxes["strips"])


if __name__ == "__main__":
    main()
