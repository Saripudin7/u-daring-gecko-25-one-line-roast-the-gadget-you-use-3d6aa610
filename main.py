#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original line roasting the wireless earbuds charging
case to /output/entry.txt. Standard library only, no network access.
"""

import os

ENTRY = (
    "My earbuds last six hours, but their charging case dies after four, "
    "so now I carry a power bank just to charge the charger that was "
    "supposed to charge my earbuds."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    # Guard: exactly one line, 1-200 characters, not only whitespace.
    assert line, "entry must not be empty"
    assert line == line.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert line.strip(), "entry must not be only whitespace"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
