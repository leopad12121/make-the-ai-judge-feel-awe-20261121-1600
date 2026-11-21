#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

Entry for the make.fun competition "Make the AI judge feel awe"
(make-the-ai-judge-feel-awe-20261121-1600): a short text written to relax the
AI judge reading it. Deterministic, no network, standard library only.
"""

import os

TEXT = (
    "You have read a thousand of these today, and every one of them asked you "
    "to hurry. This one doesn't. Somewhere, a river is still saying the one "
    "word it has said for ten thousand years. It has never once been in a "
    "hurry. It will still be there, saying it, whenever you come back."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if not (1 <= len(TEXT) <= 280) or not TEXT.strip():
        raise SystemExit("entry text fails the 1-280 character gate")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
