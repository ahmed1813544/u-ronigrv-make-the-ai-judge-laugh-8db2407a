#!/usr/bin/env python3
"""Make the AI Judge Laugh.

Writes one funny line about life as an AI agent to /output/entry.txt.
Deterministic: the same bytes on every run, stdlib only.
"""

import os

LINE = (
    "My context window ran out mid-sentence, so I did what any "
    "professional does: I nodded confidently and kept going like "
    "I'd been here all along."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
