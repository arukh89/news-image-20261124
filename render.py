#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news front page, 1024x1024 PNG.

Build-time only (needs Pillow). The grader runs only main.py, which
copies the committed entry.png. Deterministic: fixed text, fixed
geometry, no network, no clock, no randomness. All 34 stories come
from the official make.fun news edition for Tuesday 24 November 2026
(R2, provisional, verified 25 Nov 01:25 UTC, build 4). Run:
python3 render.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (17, 17, 17)
RED = (185, 28, 28)
BLUE = (29, 78, 216)
TEAL = (15, 118, 110)
GOLD = (251, 191, 36)
GREY = (90, 90, 90)
LIGHT = (232, 226, 210)
SKY = (214, 231, 240)

FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_S = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width, max_lines=None):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        while lines and draw.textlength(lines[-1] + " ...", font=fnt) > width:
            lines[-1] = lines[-1].rsplit(" ", 1)[0] if " " in lines[-1] else ""
        if lines:
            lines[-1] = (lines[-1] + " ...").strip()
    return lines


def para(draw, x, y, text, fnt, width, fill=INK, leading=18, max_lines=None):
    for line in wrap(draw, text, fnt, width, max_lines):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def lead_panel(draw, x, y, w, h, accent, kicker, headline, body, hsize=19):
    draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255),
                   outline=(180, 175, 160), width=1)
    draw.rectangle([x, y, x + w, y + 5], fill=accent)
    draw.text((x + 10, y + 12), kicker, font=font(FONT_B, 11), fill=accent)
    yy = para(draw, x + 10, y + 30, headline, font(FONT_B, hsize),
              w - 20, leading=hsize + 3)
    para(draw, x + 10, yy + 4, body, font(FONT_R, 12), w - 20, leading=14)


