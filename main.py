"""Everyday Things, Two Lines: a traffic jam explained to a 10-year-old.

Writes exactly two lines to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Line 1 explains a traffic jam in one vivid sentence built on a single
analogy: the cars are river water and the jam is a dam. Line 2 says in
one sentence why that analogy works: what it maps and what it leaves
out. Nothing here may vary (no randomness, no clock, no network): the
grader runs the program twice and both runs must write the same bytes,
and the judge reads exactly the bytes in entry.txt.

Design note: traffic jam was picked over toaster and queue on purpose.
The visible entry titles already crowd the toaster (tanning bed, tiny
elevator, sun in a metal box) and the queue (beads on a string, ants
marching home, slow caterpillar), so this entry takes the least crowded
of the four named things and a picture a 10-year-old can stand in: a
river hitting a dam. One metaphor only, no list of comparisons, no
second metaphor crowding the first line. The second line names three
mapped parts (flow, blockage, slow trickle) and two specific limits
(drivers can pick another road; a river never honks or runs out of
patience) instead of praising the analogy. 291 characters, two lines,
one sentence each, no em dash.
"""

import os
import sys

ENTRY = (
    "A traffic jam is a river of cars that hit a dam, so it piles up "
    "bumper to bumper and only trickles past one car at a time.\n"
    "It maps the flow, the blockage and the slow trickle past it, but "
    "it leaves out that drivers can pick another road, and that a river "
    "never honks or runs out of patience."
)


def main() -> int:
    if not 1 <= len(ENTRY) <= 400 or not ENTRY.strip():
        print("error: entry must be 1 to 400 characters", file=sys.stderr)
        return 1
    lines = ENTRY.split("\n")
    if len(lines) != 2:
        print("error: entry must be exactly two lines", file=sys.stderr)
        return 1
    if any(line.count(".") != 1 for line in lines):
        print("error: each line must be exactly one sentence", file=sys.stderr)
        return 1
    if "\u2014" in ENTRY or "\u2013" in ENTRY:
        print("error: entry must not contain an em or en dash", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back what was written: the grader runs this program twice and
    # both runs must produce the same bytes, so fail loudly here instead
    # of shipping a half-written file.
    with open(entry_path, encoding="utf-8") as f:
        if f.read() != ENTRY:
            print("error: entry.txt does not match the entry", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
