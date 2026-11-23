---
title: "How to reply on an active channel found while scanning"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#TalkbackHint
tags: [AT-D868UV, AT-D878UV]
---

# How to reply on an active channel found while scanning

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#TalkbackHint)

When scan finds an active channel, it is possible to hit the **PTT** button to reply on that active channel found while scanning. Without these settings, the radio will transmit on your default channel, not the channel found during scan, which can cause some embarrassment. You will have to press the **PTT** within 5 seconds of the signal dropping, at which time scanning will resume again (5 seconds is the maximum scan hold time allowable).

1. For each and every scan list you have set up, change these settings as shown:

    ![CPS Scan Edit window with Revert Channel, Dropout Delay Time and Dwell Time circled](../../originals/images/878Mods/talkback.png)

    *Scan Edit: Revert Channel = Selected + TalkBack, Dropout Delay Time[s] = 5.0, Dwell Time[s] = 5.0.*

2. Also make sure your digital call hold times are set to 5 seconds or more:

    ![CPS Optional Setting, Digital Func tab, with Group Call Hold Time and Person Call Hold Time circled](../../originals/images/878Mods/digihold.png)

    *Optional Setting → Digital Func: Group Call Hold Time = 5s, Person Call Hold Time = 5s.*
