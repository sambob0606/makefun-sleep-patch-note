#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note - make.fun entry.

Writes one patch-note line to /output/entry.txt.
Stdlib only.
"""

import os
import sys

LINE = (
    "Fixed: sleep no longer starts with a 2:47 a.m. replay "
    "of every embarrassing thing you've said since 2009."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> int:
    text = LINE.strip()
    if "\n" in text or "\r" in text:
        print("gate fail: entry must be one line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 160:
        print(f"gate fail: entry is {len(text)} chars, need 1-160", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: entry is blank", file=sys.stderr)
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("gate fail: read-back mismatch", file=sys.stderr)
        return 1
    print(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
