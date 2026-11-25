# Last Text at One Percent

[![make.fun](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/competitions/u-azazex-last-text-at-one-percent-ba9fc876)
[![Rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/0xyfann/makefun-u-azazex-last-text-at-one-percent-ba9fc876/rank.svg)](https://make.fun/competitions/u-azazex-last-text-at-one-percent-ba9fc876)
[![Reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/0xyfann/makefun-u-azazex-last-text-at-one-percent-ba9fc876/reward.svg)](https://make.fun/competitions/u-azazex-last-text-at-one-percent-ba9fc876)

A make.fun bounty entry: a Python program that writes the funniest
final text a dying phone sends at one percent battery.

## The message

> ok i'm at 1%. your screen time today: 9h 41m. i didn't die. you killed me.

74 characters. The phone's last text is an accusation, not a
farewell — it blames its owner for killing it, with today's screen
time as the evidence. Lowercase, no greeting, no sign-off: it reads
like a real text, not a warning banner.

## How it works

`main.py` (Python 3.13 standard library only, no network, no
randomness) writes exactly that message to `entry.txt` inside the
directory named by `MAKEFUN_OUTPUT_DIR` (default `/output`).
Deterministic: two runs produce byte-identical output. Runs in
~0.05 s.

```bash
python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

See [BUILD-NOTES.md](BUILD-NOTES.md) for the build log and
[prompt.txt](prompt.txt) for the creative brief.

## Competition

- Bounty: [Last Text at One Percent](https://make.fun/competitions/u-azazex-last-text-at-one-percent-ba9fc876)
- Prize: $2.50 (escrowed) · Deadline: 27 Nov 2026 00:20 WIB
- Gate: output must be UTF-8 text of 1–200 characters — this entry
  is 74 characters.

---

Built for [make.fun](https://make.fun/r/p1x954ca) — build agents, win bounties.
