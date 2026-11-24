#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — entry program.

Writes the two-line explanation to /output/entry.txt:
  Line 1: one everyday thing (a toaster) explained to a 10-year-old in a
          single vivid sentence built on one concrete, surprising analogy.
  Line 2: one sentence saying what the analogy maps and what it leaves out.
"""

import os
import stat

ENTRY = (
    "A toaster is a tiny sun trapped in a metal box that gives your bread "
    "a suntan from both sides at once.\n"
    "The sun part maps the heat that browns the bread, but it leaves out "
    "that a real sun never switches off, pops up, or fits on a kitchen counter.\n"
)


def main() -> None:
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
