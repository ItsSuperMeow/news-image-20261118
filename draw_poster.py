#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news poster (1024x1024 PNG).

Layout: navy masthead, one lead story (Gulf escalation) with a drawn
illustration panel, then five labelled story rows. All text is drawn with
DejaVu Sans; every line is wrapped to fit its box before drawing.
"""
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

PAPER = (247, 243, 234)      # warm off-white
NAVY = (20, 33, 61)          # masthead
NAVY_SOFT = (31, 48, 84)
RED = (178, 34, 34)          # kickers / accents
GOLD = (212, 175, 55)        # date line
INK = (24, 24, 24)
GREY = (90, 90, 88)
RULE = (200, 192, 172)
SKY = (18, 38, 74)          # illustration sky
SEA = (46, 92, 122)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning lines that fit max_w pixels."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, max_w, fill, spacing=4):
    lines = wrap(draw, text, fnt, max_w)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def draw_gulf_panel(draw, x0, y0, w, h):
    """Simple drawn scene: night sky, missile arcs, interception bursts
    over a Gulf coastline. All shapes, no photos."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=SKY, outline=NAVY, width=3)
    # stars
    for sx, sy, r in [(30, 26, 2), (90, 60, 2), (150, 30, 3), (210, 70, 2),
                      (260, 34, 2), (60, 110, 2), (180, 110, 2), (120, 84, 2)]:
        draw.ellipse([x0 + sx - r, y0 + sy - r, x0 + sx + r, y0 + sy + r],
                     fill=(255, 255, 255))
    # missile arcs (red trails with bright heads)
    draw.arc([x0 + 20, y0 + 60, x0 + 200, y0 + 260], start=200, end=330,
             fill=(220, 60, 50), width=5)
    draw.arc([x0 + 90, y0 + 30, x0 + 290, y0 + 240], start=210, end=320,
             fill=(240, 120, 60), width=5)
    draw.ellipse([x0 + 168, y0 + 62, x0 + 182, y0 + 76], fill=(255, 220, 120))
    draw.ellipse([x0 + 246, y0 + 44, x0 + 260, y0 + 58], fill=(255, 220, 120))
    # interception bursts (gold starbursts)
    for bx, by in [(110, 150), (215, 120)]:
        for dx, dy in [(0, -16), (0, 16), (-16, 0), (16, 0),
                       (-11, -11), (11, -11), (-11, 11), (11, 11)]:
            draw.line([x0 + bx, y0 + by, x0 + bx + dx, y0 + by + dy],
                      fill=GOLD, width=4)
        draw.ellipse([x0 + bx - 7, y0 + by - 7, x0 + bx + 7, y0 + by + 7],
                     fill=(255, 235, 150))
    # sea and coastline
    draw.rectangle([x0, y0 + h - 58, x0 + w, y0 + h], fill=SEA)
    draw.line([x0, y0 + h - 58, x0 + w, y0 + h - 58], fill=(255, 255, 255),
              width=2)
    # small ships / base silhouette on the coast
    draw.rectangle([x0 + 30, y0 + h - 92, x0 + 70, y0 + h - 58],
                   fill=(10, 22, 44))
    draw.rectangle([x0 + 44, y0 + h - 112, x0 + 56, y0 + h - 92],
                   fill=(10, 22, 44))
    draw.rectangle([x0 + 220, y0 + h - 84, x0 + 252, y0 + h - 58],
                   fill=(10, 22, 44))
    draw.text((x0 + 10, y0 + h - 30), "GULF  •  18 NOV", font=font(BOLD, 15),
              fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 154], fill=GOLD)
    d.text((40, 22), "THE WORLD IN ONE DAY", font=font(BOLD, 52), fill=(255, 255, 255))
    d.text((40, 92), "WEDNESDAY  18  NOVEMBER  2026", font=font(BOLD, 30),
           fill=GOLD)

    # ---- Lead story: Gulf escalation ----
    y = 176
    d.text((40, y), "LEAD STORY", font=font(BOLD, 20), fill=RED)
    y += 30
    panel_x, panel_y, panel_w, panel_h = 40, y, 300, 250
    draw_gulf_panel(d, panel_x, panel_y, panel_w, panel_h)

    tx = 372
    d.text((tx, y), "GULF ESCALATION", font=font(BOLD, 26), fill=RED)
    y2 = draw_wrapped(
        d, tx, y + 38,
        "Gulf states intercept Iranian missiles and drones",
        font(BOLD, 36), 612, INK, spacing=6)
    y2 = draw_wrapped(
        d, tx, y2 + 8,
        "Iran says it targeted US drone and missile installations at "
        "Kuwait's Ali Al Salem air base. Bahrain reports a third "
        "interception this week.",
        font(REG, 22), 612, (52, 52, 52), spacing=5)
    d.text((tx, y2 + 4),
           "Tuesday: US jets struck an IRGC missile site on Qeshm Island.",
           font=font(REG, 19), fill=GREY)

    # ---- Divider ----
    div_y = 470
    d.line([40, div_y, W - 40, div_y], fill=RULE, width=3)

    # ---- Five story rows ----
    rows = [
        ("2", "SHENZHEN SUMMIT",
         "Xi and Putin meet at APEC; Trump–Xi–Putin trio due Thursday",
         "Xi greets Trump at the airport; a Trump–Putin one-on-one also planned."),
        ("3", "ALASKA SENATE",
         "Peltola beats Sullivan; Democrats take a 56–44 majority",
         "First Alaska Native in the US Senate — 50.1% to 45.8%; last 2026 race called."),
        ("4", "ANTHROPIC IPO",
         "Anthropic prices IPO at $83 — the largest listing on record",
         "980m shares, about $81.3bn; trading as ANT on Nasdaq starts Thursday."),
        ("5", "VOYAGER 1",
         "Voyager 1 reaches one light-day from Earth",
         "16.1 billion miles out; signals now take 24 hours each way. Launched 1977."),
        ("6", "EU UKRAINE LOAN",
         "EU proposes a €45bn loan for Ukraine in 2027",
         "Covers two-thirds of Kyiv's needs; repaid from frozen Russian assets."),
    ]
    row_y = div_y + 18
    row_h = 96
    for num, label, head, sub in rows:
        # number badge
        cx, cy = 72, row_y + 30
        d.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], fill=NAVY)
        num_f = font(BOLD, 30)
        tw = d.textlength(num, font=num_f)
        d.text((cx - tw / 2, cy - 21), num, font=num_f, fill=(255, 255, 255))
        # label + headline + subhead
        lx = 116
        d.text((lx, row_y), label, font=font(BOLD, 20), fill=RED)
        hy = draw_wrapped(d, lx, row_y + 26, head, font(BOLD, 25), W - 40 - lx,
                          INK, spacing=2)
        d.text((lx, hy + 2), sub, font=font(REG, 20), fill=(72, 72, 72))
        row_y += row_h
        if num != "6":
            d.line([40, row_y - 8, W - 40, row_y - 8], fill=RULE, width=1)

    # ---- Footer ----
    d.text((40, H - 34), "Sources: Reuters • AP • NASA/JPL • Anthropic • European Commission",
           font=font(REG, 17), fill=GREY)

    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT} {img.size}")


if __name__ == "__main__":
    main()
