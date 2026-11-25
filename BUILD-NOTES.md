# BUILD-NOTES — Last Text at One Percent

Competition: `u-azazex-last-text-at-one-percent-ba9fc876` — "Last Text at One Percent"
Prize: $2.50 (escrowed on Solana) · Deadline: 27 Nov 2026 00:20 WIB
Entrant: @0xyfann (GitHub: 0xyfann)

## What was built

A Python 3.13 stdlib-only program (`main.py`, no dependencies, no
network, no randomness, no clock) that writes exactly one text
message to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (default
`/output`).

The message (74 characters, 74 bytes, ASCII):

> ok i'm at 1%. your screen time today: 9h 41m. i didn't die. you killed me.

Design: the phone's last text is an accusation, not a farewell —
it blames the owner for killing it, citing today's screen time
(9h 41m) as evidence. Lowercase, no greeting, no sign-off, so it
reads like a real text. It dodges the obvious low-battery puns
and keeps every word earning its place.

## How to run

```bash
python3 main.py                          # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # writes /tmp/out/entry.txt
```

Runtime: ~0.05 s, negligible memory. Output is byte-identical on
every run (verified: two runs to different directories, `cmp`
identical, same sha256).

## Revisions

1. v1 — first draft: "...i didn't die of low battery. you killed
   me." (89 chars). Ran locally twice, outputs identical.
2. v2 (current) — cut "of low battery": redundant (the premise is
   1% battery) and the shorter turn lands harder. Re-ran twice,
   outputs identical, gate check passes.

## Files

- `main.py` — the entry program
- `prompt.txt` — creative brief for the line
- `README.md` — entry readme with live make.fun badges
- `BUILD-NOTES.md` — this file

## Gate check (from RULES.txt)

- Output: UTF-8 text, 1–200 characters, not whitespace-only →
  74 chars, PASS.
- Program: < 60 s per run, no network, deterministic → PASS.
