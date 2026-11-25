"""Carry the finished front page for Tuesday 24 November 2026 to the output folder.

The picture was drawn exactly once, while the entry was being built, by
the companion script render.py, and it is stored beside this file as
entry.png. This program draws nothing, downloads nothing, and never
consults a clock. It only places a byte-for-byte copy of that stored
picture into the folder the grader names, so every run writes the same
bytes to the same place.
"""

import pathlib
import shutil


def deliver():
    root = pathlib.Path(__file__).resolve().parent
    picture = root.joinpath("entry.png")
    if not picture.is_file():
        raise SystemExit("entry.png is not beside this script")
    wanted = pathlib.os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    target = pathlib.Path(wanted)
    target.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(picture, target.joinpath("entry.png"))


if __name__ == '__main__':
    raise SystemExit(deliver())
