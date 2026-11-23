---
title: "Preventing your radio from freezing or locking up and how to cure many problems"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#Prevent
tags: [AT-D868UV, AT-D878UV]
---

# Preventing your radio from freezing or locking up and how to cure many problems

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#Prevent)

There are some things that can help prevent your radio from freezing or locking up in the first place. The same ideas can also cure many strange problems, e.g. scan speed slowing down, unattended transmit, laggy behaviour, features not working as they should etc.

Follow these suggestions, in this order:

## Rule 1: Rebuild your codeplug

99.9% of problems are caused by residual data in a codeplug file. Rebuilding your codeplug with clean data can help with many miscellaneous problems and eliminate lock ups or freezing. Do not take any shortcuts with this process! Yes, it does take a little bit of effort on your part, but as mentioned, the vast majority of issues are fixed with a rebuilt codeplug.

1. First make sure your CPS software version matches the firmware version presently in your radio.
2. In CPS, load your existing configuration codeplug and export everything (**CPS → Tool → Export → Export All**).
3. Go through all your Optional Setting and write them down or take screen shots of all the settings there. If you are using encryption, also record all your encryption keys. These settings and encryption keys are not saved by the Export All process.
4. **Reset the radio** – this step is very important! If you do not do this, the old & possibly problematic data in the radio is not removed.
5. In CPS, read from the freshly reset radio (yes, you are reading a 'blank' radio, that is OK).
6. Import everything saved from step 1.
7. Finish off your codeplug by attending to the Optional Setting & encryption keys if applicable and confirm all is correct.
8. Send the freshly rebuilt codeplug to the radio.
9. If you had a custom start up picture or background pictures, send those to the radio now.
10. Save the rebuilt codeplug and ensure you use this saved file as the basis for any further changes you may make, and make sure you delete your old problematic codeplug file.
11. Ensure you rebuild your codeplug using these steps **every** time a firmware update is made.

!!! warning
    A codeplug built using last version's CPS will sort of work with a new firmware version, but this mis-match in versions is frequently the cause of many problems. Always ensure you rebuild your codeplug with a CPS version that matches with the firmware version you are using in the radio!

## Rule 2: Turn off GPS

If you are not using GPS to send your location via APRS, turn it off. Even with GPS on just in the background but not sending any APRS positioning, the GPS positioning data being sent to the radio processor adds to its processing load.

## Rule 3: Turn off Roaming

Roaming adds significant load to the radio processor, and if you really don't need it, turn it off.

!!! warning
    **Never** turn on GPS and roaming at the same time – that is just too much for the processor to handle at the same time.

## Rule 4: Make use of the Data ACK disable feature

If you find the radio locks up whenever it is on a certain channel or frequency, it could be reception of non-standard DMR TierII data that is the cause. When the baseband processor encounters this non-standard data, it doesn't know how to handle it, and can cause the radio to lock up as a result. This can be set in CPS for your problem channels (including the VFOs all the way down the bottom of the channel list), or can also be set by the radio menu selections: **Menu → Settings → Chan Set → DataAck Forbid → On**.

## Rule 5: Turn off power save

Power save features have been known to cause issues from time to time as well, so unless you really need to squeeze out every last drop of battery life – which is already very good anyway – leave power save features off.

## Rule 6: Do not use Sub-Channel unless necessary

Unless you really need it, keep the Sub-Channel turned off.

If you follow these six golden rules, you should never have a lockup or freeze of your radio. I've been using my 868 & 878 for over two years now, and have never once had a freeze.
