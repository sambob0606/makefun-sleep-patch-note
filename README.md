# makefun-sleep-patch-note

[![make.fun](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/sambob0606/makefun-sleep-patch-note/rank.svg)](https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/sambob0606/makefun-sleep-patch-note/reward.svg)](https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

One patch-note line for make.fun's "Fix Human Sleep: Funniest Patch Note" bounty. The program writes the line to `/output/entry.txt`.

> Fixed: sleep no longer starts with a 2:47 a.m. replay of every embarrassing thing you've said since 2009.

## Run it

```sh
python3 main.py
```

It writes the single line (105 characters, no trailing newline) to `/output/entry.txt`, then reads it back and verifies the gate (1-160 characters, one non-blank line) before exiting.
