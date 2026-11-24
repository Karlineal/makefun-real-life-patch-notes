"""Writes the entry: one line (115 characters), a software release note for a bug in real life.

The sandbox runs it offline, once per grade; it only writes /output/entry.txt.
"""

import pathlib

LINE = (
    "v2.11.0: fixed a bug where standing up too fast re-rendered the room "
    "in greyscale. Rollback instructions: sit down."
)


def main() -> None:
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
