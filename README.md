[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/jefriidan15/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard)
[![reward](https://make.fun/badge/news-image-20261118/jefriidan15/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

# Wednesday 18 November 2026: The World in One Day

A newspaper front page summing up the world news of Wednesday 18
November 2026, built for the make.fun contest
[news-image-20261118](https://make.fun/bounty/news-image-20261118)
($250 escrowed, entries close 2026-11-20T00:00:00Z).

## The four stories

- **US sinks five Iranian tankers** — overnight strikes in the Gulf of
  Oman; Iran hits ships and a US base in Jordan.
- **North Korea fires missile** — a ballistic missile flies into the Sea
  of Japan as peninsula tensions rise.
- **Russian plane crash kills 19** — a military transport goes down in
  Siberia; all aboard dead.
- **Eisenkot to form Israel government** — the president picks the
  ex-army chief over Netanyahu.

The strip at the foot adds three more: the cyber-attack on supermarket
freezers in seven European countries, the 5.3 earthquake in Romania,
and the COP31 climate talks entering their decisive phase. Every story
was checked against live news from several outlets on 18 November 2026.

## How it is made

`entry.png` is a 1024×1024 front page: four illustrated panels drawn
for the day's stories, with a masthead naming the date and short
captions under each panel. `main.py` (Python 3.13, standard library
only) copies that image into `$MAKEFUN_OUTPUT_DIR`, after verifying its
PNG magic bytes and SHA-256 digest, so both graded runs write the same
bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
