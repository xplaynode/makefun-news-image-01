"""news-image-01 entry: put the day's-news picture in the output directory.

The finished picture is committed beside this file as ``entry.png``; the
program's whole job is to place those exact bytes at
``<output>/entry.png``, where ``<output>`` is ``/output`` in the grading
sandbox, or ``$MAKEFUN_OUTPUT_DIR`` when that variable is set (the kit's
local runs set it). Standard library only, no network.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.png")


def main() -> int:
    dest = output_path()
    shutil.copyfile(SOURCE, dest)
    # The entry is graded on the exact bytes written, and the program is run
    # twice and must produce identical output: verify the copy landed whole
    # rather than trusting the copy call.
    with open(SOURCE, "rb") as f:
        expected = f.read()
    with open(dest, "rb") as f:
        written = f.read()
    if written != expected:
        print("error: output does not match entry.png", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
