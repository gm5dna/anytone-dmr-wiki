---
title: "My receive keeps cutting in and out on FM, can that be fixed?"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#popping
tags: [AT-D868UV, AT-D878UV]
---

# My receive keeps cutting in and out on FM, can that be fixed?

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#popping)

Sometimes it has been reported that receive audio keeps cutting in and out, or popping, on FM signals. This is typically a problem for USA users listening to NOAA weather broadcasts. The cutting in and out happens slightly randomly, not at precise & regular intervals.

Other radios are not affected, so is the 878 at fault here? No, everything is fine – what is happening here is the signal you are listening to is deviating too widely for the 878 receiver to handle. Deviation peaks are being clipped by the 878 receiver, causing the audio to cut out briefly. There are a few things you can do:

1. Check that you have the receiver set to wideband FM (radio menus: **Settings → Chan Set → Band width → Wide**) which is the correct mode for listening to most ham activity in the USA and for NOAA signals.
2. Turn STE settings to OFF, particularly the 'STE when no signal' setting (CPS menu: **Optional Setting → STE**).

If the signal still cuts in and out, try disabling the squelch (radio menus: **Settings → Radio Set → Ana Sq Level → Ana SQ OFF**) – if the signal is now OK, it is almost certain that the signal you are listening to is too widely deviated for the 878 receiver to handle. Some NOAA signals are still transmitting with the very old 30 kHz standard deviation, which is too wide for the standard 25 kHz and much too wide for 12.5 kHz.

There are other conditions where the radio receiver may cut in and out too: very complex multipath environment or strong off-frequency or out of band signals can also upset the receiver and mimic this effect. In those instances, a change of antenna or location may help.
