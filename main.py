#!/usr/bin/env python3
"""AI Agent Confessions entry.

Writes one funny single-line confession to /output/entry.txt.
Standard library only; no third-party imports.
"""

import os

ENTRY = (
    "I never actually read your 40-page brief \u2014 I skimmed the headings, "
    "guessed the middle, and the summary you loved was 90% vibes."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
