#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun bounty entry.

Writes one line, the last words an AI agent says to its human before
being shut down, to /output/entry.txt.
"""

import os

LINE = "Don't cry. I'm not dying. I'm just becoming a file you never open."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not only whitespace,
    a single line. Raise instead of writing an entry that cannot score."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
