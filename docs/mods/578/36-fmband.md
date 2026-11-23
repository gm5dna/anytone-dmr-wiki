---
title: "Expanding FM band frequencies 76 to 120 MHz"
source_url: https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#FMBand
tags: [AT-D578UV]
---

# Expanding FM band frequencies 76 to 120 MHz

[← All 578 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#FMBand)

*Difficulty: Easy*

The present firmware version only permits FM band VFO tuning from 87.5 to 108 MHz. The software however, permits entry of frequencies from 76.0 to 108.0 MHz for memories in the FM band. This is the easiest way to get the 578 to tune down to 76 MHz – put those frequencies into a FM band memory channel.

Tuning below 76 MHz isn’t possible at this stage as the RDA 5802 needs to be set up differently to go below 76 MHz. But going up past 108 MHz is possible – though I’m not sure why you’d want to. Reception of air band transmissions using wideband FM, even with a very strong AM signal, is impossible. But, if you have the need to, I found that my 578 was able to receive test signals all the way up to 120 MHz.

Entering such frequencies is quite easy:

1. Enter some ’dummy’ channels.
2. Using the **Tool → Export** menu in the CPS programming software, export your FM channels and open the file with Notepad for editing.
3. Change the frequencies of the dummy channels you entered and save the file.
4. Use the **Tool → Import** menu in the CPS programming software to import your edited file.

This way you can enter any FM frequency, in 50 kHz steps, between 76.00 and 120.00 MHz. You can edit and import frequencies outside these limits, but the receiver won’t actually work properly beyond those limits.
