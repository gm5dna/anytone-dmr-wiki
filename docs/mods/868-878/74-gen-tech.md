---
title: "General technical information"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#GenTech
tags: [AT-D868UV, AT-D878UV]
---

# General technical information

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#GenTech)

The 868 / 878 / DMR-6X2 contains the following devices:

- Early 868s: GD32F303VET6 ARM Cortex-M4 32 bit MCU with 512kbyte internal flash and 64kbyte internal SRAM
- Later 868s, 878s and most 6X2: GD32F303VGT6 ARM Cortex-M4 32 bit MCU with 1024kbyte internal flash and 96kbyte internal SRAM
- Toshiba TC58CVG0S3HRAIG 1Gbit / 128Mbyte NAND flash memory
- Sicomm CT3258TD baseband processor for DMR & dPMR with built in AMBE2+ vocoder & 12.2 MHz oscillator
- Texas Instruments TLV320AIC3204 DSP / codec
- AT1846S radio-on-a-chip & 26.0 MHz reference oscillator
- RDA 5802N FM broadcast band receiver
- H&M Semiconductor HM8872 8 watt audio power amp
- Two NXP AFT05MS006NT1 LDMOS 6 watt RF power amps, 18dB narrowband gain, one each for independent VHF & UHF power amp stages
- 2SC3356 based low noise preamps for VHF & UHF receiver stages
- VHF and UHF receive front ends each have four stages of varactor track tuned filtering
- Infineon BGM781N11 GPS front end (GPS models only)
- ATGM336H GPS & BDS (BeiDou) positioning module or Cdtech T3RV1-9600 GPS only module (GPS models only)
- Battery backup for real time clock
- Solder pads for expansion memory SOIC size IC and a small push fit expansion connector for add on Bluetooth or extra memory module. (Not found on the 868 version 1 hardware)
