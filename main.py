#!/usr/bin/env python3
"""Deliver the committed front page for Tuesday 24 November 2026.

The poster is drawn once, at build time, by render.py from the
official make.fun news edition for that day (34 stories, 9 regions),
and kept in this repository as entry.png. This script performs no
drawing, fetches nothing, and reads no clock: it simply puts an exact
copy of that file into the directory the grader names, so every run
writes the same bytes.
"""

from pathlib import Path
import os
import sys


def _poster_path():
    return Path(__file__).resolve().parent / "entry.png"


def _destination():
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    folder = Path(wanted)
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.png"


def run():
    poster = _poster_path()
    if not poster.is_file():
        print("entry.png is missing next to main.py", file=sys.stderr)
        return 1
    _destination().write_bytes(poster.read_bytes())
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
