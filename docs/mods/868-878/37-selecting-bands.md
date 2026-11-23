---
title: "Selecting operational bands"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#SelectingBands
tags: [AT-D868UV, AT-D878UV]
---

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, unchanged, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#SelectingBands)

**Selecting operational bands**
There are many different choices of bands that you can select to use, depending on your radio type & firmware version.

*Note that whenever you do change MODE, the radio will reset and you will lose your programmed data. Make sure you have a saved copy of your codeplug. Each saved codeplug will have the MODE it was created under encoded within it. If you try to reload the same codeplug after changing MODE, the CPS software will reject it, saying that it is the wrong band. To fix this, you will need to 'hex edit' the codeplug rdt file: change byte 0x0011 to match the MODE selected. For example, if you set MODE=00002 then edit your codeplug byte 0x0011 to be hex value 02. Or if you set MODE=00010 then set codeplug byte 0x0011 to hex value 0A.*
Note- there is a bug in the CPS programming software: Local Information will not show the correct frequency band the radio is set to, but Model \> Model Information does show the correct frequency band

Begin by turning the radio off, then press and hold the PTT and 1 buttons while turning on the radio, hold those two buttons until you see 'TEST MODE' appear on screen. After releasing the buttons the radio will start up with the text 'MODE:00000' to the bottom of the screen
*If you don't see this screen, you will need to download AT Options software and enable 'Band select' check box & write this back to the radio. See:* *[Download AT Options software](65-atoptions.md)*
Rotate the top dial to change the mode number, which will select the following:

Standard MODES selectable 878, 878-II, 868, Btech 6X2, Alinco DJ-MD5, Alinco DJ-MD5XGP:

