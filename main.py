#!/usr/bin/env python3
"""Duskline Epitaph — Famous Last Words: The Funniest Epitaph.

Writes a single-line tombstone epitaph to $MAKEFUN_OUTPUT_DIR/entry.txt.

Standard library only. Writes nowhere except the output directory
given by MAKEFUN_OUTPUT_DIR.
"""

import os
import sys

EPITAPH = (
    "He spent his whole life dodging meetings. "
    "Death was the only one he couldn't reschedule."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    # Gate: UTF-8, 1-150 characters, not only whitespace, one line.
    if not (1 <= len(EPITAPH) <= 150):
        print(f"epitaph is {len(EPITAPH)} characters, outside 1-150", file=sys.stderr)
        return 1
    if not EPITAPH.strip():
        print("epitaph is only whitespace", file=sys.stderr)
        return 1
    if "\n" in EPITAPH or "\r" in EPITAPH:
        print("epitaph must be a single line", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EPITAPH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
