---
title: "Flash memory structure in the 868 / 6X2 / 878"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#FlashMem
tags: [AT-D868UV, AT-D878UV]
---

# Flash memory structure in the 868 / 6X2 / 878

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#FlashMem)

The 868 / 878 / 6X2 is fitted with a 1 Gbit / 128 Mbyte external flash memory, and depending on what version of hardware, and type of MCU is fitted, the MCU has either 512 kbyte or 1 Mbyte of internal flash memory that holds the operating firmware.

Here's what is known about the structure of memory in these radios so far:

- 0x00000000 to 0x07FFFFFF is mapped to external flash memory chip; and
- 0x08000000 to 0x080FFFFF is mapped to MCU internal flash memory.

## 868 / 6X2 / 878 Toshiba TC58CVG0S3HRAIG 1Gbit / 128Mbyte NAND external flash memory map

| Address in flash | Contents |
|---|---|
| 0x00000000 to 0x0014FFFF | holds alternate language fonts e.g. Chinese, Japanese, Greek, Cyrillic, Roman numerals. There is some English font there but it doesn't appear to be used at all |
| 0x00150000 to 0x00159FFF | default AnyTone start-up picture |
| 0x0015A000 to 0x001FFFFF | multi colour icons bitmaps |
| 0x003E0000 to 0x0041FFFF | unknown data |
| 0x00420000 to 0x0043BFFF | more multi colour icons bitmaps |
| 0x00800000 to 0x02EFFFFF | codeplug data |
| 0x02F00000 to 0x02F8061F | active RF 'soft' alignment data and backup copies |
| 0x02FA0000 to 0x02FDFFFF | active 'local information' radio configuration data and backup copy |
| 0x042C0000 to 0x042C9FFF | custom start up image bitmap |
| 0x04300000 to 0x04309FFF | background display image bitmap (878 only, unused in 868 / 6X2) |
| 0x04500000 to (likely) 0x06BFFFFF | DMR ID database, with other support data being written around 0x04000000 |
| 0x06D00000 to (likely) 0x07FFFFFF | DMR audio recordings |

## MCU internal flash memory

0x08000000 to 0x080FFFFF is mapped to GD32F303VE or GD32F303VG MCU internal flash memory:

- 0x08000000 to 0x08003FFF used by the AnyTone custom boot loader for firmware updating etc.
- 0x08004000 to 0x0807FFFF used by firmware and display fonts
- 0x08080000 to 0x080FFFFF is only available on hardware fitted with GD32F303VG (1024k) MCUs, and is empty on 868s, used by firmware on 878s.
