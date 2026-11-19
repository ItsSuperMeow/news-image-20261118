# News Image — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/ItsSuperMeow/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/ItsSuperMeow/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image that sums up the world news of **Wednesday 18 November 2026**.

Built for the [make.fun news-image-20261118 bounty](https://make.fun/bounty/news-image-20261118)
($250, 50 paid places). The entry is `main.ts` at the root: it copies
`entry.png` to `/output/entry.png`. The image is drawn in code
(`draw_poster.py`, Python + Pillow) so every label is crisp and legible.

## The six stories

All six were verified against primary news reporting on 18 November 2026:

1. **Gulf escalation** — Gulf states intercepted missiles and drones from
   Iran and its Houthi allies; Iran's army said it targeted US drone and
   missile installations at Kuwait's Ali Al Salem air base; Bahrain said it
   intercepted Iranian attacks for a third time this week. (Context: on
   Tuesday 17 Nov, US fighter jets struck an IRGC missile launch site on
   Qeshm Island.) Source: Reuters.
2. **Shenzhen summit** — Xi Jinping and Vladimir Putin met in Shenzhen at
   the APEC summit; Xi greeted Donald Trump at the airport; the first-ever
   three-way Trump–Xi–Putin meeting is set for Thursday 19 Nov, plus a
   Trump–Putin one-on-one. Source: Reuters.
3. **Alaska Senate** — Democrat Mary Peltola defeated Republican incumbent
   Dan Sullivan (AP called it Tuesday night, 17 Nov US time); the last
   Senate race of the 2026 midterms called; Democrats take a 56–44 majority
   after flipping nine seats; Peltola is the first Alaska Native in the US
   Senate (50.1% vs 45.8%). Source: AP.
4. **Anthropic IPO** — Anthropic priced its IPO at $83 a share, above its
   $70–78 range; 980 million shares, about $81.3bn — the largest listing on
   record, passing SpaceX; trading on Nasdaq as ANT starts 19 Nov; roughly
   $1.5tn valuation fully diluted. Sources: Anthropic announcement, CNBC/AP.
5. **Voyager 1** — At 5:16 a.m. ET (10:16 UTC) NASA's Voyager 1 became the
   first human-made object one light-day (16.1 billion miles) from Earth;
   its radio signals now take 24 hours each way. Launched 1977.
   Source: NASA/JPL.
6. **EU Ukraine loan** — European Commission President Ursula von der Leyen
   announced a proposed €45bn loan to Ukraine for 2027, covering about
   two-thirds of Kyiv's financing needs, to be repaid from frozen Russian
   assets. Sources: European Commission, Reuters/AP.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# writes out/entry.png (1024x1024 PNG, 129 KiB)
```

## Regenerate the poster

```sh
python3 draw_poster.py   # writes entry.png
```
