---
title: "Writing your own .CDD files Advanced"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#CDD
tags: [AT-D868UV, AT-D878UV]
---

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, unchanged, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#CDD)

**Writing your own .CDD files** Advanced
Reading data out of the radio flash memory is easy using Colin's AT Flash Utility software, but if you want to write data, especially to 'critical' areas of flash memory such as anywhere between 0x02F00000 and 0x02FDFFFF, you will need to use a special technique to do this. This involves creating a CDD file and supporting SPI and CDI files, and sending this to the radio in the 'icon update' mode (holding PTT & PF2 buttons on power up). This ensures the radio CPU is halted from normal execution while data is being written, and places the radio in a safe mode to permit data to be written. The CDD file is simply a binary image of the data you wish to write - nothing out of the ordinary there. There are three rules you need to follow:

- You must ensure your CDD file is 256kbyte or some multiple of that size
- You must ensure that your data to be written starts at a 256kbyte page eg: hex addresses 00040000, 00080000, 000C0000, 00100000, 00140000 etc.
- And then lastly, you will write this data with an offset of (hex) 20000 bytes above the intended actual location you wish to write to.

Example: you wish to write 256kbytes of data to 0x02F40000. First determine if this is the start of a 256k page. 0x02F40000 is evenly divisible by 040000 (256k) so that is good. Then specify for data to be written with a 128k (hex 20000) offset, so writing should begin at address 0x02F60000, and the data you write will actually go to 0x02F40000.

It is the SPI and CDI support files that tell the radio where to write this data, and how that should be done that is the slightly tricky bit.

SPI format:
20 00 00 00
(number of sections to load in hex)
00
(4 bytes of CDD file length in bytes, little endian)
00 00 00 00


CDI format:
(name of original .bin file followed by 00 then padded out to 256 bytes with 20)
(4 bytes of the starting write address to the radio, little endian - note you need to apply a 0x020000 offset as detailed just above)
(4 bytes of number of bytes to write, little endian)
(4 bytes of the starting point address in the CDD file to begin writing from, little endian)
00 00 01 00
00 00 00 00 00 00
\[next record of another section to write, if applicable\]
\[and so on...\]

------------------------------------------------------------------------
