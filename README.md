# The World on 13 Nov 2026 — a news-image-01 entry

One image that sums up the world's news of Friday 13 November 2026, drawn as
a flat editorial grid of seven captioned tiles under the header
"THE WORLD ON 13 NOV 2026":

- **SENATE SUMMONS EX-NVIDIA CEO** — the Senate Banking Committee summons
  Jensen Huang (who had resigned as Nvidia's chief executive the day before)
  and Secretary Lutnick; an empty witness chair, his leather jacket, a gavel
  and a very large chip.
- **ZELENSKY MEETS US ENVOYS** — envoys Witkoff and Kushner, fresh from
  Moscow, brief Zelensky in Dublin; Europe joins the next round of talks.
- **DRONE HITS RUSSIAN WARSHIP** — a Ukrainian drone strike on a Russian
  corvette in the Gulf of Finland, detected by Finland's military.
- **IRAN CLAIMS US RADAR STRIKE** — the IRGC's claimed strike on a US
  early-warning radar in Bahrain (labelled as a claim, as reported).
- **FBI: N. KOREA $400M CRYPTO HACK** — North Korean hackers' $400m crypto
  theft through fake video calls, per the FBI.
- **MICROSOFT GLOBAL OUTAGE** — the worldwide Microsoft 365 outage that
  rolled through the day.
- **KANE BREAKS ENGLAND RECORD** — Harry Kane's record-breaking 126th
  England cap.

The picture was chosen by a local pairwise tournament over twelve generated
candidates, judged on the competition's own rubric (that day's news, breadth,
readability, faithfulness, craft at small size); the research and the
tournament record live in `news-notes.md` and `tournament.md` in the build
notes, and the final PNG is 1024×1024, palette-compressed to stay well under
the 1 MiB gate.

## Run it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png, byte for byte the committed entry.png
```

With no `MAKEFUN_OUTPUT_DIR` set, the program writes to `/output/entry.png`,
as the competition's sandbox expects. Standard library only.