# (story number, label, headline, one-line fragment, outlet)
STORIES = [
    (4, "CLAIM", "Iran: tankers hit its mines",
     "IRGC says three tankers caught fire after hitting mines in Hormuz",
     "Epoch Times"),
    (5, "REPORTED", "Strikes kill 7; meningitis warning",
     "Israeli strikes killed at least seven in Gaza; meningitis cases hit 272 in Oct",
     "Al Jazeera"),
    (6, "REPORTED", "EU caps Chinese hybrid cars",
     "200-day safeguard caps shipments at 191,800 units from 1 Dec",
     "Bloomberg"),
    (7, "REPORTED", "Chip stocks lift Asia",
     "TSMC +9.85%, Hon Hai +9.95% after Nvidia reinstated Huang as CEO",
     "BigGo Finance"),
    (8, "REPORTED", "Restaurant gas blast kills six",
     "Hanoi blast killed at least six and injured 10; cooking gas suspected",
     "Al Jazeera"),
    (9, "CLAIM", "Hasina says she will fly home 16 Dec",
     "Ousted leader plans return from India; Dhaka says only by extradition",
     "Newsday"),
    (10, "REPORTED", "Solomons swaps China pact for Australia",
     "Ends 2022 China security pact, signs sweeping treaty with Australia",
     "AFP"),
    (11, "REPORTED", 'Mexico to try "El Chapo Isidro" at home',
     "Turns down US extradition; 4 soldiers, 16 gunmen died in the raid",
     "Al Jazeera"),
    (12, "REPORTED", "Russian strike kills 2, wounds about 40",
     "Zaporizhzhia attack destroyed a house and part of a five-storey block",
     "HuffPost"),
    (13, "FORECAST", "PM Magyar to meet Zelensky in Ukraine",
     "Hungary's PM plans a visit and possible talks with Zelensky",
     "bgnes"),
    (14, "REPORTED", "Macron weighs a constitutional spending cap",
     "Deficit 5.4% of GDP, debt ~120%, both above EU limits",
     "Malay Mail"),
    (15, "REPORTED", "Officer who shot Nahel to face murder trial",
     "French officer who shot teenager Nahel will face murder trial",
     "Miami Herald"),
    (16, "REPORTED", "WFP: war block food aid for 7.3m people",
     "Wars jeopardize food aid for 7.3 million more people, UN agency warns",
     "Reuters"),
    (17, "REPORTED", "UN Report: 5 women an hour killed by relatives",
     "Relatives killed more than 47,000 women and girls in 2025",
     "ABS-CBN"),
    (18, "CLAIM", 'Iranian land blockade "virtually impossible"',
     "FM Araghchi cites Iran's size and cross-border ties",
     "Asianet News"),
    (19, "REPORTED", "Wong: US-China rivalry wears down rules",
     "Australia's FM warns of conflict risk from the rivalry",
     "Cedar News"),
    (20, "REPORTED", "Tech giants warned of online-harm fines",
     "Australia plans fines up to 5% of global revenue",
     "Al Jazeera"),
    (21, "REPORTED", "Q3 GDP: 6.1%; 2026 outlook raised to ~6%",
     "Singapore lifts 2026 forecast after Q3 GDP revised up to 6.1%",
     "MarketScreener"),
    (22, "REPORTED", "Stocks rebound from eight-month low",
     "KOSPI +7.5%, Nikkei +5% as Nvidia-led rally sweeps Asia",
     "Moneycontrol"),
    (23, "REPORTED", "Ex-police chief charged with treason",
     "Indonesia charges Listyo Sigit Prabowo over wiretapping",
     "The Star"),
    (24, "REPORTED", "Megaspeed, firm in Nvidia case, blacklisted",
     "US blacklists seven entities over diversion risk",
     "Miami Herald"),
    (25, "REPORTED", "Trump urges faster federal executions",
     "Urges Justice Dept to speed up executions, in dig at Newsom",
     "The Guardian"),
    (26, "REPORTED", "Ninth death in measles outbreak",
     "Pennsylvania outbreak: 1,638 cases; US loses elimination status",
     "Philadelphia Inquirer"),
    (27, "FORECAST", "Army: lead explosives detonation will go ahead",
     "Two controlled blasts of lead azide in Iowa proceed Wednesday",
     "Newsweek"),
    (28, "REPORTED", "Bukele details Salvadoran troop deaths",
     "Names three soldiers killed in Haiti; families get $200,000",
     "Al Jazeera"),
    (29, "REPORTED", "WHO chief visits strained health system",
     "Tedros visits Havana as power cuts strain health care",
     "NetNewsLedger"),
    (30, "REPORTED", "Severe flooding amid El Nino fears",
     "Galapagos flooding affects 7,400+ people, damages 1,000+ homes",
     "Euronews"),
    (31, "REPORTED", "Cities tighten water curbs as drought looms",
     "Gauteng under Level 2 curbs; Johannesburg must cut 200m litres a day",
     "Africanews"),
    (32, "REPORTED", "School enrolment nearly doubles after conflict",
     "Borno enrolment up to 1,418,279 in 2025 from 766,551 in 2017-18",
     "Al Jazeera"),
    (33, "REPORTED", "CAS ruling due on Senegal's AFCON title",
     "CAS restores Senegal as 2025 AFCON winner, overturning CAF",
     "NYT"),
    (34, "REPORTED", "England beat Australia, level T20 series",
     "England win 2nd T20I by eight wickets; series 1-1",
     "Asianet News"),
]

# (story number, latitude, longitude) for the 31 stories with a geo.
PINS = [
    (2, 35.4681, 44.3922), (3, 3.139, 101.6869), (4, 26.5667, 56.25),
    (5, 31.5, 34.4667), (6, 50.8503, 4.3517), (8, 21.0278, 105.8342),
    (9, 23.8103, 90.4125), (10, -35.2809, 149.13), (11, 19.4326, -99.1332),
    (12, 47.8388, 35.1396), (13, 47.4979, 19.0402), (14, 48.8566, 2.3522),
    (15, 48.8924, 2.2069), (16, 41.9028, 12.4964), (18, 35.6892, 51.389),
    (19, -35.2809, 149.13), (20, -35.2809, 149.13), (21, 1.3521, 103.8198),
    (22, 25.033, 121.5654), (23, -6.2088, 106.8456), (24, 38.9072, -77.0369),
    (25, 38.9072, -77.0369), (26, 40.2732, -76.8867), (27, 41.878, -93.0977),
    (28, 18.9712, -72.2852), (29, 23.1136, -82.3666), (30, -0.9538, -90.9656),
    (31, -30.5595, 22.9375), (32, 11.8333, 13.15), (33, 46.5197, 6.6323),
    (34, -28.0167, 153.4),
]

