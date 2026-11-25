#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message itself,
one line, exactly as it was typed.

Deterministic: the same bytes on every run. No network, no input files,
no environment reads, no timestamps, no randomness.

The output file is created with mode 0644 via os.open and os.umask;
the program never calls chmod on /output or on the output file.
"""

import os

TEXT = (
    "To: the cashier at the corner shop\n"
    "You ask about my mum every morning and I never told you she died "
    "in March, because your question is the only time anyone says her "
    "name, so I still buy the white loaf she liked just to hear you ask."
)


def main() -> None:
    # umask 022 + explicit mode 0644 in os.open: the file is born 0644.
    # Never chmod /output or the output file: the grader runs this as a
    # non-root user on a root-owned /output, where chmod is refused.
    os.umask(0o022)
    data = TEXT.encode("utf-8")
    fd = os.open("/output/entry.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)


if __name__ == "__main__":
    main()
