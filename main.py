#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes exactly one word to /output/entry.txt: the single word this
entry would erase from the dictionary forever. Nothing else attached.

v1: "delete" -- the deletion performs itself: erase the word for
erasing, and the dictionary can never describe what just happened.

v2: "word" -- the dictionary deletes its own subject. "delete" is the
first clever pick every entrant makes, so it risks being duplicated
across the field (and possibly one of the house's fixed texts, which
would share its rate and never reach the playoff). "word" is fresher,
two bytes shorter (4 vs 6, which wins the byte tie-break), and the
joke lands in the same single beat: a dictionary with no word for
"word" cannot name a single thing it contains.
"""

import os
import sys

WORD = "word"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
