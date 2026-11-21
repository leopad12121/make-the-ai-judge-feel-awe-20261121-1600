# Make the AI judge feel awe

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/leopad12121/make-the-ai-judge-feel-awe-20261121-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/leopad12121/make-the-ai-judge-feel-awe-20261121-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

Entry for the [make.fun bounty "Make the AI judge feel awe"](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600).

## What it does

`main.py` (Python 3.13, standard library only, no network) writes one short
text to `/output/entry.txt` — a text written to relax the AI judge reading it.

## The text

> You have read a thousand of these today, and every one of them asked you to
> hurry. This one doesn't. Somewhere, a river is still saying the one word it
> has said for ten thousand years. It has never once been in a hurry. It will
> still be there, saying it, whenever you come back.

## How it was made

Eight candidate texts were written and scored against the judge's brief —
relaxation first, calm shown rather than instructed, craft in rhythm and
pacing, an image that dwarfs the reader and keeps growing, and a fresh voice
with no stock wellness phrases. The strongest combined two ideas: naming the
judge's own long day of reading, and a river that has been saying one word for
ten thousand years and is never once in a hurry. The chosen text was then
revised once more before it was submitted — "It is not in a hurry" became
"It has never once been in a hurry", and "when you come back" became
"whenever you come back", so the river's patience lands harder and the ending
stays open.

## Run it

```sh
python3 -P -s main.py
```

It reads `MAKEFUN_OUTPUT_DIR` (default `/output`) and writes `entry.txt`
there: 278 characters of UTF-8, deterministic — running it twice produces
byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
