---
title: "Flash Utility software"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#FlashUtility
tags: [AT-D868UV, AT-D878UV]
---

# Flash Utility software

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#FlashUtility)

Courtesy of Colin G4EML comes this small utility program that can read and write the *external* 1Gbit flash memory where the codeplug, DMR ID database, RF alignment data etc. lives.

There are some rules to the safe use of this software:

- Reading the flash is perfectly safe, it is the writing of data that you need to be careful with.
- Through careless use when writing data, this software can most definitely 'brick' or disable your radio, or cause hardware damage by writing RF output power values to destructively high levels for example. You accept all risk in use of the software.
- The radio will attempt to prevent overwriting of critical data in certain areas of the flash memory, typically stored between addresses 02F00000 and 02FDFFFF. It is generally better to create a set of CDD, CDI and SPI files to write to this area of memory, and write using icon update mode to ensure the radio MCU is safely halted.
- If using Flash Utility to write to the flash memory you need to apply a (hex) 20000 byte offset. For example, if you want to write to address 00000000 you should instruct Flash Utility to begin writing at 00020000. It is unknown why this is necessary, and exactly at what memory address this offset is no longer needed, but it applies at least as high as address (hex) 04000000.
- You should write to the radio in multiples of 256kbytes, even if you only want to change just one byte. (Do not forget the 128k offset that needs to be applied.) This restriction doesn't exist when only reading the flash.

!!! warning
    I **strongly** recommend you make a backup of your flash memory contents by reading at least the critical memory area between addresses 02F00000 and 02FDFFFF and saving to a file, and keep that file in a safe location. You can read the entire flash contents from 00000000 to 07FFFFFF if you wish, but this will take several hours to read a 1Gbit flash memory via a serial interface.

Download **Flash Utility software (10kb)** from:

- [Download from this webpage here](../../originals/anytonetechzone/AT_Flash_Utility_v3.zip)
- [Download via Mega](https://mega.nz/file/v1tVHYIT#r1i82DLy-XRwDGsNnqkcSj2ClME1KvsE2Qr3YaqPFps)
- [Download via Google Drive](https://drive.google.com/file/d/1mV4L8xQSz9GRImEwtNsgjpByWZ_h1MFx/view?usp=sharing)
- [Download via Sabercat host](https://sabercathost.com/e85c/AT_Flash_Utility_v3.zip)

Flash Utility is compatible with the 868, 878 & 6X2. When reading from the radio, it might be a bit confusing to users to have to specify a file before reading begins – this is the file you will be saving your read results to.
