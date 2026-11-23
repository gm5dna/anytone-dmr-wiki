---
title: "General technical information"
source_url: https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#GenTech
tags: [AT-D578UV]
---

# General technical information

[← All 578 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#GenTech)

The 578 uses a hybrid receiver, with a conventional super-heterodyne 1st IF stage using 38.550 and 38.850 MHz Intermediate Frequencies, each followed by a direct conversion IF receiver; this is a design architecture that Motorola and others have used to great success for many years. There is also a relay and substantial diode for reverse polarity protection, and a third IF strip that is unpopulated.

The following devices are found within:

- GD32F303VKT6 ARM Cortex-M4 32 bit MCU with 3072kbyte internal flash and 96kbyte internal SRAM. 578s produced after mid 2022 will use an equivalent AT32F435/437 brand MCU.
- Toshiba TC58CVG1S3HRAIG 2Gbit / 256Mbyte NAND flash memory
- Sicomm CT3258TD baseband processor for DMR with built in AMBE2+ vocoder & 12.2 MHz oscillator
- Texas Instruments TLV320AIC3204 DSP / codec
- 4 x QA4818N transceiver ICs & 26.0 MHz reference oscillators. These devices have the same pinout as the more common AT1846S, but are more capable. One pair is being used as the 1st Local Oscillator for VFO-A and VFO-B, and the other pair are acting as a direct conversion 1st IF baseband receiver.
- RDA 5802N FM broadcast band receiver
- YD1517P (LM1517P equivalent) 2x 6 watt audio power amp, working in push-pull mode to give 12 watt output
- Two NXP AFT05MP075N LDMOS 70 watt RF power amps, 18dB narrowband gain, one each for independent VHF & UHF power amp stages
- VHF and UHF receive front ends each have four stages of varactor track tuned filtering
- ATGM336H GPS & BDS (BeiDou) positioning module (GPS models only)
- Battery backup for real time clock, plus a second backup battery for GPS ’hot start’
