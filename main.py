"""news-image-20261124 entrypoint.

Reads the image this repository holds (entry.png) and writes it, byte for
byte, to the grader's output directory. Nothing else: no network, no clock,
no files outside this repository, deterministic across runs.

The grader runs it as:
    MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"

BOT_DIR = os.environ.get("MAKEFUN_BOT_DIR", "/bot")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
def main() -> int:
    source = os.path.join(BOT_DIR, IMAGE_NAME)
    target = os.path.join(OUTPUT_DIR, IMAGE_NAME)
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        shutil.copyfile(source, target)
    except OSError as exc:
        print(f"{IMAGE_NAME} could not be copied from {BOT_DIR}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
