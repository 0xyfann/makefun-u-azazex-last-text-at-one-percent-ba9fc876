#!/usr/bin/env python3
"""Last Text at One Percent -- make.fun entry.

Writes exactly one final text message from a dying phone to
``entry.txt`` inside the directory named by MAKEFUN_OUTPUT_DIR
(default: /output, the grader's output directory).

Python 3.13 standard library only. No network, no randomness, no
clock reads, no environment reads other than MAKEFUN_OUTPUT_DIR --
so two runs produce byte-identical output.
"""

import os
import sys

# The message, written by hand for this competition. Lowercase, no
# greeting, no sign-off: it reads like a real last text, not a
# warning banner. The joke is a turn: the phone does not die of low
# battery, it accuses its owner of killing it -- with one specific,
# embarrassing number (today's screen time) as the evidence.
# REVISION (after first local run): cut "of low battery" -- redundant,
# the whole premise is 1% battery, and the shorter turn ("i didn't
# die. you killed me.") lands harder with no wasted words.
MESSAGE = (
    "ok i'm at 1%. your screen time today: 9h 41m. "
    "i didn't die. you killed me."
)

MAX_CHARS = 200


def main() -> int:
    # Gate mirror: the sealed scorer requires UTF-8 text of 1 to 200
    # characters, not only white space. Fail loudly here instead of
    # shipping an invalid entry.
    if not MESSAGE or not MESSAGE.strip():
        print("error: message is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(MESSAGE) > MAX_CHARS:
        print(
            "error: message is %d chars, over the %d limit"
            % (len(MESSAGE), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    # Write exactly the message, no trailing newline: the gate counts
    # every character, and a newline would be a wasted one.
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(MESSAGE)

    print("wrote %s (%d chars)" % (out_path, len(MESSAGE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