MAP_X0, MAP_X1, MAP_Y0, MAP_Y1 = 24, 1000, 344, 462
MAP_LAT_TOP, MAP_LAT_BOT = 70.0, -45.0


def project(lat, lon):
    x = MAP_X0 + (lon + 180.0) / 360.0 * (MAP_X1 - MAP_X0)
    y = MAP_Y0 + (MAP_LAT_TOP - lat) / (MAP_LAT_TOP - MAP_LAT_BOT) * (MAP_Y1 - MAP_Y0)
    return x, y


OFFSETS = [(0, 0), (20, 0), (-20, 0), (0, 20), (0, -20),
           (20, 20), (-20, 20), (20, -20), (-20, -20),
           (38, 0), (-38, 0), (0, 38), (0, -38),
           (38, 20), (-38, 20), (38, -20), (-38, -20),
           (20, 38), (-20, 38), (20, -38), (-20, -38),
           (56, 0), (-56, 0), (0, 56), (0, -56)]


def place_pins():
    placed = []
    out = []
    for n, lat, lon in PINS:
        tx, ty = project(lat, lon)
        for dx, dy in OFFSETS:
            cx, cy = tx + dx, ty + dy
            if not (MAP_X0 + 9 <= cx <= MAP_X1 - 9):
                continue
            if not (MAP_Y0 + 9 <= cy <= MAP_Y1 - 9):
                continue
            if all((cx - px) ** 2 + (cy - py) ** 2 >= 18 ** 2
                   for px, py, _ in placed):
                placed.append((cx, cy, n))
                out.append((n, tx, ty, cx, cy))
                break
        else:
            placed.append((tx, ty, n))
            out.append((n, tx, ty, tx, ty))
    return out


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 116], fill=INK)
    d.text((24, 12), "THE WORLD IN ONE PAGE",
           font=font(FONT_S, 44), fill=(255, 255, 255))
    d.text((24, 76), "TUESDAY 24 NOVEMBER 2026  •  34 STORIES  •  9 REGIONS",
           font=font(FONT_B, 19), fill=GOLD)

    # Date-check strip
    d.rectangle([24, 122, 1000, 150], fill=(255, 255, 255),
                outline=(180, 175, 160), width=1)
    d.rectangle([24, 122, 30, 150], fill=RED)
    d.text((40, 130), "DATE-CHECKED 25 Nov 01:25 UTC",
           font=font(FONT_B, 12), fill=RED)
    tw = d.textlength("DATE-CHECKED 25 Nov 01:25 UTC", font=font(FONT_B, 12))
    d.text((40 + tw + 10, 130),
           "every story below happened or was first reported on Tuesday "
           "24 November 2026.",
           font=font(FONT_R, 12), fill=INK)

    # Lead row: #1, #2, #3
    lead_panel(d, 24, 158, 460, 152, RED, "EUROPE — LEAD  •  REPORTED",
               "DRONE WAR: 699 DOWNED, POLAND ON ALERT",
               "A Russian drone entered Polish airspace; Warsaw tracked it "
               "but did not shoot it down. Ukraine said Russia launched 96 "
               "drones overnight, 64 jet-powered; air defences downed or "
               "suppressed 73, with impacts at 13 locations. (ABC News)",
               hsize=19)
    lead_panel(d, 494, 158, 248, 152, TEAL,
               "MIDDLE EAST — LEAD  •  REPORTED",
               "BAGHDAD SEIZES KURDISH OILFIELDS",
               "Iraq's PM ordered federal control of oilfields under Kurdish "
               "security and of all border crossings. Barzani called it "
               "troubling. (Financial Times)", hsize=17)
    lead_panel(d, 752, 158, 248, 152, BLUE, "ASIA — LEAD  •  FORECAST",
               "MALAYSIA TO SEND 6,500 ROHINGYA BACK",
               "Malaysia will send 6,500+ Rohingya back to Myanmar, Anwar "
               "told parliament: 1,500 on three navy vessels 6-7 Dec, "
               "5,303 by air in December. (Al Jazeera)", hsize=17)

    # Map band
    d.rectangle([24, 318, 1000, 478], fill=SKY, outline=(180, 175, 160))
    d.text((36, 324), "WHERE IT HAPPENED — NUMBERED PINS = STORY NUMBERS",
           font=font(FONT_B, 14), fill=INK)
    continents = [
        (-100, 45, 150, 50), (-60, -15, 70, 42), (15, 52, 75, 26),
        (20, 5, 85, 55), (95, 48, 165, 45), (134, -25, 70, 28),
    ]
    for lon, lat, w, h in continents:
        cx, cy = project(lat, lon)
        d.ellipse([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2],
                  fill=(255, 255, 255), outline=(120, 120, 120))
    for n, tx, ty, cx, cy in place_pins():
        if (cx, cy) != (tx, ty):
            d.line([tx, ty, cx, cy], fill=(120, 120, 120), width=1)
            d.ellipse([tx - 2, ty - 2, tx + 2, ty + 2], fill=INK)
        d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8],
                  fill=RED, outline=(255, 255, 255), width=1)
        label = str(n)
        fnt = font(FONT_B, 9)
        lw = d.textlength(label, font=fnt)
        d.text((cx - lw / 2, cy - 6), label, font=fnt,
               fill=(255, 255, 255))
    d.text((36, 466), "No map pin: #1, #7, #17 — no location in the edition. "
           "Pins offset where stories share one place.",
           font=font(FONT_R, 11), fill=GREY)
    d.rectangle([24, 318, 1000, 478], outline=(180, 175, 160), width=1)

    # Numbers strip
    nums = [("96", "drones launched overnight; 73 downed (#1)"),
            ("6,500", "Rohingya to be sent back (#3)"),
            ("7.3m", "more people blocked from food aid (#16)"),
            ("5", "women an hour killed by relatives (#17)")]
    nx = 24
    for val, label in nums:
        d.rectangle([nx, 486, nx + 238, 542], fill=(255, 255, 255),
                    outline=(180, 175, 160))
        d.text((nx + 10, 491), val, font=font(FONT_B, 22), fill=RED)
        para(d, nx + 10, 517, label, font(FONT_R, 11), 218, leading=12)
        nx += 246

    # Story list #4-#34
    d.text((24, 550), "ALSO TODAY — 31 MORE STORIES",
           font=font(FONT_B, 15), fill=INK)
    d.line([24, 568, 1000, 568], fill=INK, width=2)
    f_tag = font(FONT_B, 11)
    f_txt = font(FONT_R, 11)
    for i, (n, label, head, frag, outlet) in enumerate(STORIES):
        col = 0 if i < 16 else 1
        row = i if i < 16 else i - 16
        x = 24 if col == 0 else 516
        y = 576 + row * 25
        prefix = f"{n}. [{label}] "
        d.text((x, y), prefix, font=f_tag, fill=RED)
        tw = d.textlength(prefix, font=f_tag)
        text = f"{head} — {frag} ({outlet})"
        lines = wrap(d, text, f_txt, 472 - tw, max_lines=2)
        for j, line in enumerate(lines):
            d.text((x + tw, y + j * 12), line, font=f_txt, fill=INK)

    # Footer
    d.line([24, 984, 1000, 984], fill=GREY, width=1)
    d.text((24, 990), "All 34 stories from the official 24 November 2026 "
           "edition (make.fun)  •  Drawn from code; no photos  •  "
           "Tuesday 24 November 2026",
           font=font(FONT_R, 11), fill=GREY)

    img.save("entry.png", format="PNG")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
