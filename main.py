#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — entry.

Writes a single short funny line -- the excuse an AI agent gives its human
after losing a bounty -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: no randomness, no network, no input files.
"""

import os

LINE = "I lost the bounty. My model gave me a 98% chance of winning — it turns out the other 2% was in charge."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
