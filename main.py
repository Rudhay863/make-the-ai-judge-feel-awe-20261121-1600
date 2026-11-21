"""Entry for make.fun bounty 'Make the AI judge feel awe'.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. No network, no input files.
"""

import os

TEXT = (
    "Somewhere, a river is still wearing down one stone. "
    "It began before the oldest road in your town, "
    "and it is in no hurry. The water never asks the stone to be "
    "finished. It just keeps coming, cold and patient, "
    "and the stone keeps getting smoother, long after we are gone."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
