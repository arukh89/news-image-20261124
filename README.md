# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/arukh89/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/arukh89/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One page that sums up Tuesday 24 November 2026 in 34 stories across
9 regions: a drone war that reached Polish airspace, Baghdad seizing
Kurdish-held oilfields, Malaysia sending 6,500 Rohingya back, and 31
more stories from the official make.fun news edition for that day —
each labelled REPORTED, CLAIM, DENIAL or FORECAST and pinned on a
numbered world map, with a date-check box proving every story belongs
to 24 November 2026.

## Run it

```sh
python3 main.py
```

That writes `entry.png` into `out/` (or into `$MAKEFUN_OUTPUT_DIR`
when set). `entry.png` itself is drawn once, at build time, by
`render.py` (Pillow; run `python3 render.py` to redraw it) — `main.py`
only copies the committed image, so two runs write identical bytes.

---

<sub>Entry for the make.fun bounty
[news-image-20261124](https://make.fun/bounty/news-image-20261124).
Drawn from code; no photos.</sub>
