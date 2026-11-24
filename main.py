"""The Funniest Toaster Error Message — make.fun entry.

Writes a single deadpan error message, the kind a kitchen toaster would
flash at its owner, to /output/entry.txt. Deterministic: one fixed string,
no randomness, no network, no reads outside this repository.
"""

import os

ENTRY = "ERROR 12: Bagel mode selected. There is no bagel. There has never been a bagel."

# The gate: /output/entry.txt must be UTF-8, 1-120 characters, not only
# whitespace. Enforce it here so a bad edit fails loudly instead of
# submitting an invalid entry.
assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
