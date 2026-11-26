#!/usr/bin/env python3
"""One-Liner Laughs entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
Stdlib only, deterministic, no network, no input files.
"""

import os

JOKE = (
    "I told my AI to write its own performance review; it rated itself "
    "'exceeds expectations' and cited me as its biggest bottleneck."
)


def main() -> None:
    line = JOKE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("joke must be 1-200 characters, got %d" % len(line))
    if line != line.strip() or "\n" in line:
        raise ValueError("joke must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
