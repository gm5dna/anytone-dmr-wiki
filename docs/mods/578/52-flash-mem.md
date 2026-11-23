---
title: "Flash memory structure in the 578"
source_url: https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#FlashMem
tags: [AT-D578UV]
---

[← All 578 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, unchanged, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#FlashMem)

**Flash memory structure in the 578**
The 578 is fitted with a 2 Gbit / 256 Mbyte external flash memory, and the MCU has 3 Mbyte of internal flash memory that holds the operating firmware.
Here’s what is known about the structure of memory in these radios so far:

**578 Toshiba TC58CVG1S3HRAIG 2Gbit / 256 Mbyte NAND external flash memory map**

|  |  |
|----|----|
| Address in flash | Contents |
| 0x00000000 to 0x0014FFFF | holds alternate language fonts e.g. Chinese, Japanese, Greek, Cyrillic, Roman numerals. There is some English font there but it doesn’t appear to be used at all |
| 0x00150000 to 0x00159FFF | default AnyTone start-up picture |
| 0x0015A000 to 0x001FFFFF | multi colour icons bitmaps |
| 0x003E0000 to 0x0041FFFF | unknown data |
| 0x00420000 to 0x00434FFF | more multi colour icons bitmaps |
| 0x00435000 to 0x0043BFFF | monochrome fonts, possibly not used |
| 0x00800000 to 0x02A9FFFF | codeplug data (not including DMR IDs) |
| 0x02AC0000 to 0x02AC9FFF | custom start up image bitmap |
| 0x02B00000 to 0x02B09FFF | background display image bitmap BK1 |
| 0x02B80000 to 0x02B89FFF | background display image bitmap BK2 |
| 0x02F00000 to 0x02F80679 | active RF ’soft’ alignment data and backup copies |
| 0x02FA0000 to 0x02FDFFFF | active ’local information’ radio configuration data and backup copy |
| 0x02FE0000 to 0x03000000 | unknown data |
| 0x05500000 to (likely) 0x07FFFFFF | DMR IDs |
| 0x0C8E0000 to (likely) 0x0FFFFFFF | DMR audio recordings |