|  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|
| MODE | 878 v1.27 & 878-II v2.05 RX | 878 v1.27 & 878-II v2.05 TX | 868 v2.40 RX | 868 v2.40 TX | 6X2 v2.04d RX | 6X2 v2.04d TX | DJ-MD5 v1.13e RX | DJ-MD5 v1.13e TX | DJ-MD5X v1.11 RX | DJ-MD5X v1.11 TX |
| 00000 | 400-480 & 136-174 | 400-480 & 136-174 | 400-480 & 136-174 | 400-480 & 136-174 | 400-480 & 136-174 | 400-480 & 136-174 | 400-480 & 136-174 | 400-480 & 136-174 | 400-480 & 136-174 | 400-480 & 136-174 |
| 00001 | 400-480 & 136-174 (12.5k only) | 400-480 & 136-174 (12.5k only) | 420-450 & 144-148 | 420-450 & 144-148 | 400-480 & 144-146 | 400-480 & 144-146 | 400-480 & 144-146 | 400-480 & 144-146 | 430-440 & 136-174 | 430-440 & 136-174 |
| 00002 | 430-440 & 136-174 | 430-440 & 136-174 | 430-440 & 136-174 | 430-440 & 136-174 | 430-440 & 136-174 | 430-440 & 136-174 | 430-440 & 136-174 | 430-440 & 136-174 | 400-480 & 136-174 | 430-440 & 144-146 |
| 00003 | 400-480 & 136-174 | 430-440 & 144-146 | 430-440 & 144-146 | 430-440 & 144-146 | 430-440 & 144-146 | 430-440 & 144-146 | 430-440 & 144-146 | 430-440 & 144-146 | 440-480 & 136-174 | 440-480 & 136-174 |
| 00004 | 434-438 & 144-146 | 434-438 & 144-146 | 440-480 & 136-174 | 440-480 & 136-174 | 440-480 & 136-174 | 440-480 & 136-174 | 440-480 & 136-174 | 440-480 & 136-174 | 440-480 & 144-146 | 440-480 & 144-146 |
| 00005 | 434-447 & 144-146 | 434-447 & 144-146 | 440-480 & 144-146 | 440-480 & 144-146 | 440-480 & 144-146 | 440-480 & 144-146 | 440-480 & 144-146 | 440-480 & 144-146 | 446-447 & 136-174 | 446-447 & 136-174 |
| 00006 | 446-447 & 136-174 | 446-447 & 136-174 | 446-447 & 136-174 | 446-447 & 136-174 | 446-447 & 136-174 | 446-447 & 136-174 | 446-447 & 136-174 | 446-447 & 136-174 | 400-480 & 136-174 | 420-450 & 144-148 |
| 00007 | 400-480 & 136-174 | 420-450 & 144-148 | 446-447 & 144-146 | 446-447 & 144-146 | 446-447 & 144-146 | 446-447 & 144-146 | 446-447 & 144-146 | 446-447 & 144-146 | 400-470 & 136-174 | 400-470 & 136-174 |
| 00008 | 400-470 & 136-174 | 400-470 & 136-174 | 400-470 & 136-174 | 400-470 & 136-174 | 400-470 & 136-174 | 400-470 & 136-174 | 400-470 & 136-174 | 400-470 & 136-174 | 430-432 & 144-146 | 430-432 & 144-146 |
| 00009 | 430-432 & 144-146 | 430-432 & 144-146 | 430-432 & 144-146 | 430-432 & 144-146 | 430-432 & 144-146 | 430-432 & 144-146 | 430-432 & 144-146 | 430-432 & 144-146 | 400-480 & 136-174 | 430-450 & 144-148 |
| 00010 | 400-480 & 136-174 | 430-450 & 144-148 | 400-480 & 136-174 | 430-450 & 144-148 | 400-480 & 136-174 | 430-450 & 144-148 | 400-480 & 136-174 | 420-450 & 144-148 | 400-520 & 136-174 | 400-520 & 136-174 |
| 00011 | 400-520 & 136-174 | 400-520 & 136-174 | 400-480 & 136-174 | 430-440 & 144-146 | 400-480 & 136-174 | 430-440 & 144-146 | 430-440 & 144-148 | 430-440 & 144-148 | 400-490 & 136-174 | 400-490 & 136-174 |
| 00012 | 400-490 & 136-174 | 400-490 & 136-174 | 403-470 & 136-174 | 403-470 & 136-174 | 403-470 & 136-174 | 403-470 & 136-174 | 405-415 & 136-174 | 405-415 & 136-174 | 400-480 & 136-174 | 403-470 & 136-174 |
| 00013 | 400-480 & 136-174 | 403-470 & 136-174 |  |  |  |  |  |  | 400-520 & 220-225 & 136-174 | 400-520 & 220-225 & 136-174 |
| 00014\* | 400-520 & 220-225 & 136-174 | 400-520 & 220-225 & 136-174 |  |  |  |  |  |  | 420-520 & 220-225 & 144-148 | 420-520 & 220-225 & 144-148 |
| 00015 | 420-520 & 144-148 | 420-520 & 144-148 |  |  |  |  |  |  | 430-440 & 144-147 | 430-440 & 144-147 |
| 00016 | 430-440 & 144-147 | 430-440 & 144-147 |  |  |  |  |  |  | 430-440 & 136-174 | 136-174 only |
| 00017 | 430-440 & 136-174 | 136-174 only |  |  |  |  |  |  |  |  |

\* MODE 14 is not directly selectable on recent 878 firmware versions, you first need to enter a password to enable this band. When MODE and the band number is displayed, press any number on the keypad and the radio will ask "INPUT PASSWORD:" if you happen to know what this password is, enter it, and then you should be able to select MODE 00014.

Then turn off the radio, which will save your selected mode setting, and from that point on, your radio will use the frequency limits that correspond with the mode setting you selected. You can repeat the process to change MODES at any time.
If using AT Options to set the band, this software will automatically do what is necessary to enable MODE 00014, knowledge of the password is not needed.
Note- there is a bug in the CPS programming software: Local Information will not show the correct frequency band the radio is set to, but Model \> Model Information does show the correct frequency band
Starting with firmware V1.11 on the 878, fewer MODE options were available to select due to FCC rules governing the sale of radios. This doesn't mean those other MODES are not actually gone, they're just not able to be selected. You can use AT Options application to select one of these hidden bands.

***I will not be sharing the password for MODE 00014 under any circumstances, as the FCC is starting to closely scrutinise these matters and we don't want them to revoke the approval status for these wonderful radios, which would result in the AnyTone radios being withdrawn from sale, then nobody would be able to enjoy them.***
For the vast majority of users, there is no need to use MODE 00014 anyway. The alternate firmware files available at [expanded RX frequencies with alternate firmware](49-expand-rx.md) will permit reception of the 220 MHz band under any MODE selection, making MODE 00014 redundant.

------------------------------------------------------------------------
