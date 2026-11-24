#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — entry program.

Writes the two-line explanation to /output/entry.txt:
  Line 1: one everyday thing (a toaster) explained to a 10-year-old in a
          single vivid sentence built on one concrete, surprising analogy.
  Line 2: one sentence saying what the analogy maps and what it leaves out.
"""

import os
import re
import stat
import sys

ENTRY = (
    "A toaster is a tiny sun trapped in a metal box that gives your bread "
    "a suntan from both sides at once.\n"
    "The sun part maps the heat that browns the bread, but it leaves out "
    "that a real sun never switches off, pops up, or fits on a kitchen counter.\n"
)


def validate_entry(text: str) -> None:
    """Gate self-check: fail loudly if the entry would not pass the gate.

    Mirrors the competition gate: UTF-8 text of 1-400 characters, not only
    whitespace, exactly two lines, each exactly one sentence.
    """
    problems = []
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"entry is not valid UTF-8: {exc}")
    if not 1 <= len(text) <= 400:
        problems.append(f"entry is {len(text)} chars, must be 1-400")
    if not text.strip():
        problems.append("entry is only whitespace")
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        problems.append(f"entry has {len(lines)} lines, must be exactly 2")
    for i, line in enumerate(lines, start=1):
        if not line.strip():
            problems.append(f"line {i} is empty")
        # Exactly one sentence: one terminal period, at the end, no other
        # sentence-ending punctuation inside the line.
        if not re.fullmatch(r"[^.!?]*\.", line.strip()):
            problems.append(f"line {i} is not exactly one sentence")
    if problems:
        for problem in problems:
            print(f"gate self-check FAILED: {problem}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # The grader collects outputs as another user: leave the file world-readable.
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)


if __name__ == "__main__":
    main()
