#!/usr/bin/env python3
"""The 3 AM Excuse — v1 (C5).

Writes one funny line to /output/entry.txt. The line is the whole entry:
a hardware wallet whose 24 seed words hold a vote at 3 AM — and vote
24 to nothing against signing.
"""

import os

TEXT = "All 24 of my words held a vote at 3 AM. It was 24–0 against you."


def main():
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
