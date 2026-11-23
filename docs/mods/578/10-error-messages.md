---
title: "Strange error messages"
source_url: https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#ErrorMessages
tags: [AT-D578UV]
---

[← All 578 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, unchanged, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#ErrorMessages)

**Strange error messages**

|  |  |
|----|----|
| ![](../../originals/images/578Mods/banderror.jpg) | [Band Error has it’s own section, click here](02-band-error.md) to see five different methods on how to fix this problem. |


[TABLE]


[TABLE]


[TABLE]


|  |  |
|----|----|
| ![](../../originals/images/578Mods/codeplugerror.png) | If you see this error, or something similar to it, this means your codeplug is corrupt. The solution is to reset the radio, [REBUILD](57-prevent.md) your codeplug, and write the rebuilt codeplug to your radio (thanks to Lane KD2TVW for this one) |


|  |  |
|----|----|
| ![](../../originals/images/578Mods/ProgramError.jpg) | This error means your codeplug has become corrupt in memory. All you need do is perform a reset on the radio and reload the codeplug. I also strongly recommend doing a codeplug [REBUILD](57-prevent.md) before reloading it to the radio. |


[TABLE]


[TABLE]


|  |  |
|----|----|
| ![](../../originals/images/578Mods/RTCTryingError.jpg) | This error, or ’RTC ERROR!’ or ’RTC not run!’ means that, for what ever reason, the radio can not read the Real Time Clock. There is a pair of tiny internal batteries, one of which backs up the Real Time Clock and keeps time when the radio is turned off. If that battery becomes too old, or goes faulty, you may see this error. If you continue to ignore this error message and the battery becomes so bad that it short circuits itself, then that could start to induce other new random errors such as the radio freezing up, not accepting any codeplug or firmware updates, and finally becoming completely unresponsive. A short circuit battery will drag down the microprocessor voltage supply, causing these random failures. The RTC backup battery can be replaced by getting access to the bottom side of the PCB and desoldering the old battery and replacing it with a new XH414HG IV01E 3 volt lithium battery. After fitting, a reset of the radio, setting the time & date and reprogramming the codeplug should set everything right. You can find out more information about the little lithium backup batteries [here](45-backup-batteries.md) |


[TABLE]


------------------------------------------------------------------------
