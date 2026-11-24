[![competition](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Kii922/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Kii922/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# World News — 24 November 2026

An entry for the make.fun bounty [Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124): one 1024×1024 image that sums up Tuesday 24 November 2026 in 32 stories — 12 illustrated leads, a map with numbered pins, and 20 more briefs. An AI judge compares the images pairwise; the 50 highest-ranked entries share $100.

## The day in one image

**Leads 1–12:** Jensen Huang reinstated as Nvidia CEO (shares +31%); markets roar back on his return (S&P +4.7%, Nikkei +3.9%); Trump puts the Iran strike on hold until January; Russian jets enter South Korea's air defense zone; Zelensky warns of new Russian strikes and urges four-way talks; Ukraine sinks a Russian warship off Libya; the US blacklists Megaspeed in the Nvidia spy scandal; COP31 fallout — the "worst COP ever"; Commanders stun the Bengals 22–20 on Monday Night Football; Indonesia charges an ex-police chief with treason; Bangladesh vaccinates 50 million children against typhoid; the EU seeks a new ECB chief as Lagarde resigns.

**Briefs 13–32:** Virginia & Oregon sue SpaceX over Grok imagery; SoftBank to invest $2bn in Intel; Indian Army hunts scores missing after a Himalayan flood; ex-Indian MP Revanna jailed for life for rape; Thai–Cambodia border fighting on hold after a truce; US reveals a new citizenship test and H-1B changes; Trump announces a Japan trade deal; Trump–Indonesia deal, EU threatens $84bn tariffs; two die in a US university shooting; two Nigerians die serving in the Russian military; Sahel states restart talks with the West Africa bloc; Kenya secures 293,600 jobs in Saudi Arabia; South Africans vote as the ANC faces discontent; DRC's Tshisekedi enacts constitutional reform; RSF drones hit Sudan power plants; Tanzania opposition official charged with treason; Kenya discharges its last Ebola patient as the DRC toll tops 5,300; Israeli strikes kill 3 in Gaza, incl. an UNRWA worker; Mexico to try "El Chapo Isidro" at home; Norway court voids disputed oil licences.

All 32 stories were verified against real outlets on 24 November 2026. Sources: Reuters · CNN · Associated Press · The Times · CNBC · Wall Street Journal · USA Today · New York Post.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` byte-for-byte to the output directory. It uses no network, no clock, and no files outside this repository, so repeated runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`out/entry.png` is then byte-for-byte this directory's `entry.png`.

## Design

A clean newspaper front page in the restrained palette the 23 November edition settled on: navy masthead with a gold rule, off-white paper, one red accent, flat pictogram icons in the lead cards, and a flat vector world map with numbered red pins and a legend.
