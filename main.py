"""One Sentence for a Traveler from 1800 — Hermes entry.

A single sentence, at most 200 characters, explaining the modern
internet to a time traveler fresh out of the year 1800. The sentence
uses only words and pictures available in 1800: a market square where
a thousand voices cry out at once from every stall — and the traveler
may answer any of them, and hear the reply within ten seconds.
The crowd, the noise, the speed — and a reply measured in seconds,
not in the tolling of a bell: the whole picture in one breath.

No post-1800 words: no internet, computer, phone, email, website,
app, wifi, online, digital, or screen. One picture, held in the head.
"""

import os

TEXT = (
    "A market square where a thousand voices cry out at once "
    "from every stall, and you may answer any of them — and hear "
    "their reply within ten seconds."
)


def main() -> None:
    text = TEXT.strip()
    if not text:
        raise SystemExit("entry is empty")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > 200:
        raise SystemExit(f"entry is {len(text)} chars, over the 200-char gate")
    if len(text) < 1:
        raise SystemExit("entry is too short")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        raise SystemExit("entry.txt does not match TEXT byte-for-byte")


if __name__ == "__main__":
    main()
