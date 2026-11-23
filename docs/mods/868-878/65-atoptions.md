---
title: "AnyTone Options software download"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#ATOptions
tags: [AT-D868UV, AT-D878UV]
---

# AnyTone Options software download

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#ATOptions)

Colin G4EML has created an application called AT Options, which will allow you to enable the full test mode, enable a programming password (more about this in [Programming password lock](67-password.md)) and to edit other text such as the dealer you purchased your radio from, or any maintenance notes you might like to add. For example, you can enter your name, phone number and callsign in this text area in case you ever misplace your radio.

Download Colin G4EML **AT Options version 8 (17kb) software** from:

- [Download from this webpage here](../../originals/anytonetechzone/AT_Options_v8.zip)
- [Download via Mega](https://mega.nz/file/HxVUTbbI#zUdyTNjXF1gOdanSrRALbWiajamGf6Yey_Gcn2z-wqM)
- [Download via Google Drive](https://drive.google.com/file/d/1zRj035TWc_1y3VavoLrgUmdsoBGGTF_A/view?usp=sharing)
- [Download via Sabercat host](https://sabercathost.com/a1gd/AT_Options_v8.zip)

!!! warning
    As always, this software is provided without any warranties, and you use it entirely at your own risk. Using this application to write any changes to your radio is also likely to invalidate the manufacturer's warranty.

The application is suitable for the AnyTone 878, 878-II, 868, AnyTone 578 of all flavours, Btech 6X2, Alinco DJ-MD5 & DJ-MD5X, Alinco DR-MD500 & DR-MD520 of all flavours, but **not** the Radioddity GD-AT10G at this stage.

## Using AT Options

!!! warning
    Ensure that you do not have any power on password active. If you do, you must use the CPS software to remove it first. Use of AT Options while a power on password is active can, under certain circumstances, cause some data to be overwritten with default data.

1. When you run the software, select your Com port and **Read** from the radio.
2. Then edit any text fields you may want, and make sure the Band Select and Full Test Mode check boxes are ticked.
3. Finally, **Write** the settings back to the radio – this only takes a fraction of a second to do, and the radio will reboot. It may take a few extra seconds more than normal to boot up; this is OK as it is reconfiguring internal memory.

## Test mode

To activate test mode, turn off the radio, hold down the **PTT** + keypad **1** buttons until TEST MODE is displayed on the radio screen, then let the two buttons go. The radio will boot up into its full test / self adjustment mode.

Once you start test mode, scroll up and down between different test adjustment points using the zone up/down button. The following adjustments are available:

!!! warning
    I strongly recommend you go through each setting and write down what they are before making any adjustments.

| CH | 868 Setting | Adj. range | 868 Description | 878 / 6X2 Setting | Adj. range | 878 / 6X2 Description |
|---|---|---|---|---|---|---|
| 1 | nil | nil | Low UHF test frequency | nil | nil | Low UHF test frequency |
| 2 | nil | nil | Mid UHF test frequency | nil | nil | Mid UHF test frequency |
| 3 | nil | nil | High UHF test frequency | nil | nil | High UHF test frequency |
| 4 | nil | nil | Low VHF test frequency | nil | nil | Low VHF test frequency |
| 5 | nil | nil | Mid VHF test frequency | nil | nil | Mid VHF test frequency |
| 6 | nil | nil | High VHF test frequency | nil | nil | High VHF test frequency |
| 7 | FQCU | 0-65535 | Frequency fine tune | FQCU | 0-65535 | Frequency fine tune |
| 8 | PAHU | 0-255 | UHF RF power output turbo setting | PATU | 0-255 | UHF RF power output turbo setting |
| 9 | PAMU | 0-255 | UHF RF power output high setting | PAHU | 0-255 | UHF RF power output high setting |
| 10 | PALU | 0-255 | UHF RF power output medium setting | PAMU | 0-255 | UHF RF power output medium setting |
| 11 | PASU | 0-255 | UHF RF power output low setting | PALU | 0-255 | UHF RF power output low setting |
| 12 | MODU | 0-255 | Overall deviation setting for both UHF & VHF (value copied to 39 below) | MODU | 0-255 | Overall deviation setting for both UHF & VHF (value copied to 40 below) |
| 13 | TONEU | nil | Push PTT to transmit a test 1000 Hz tone on a UHF FM frequency | TONEU | nil | Push PTT to transmit a test 1000 Hz tone on a UHF FM frequency |
| 14 | CTCW | 0-63 | Deviation setting for CTCSS in both UHF & VHF (value copied to 41 below) | CTCW | 0-63 | Deviation setting for CTCSS in both UHF & VHF (value copied to 42 below) |
| 15 | DCSW | 0-63 | Deviation setting for DCS in both UHF & VHF (value copied to 42 below) | DCSW | 0-63 | Deviation setting for DCS in both UHF & VHF (value copied to 43 below) |
| 16 | RXVLU | 0-4095 | UHF receive tracking gain, low end of band | RXVLU | 0-4095 | UHF receive tracking gain, low end of band |
| 17 | RXVMU | 0-4095 | UHF receive tracking gain, mid band | RXVMU | 0-4095 | UHF receive tracking gain, mid band |
| 18 | RXVHU | 0-4095 | UHF receive tracking gain, top end of band | RXVHU | 0-4095 | UHF receive tracking gain, top end of band |
| 19 | SQTHU | 60-134 | UHF squelch threshold | SQTHU | 60-134 | UHF squelch threshold |
| 20 | RSSIU | nil | UHF RSSI, inject RF at desired level for 1 bar reading, rotate top dial to sample and lock in value | RSSIU | nil | UHF RSSI, inject RF at desired level for 1 bar reading, rotate top dial to sample and lock in value |
| 21 | A OBHU | 0-65535 | not yet known, but seems to adjust screen brightness (suspect this is a bug) | A OBHU | 0-65535 | not yet known |
| 22 | A OBLU | 0-65535 | not yet known | A OBLU | 0-65535 | not yet known |
| 23 | D OBHU | 0-65535 | not yet known, unable to adjust from test menu | D OBHU | 0-65535 | not yet known |
| 24 | D OBLU | 0-65535 | not yet known, unable to adjust from test menu | D OBLU | 0-65535 | not yet known |
| 25 | D CTCW | 0-65535 | CTCSS deviation level in A+D mode | D CTCW | 0-65535 | CTCSS deviation level in A+D mode |
| 26 | D DCSW | 0-65535 | DCS deviation level in A+D mode | D DCSW | 0-65535 | DCS deviation level in A+D mode |
| 27 | DIGIU FSKL | nil | Push PTT to send test FSK signal (heard as 2400 Hz) at low end of UHF band | DIGIU FSKL | nil | Push PTT to send test FSK signal (heard as 2400 Hz) at low end of UHF band |
| 28 | DIGIU FSKM | nil | Push PTT to send test FSK signal (heard as 2400 Hz) at mid UHF band | DIGIU FSKM | nil | Push PTT to send test FSK signal (heard as 2400 Hz) at mid UHF band |
| 29 | DIGIU FSKH | nil | Push PTT to send test FSK signal (heard as 2400 Hz) at high end of UHF band | DIGIU FSKH | nil | Push PTT to send test FSK signal (heard as 2400 Hz) at high end of UHF band |
| 30 | DIGIU 600Hz | nil | Push PTT to send test 600Hz signal UHF band (heard on FM as 200 & 400 Hz?) | DIGIU 600Hz | nil | Push PTT to send test 600Hz signal UHF band (heard on FM as 200 & 400 Hz?) |
| 31 | DIGIU 300Hz | nil | Push PTT to send test 300Hz signal UHF band (heard on FM as 800 Hz?) | DIGIU 300Hz | nil | Push PTT to send test 300Hz signal UHF band (heard on FM as 800 Hz?) |
| 32 | DIGIU 1031 | nil | Push PTT to send test signal UHF band, heard on DMR as 1031 Hz | DIGIU 1031 | nil | Push PTT to send test signal UHF band, heard on DMR as 1031 Hz |
| 33 | DIGIU BER | nil | Display received BER of DMR test signal | DIGIU BER | nil | Display received BER of DMR test signal |
| 34 | DIGIU TEST | nil | Test UHF DMR for both TX & RX as if it were on a regular DMR channel | DIGIU TEST | nil | Test UHF DMR for both TX & RX as if it were on a regular DMR channel |
| 35 | PAHV | 0-255 | VHF RF power output turbo setting | PATV | 0-255 | VHF RF power output turbo setting |
| 36 | PAMV | 0-255 | VHF RF power output high setting | PAHV | 0-255 | VHF RF power output high setting |
| 37 | PALV | 0-255 | VHF RF power output medium setting | PAMV | 0-255 | VHF RF power output medium setting |
| 38 | PASV | 0-255 | VHF RF power output low setting | PALV | 0-255 | VHF RF power output low setting |
| 39 | MODV | 0-255 | Overall deviation setting for both VHF & UHF (value copied to 12 above) | PAMV_2 | 0-255 | 222 MHz RF power output medium setting |
| 40 | TONEV | nil | Push PTT to transmit a test 1000 Hz tone on a VHF FM frequency | MODV | 0-255 | Overall deviation setting for both VHF & UHF (value copied to 12 above) |
| 41 | CTCWV | 0-63 | Deviation setting for CTCSS in both UHF & VHF (value copied to 14 above) | TONEV | nil | Push PTT to transmit a test 1000 Hz tone on a VHF FM frequency |
| 42 | DCSWV | 0-63 | Deviation setting for DCS in both UHF & VHF (value copied to 15 above) | CTCWV | 0-63 | Deviation setting for CTCSS in both UHF & VHF (value copied to 14 above) |
| 43 | RXVLV | 0-4095 | VHF receive tracking gain, low end of band | DCSWV | 0-63 | Deviation setting for DCS in both UHF & VHF (value copied to 15 above) |
| 44 | RXVMV | 0-4095 | VHF receive tracking gain, mid band | RXVLV | 0-4095 | VHF receive tracking gain, low end of band |
| 45 | RXVHV | 0-4095 | VHF receive tracking gain, top end of band | RXVMV | 0-4095 | VHF receive tracking gain, mid band |
| 46 | SQTHV | 60-134 | VHF squelch threshold | RXVHV | 0-4095 | VHF receive tracking gain, top end of band |
| 47 | RSSIV | nil | VHF RSSI, inject RF at desired level for 1 bar reading, rotate top dial to sample and lock in value | SQTHV | 60-134 | VHF squelch threshold |
| 48 | A OBHV | 0-65535 | not yet known | RSSIV | nil | VHF RSSI, inject RF at desired level for 1 bar reading, rotate top dial to sample and lock in value |
| 49 | A OBLV | 0-65535 | not yet known | A OBHV | 0-65535 | not yet known |
| 50 | D OBHV | 0-65535 | not yet known | A OBLV | 0-65535 | not yet known |
| 51 | D OBLV | 0-65535 | not yet known | D OBHV | 0-65535 | not yet known |
| 52 | DIGIV FSKL | nil | Push PTT to send test FSK signal (heard as 2400 Hz) at low end of VHF band | D OBLV | 0-65535 | not yet known |
| 53 | DIGIV FSKM | nil | Push PTT to send test FSK signal (heard as 2400 Hz) at mid VHF band | DIGIV FSKL | nil | Push PTT to send test FSK signal (heard as 2400 Hz) at low end of VHF band |
| 54 | DIGIV FSKH | nil | Push PTT to send test FSK signal (heard as 2400 Hz) at high end of VHF band | DIGIV FSKM | nil | Push PTT to send test FSK signal (heard as 2400 Hz) at mid VHF band |
| 55 | DIGIV 600Hz | nil | Push PTT to send test 600Hz signal VHF band (heard on FM as 200 & 400 Hz?) | DIGIV FSKH | nil | Push PTT to send test FSK signal (heard as 2400 Hz) at high end of VHF band |
| 56 | DIGIV 300Hz | nil | Push PTT to send test 300Hz signal VHF band (heard on FM as 800 Hz?) | DIGIV FSKH2 | nil | Push PTT to send test FSK signal (heard as 2400 Hz) at 222 MHz band |
| 57 | DIGIV 1031 | nil | Push PTT to send test signal VHF band, heard on DMR as 1031 Hz | DIGIV 600Hz | nil | Push PTT to send test 600Hz signal VHF band (heard on FM as 200 & 400 Hz?) |
| 58 | DIGIV BER | nil | Display received BER of DMR test signal | DIGIV 300Hz | nil | Push PTT to send test 300Hz signal VHF band (heard on FM as 800 Hz?) |
| 59 | DIGIV TEST | nil | Test VHF DMR for both TX & RX as if it were on a regular DMR channel | DIGIV 1031 | nil | Push PTT to send test signal VHF band, heard on DMR as 1031 Hz |
| 60 | VBAT | 0-200 | Calibrate displayed voltage of battery | DIGIV BER | nil | Display received BER of DMR test signal |
| 61 | MODE | 0-12 | Changes operational frequency bands of radio | DIGIV TEST | nil | Test VHF DMR for both TX & RX as if it were on a regular DMR channel |
| 62 | 087.50M | nil | Receiver test of FM broadcast band | VBAT | 0-200 | Calibrate displayed voltage of battery |
| 63 | 097.50M | nil | Receiver test of FM broadcast band | F1 ParaA0 | 0-65535 | Hex BCD combined mic gain & mic AGC values at 65 & 66 below, changing has no effect |
| 64 | 108.00M | nil | Receiver test of FM broadcast band | REG0 | 0-FFFF | If set correctly will copy 32 bytes of firmware to memory just above RF cal data, use unknown |
| 65 |  |  |  | MIC | 0-95 | Microphone gain, but does not appear to have any effect |
| 66 |  |  |  | AGC | 0-95 | Microphone dynamic auto gain for DMR, but does not appear to have any effect |
| 67 |  |  |  | MODE | 0-17 | Changes operational frequency bands of radio |
| 68 |  |  |  | 087.50M | nil | Receiver test of FM broadcast band |
| 69 |  |  |  | 097.50M | nil | Receiver test of FM broadcast band |
| 70 |  |  |  | 108.00M | nil | Receiver test of FM broadcast band |

For the squelch threshold values, a higher value gives a more sensitive squelch. Typically little to no improvement in squelch sensitivity is obtained with values higher than about 115, but some users have reported improvement with higher values. Lower values require progressively stronger signals to open the squelch.

The RSSI (received signal strength indicator – in other words the signal meter) has a fairly compressed range of 15dB. I'd have preferred to see at least 30dB range in the signal meter, but I've found an acceptable compromise has been to set one bar at -113dBm, which equates to values of RSSIU of 36 and RSSIV of 39. The signal meter then reads:

| Bars | Level |
|---|---|
| 1 bar | -113 dBm or about S-5 |
| 2 bars | -108 dBm or about S-6 |
| 3 bars | -103 dBm or about S-7 |
| 4 bars | -98 dBm or about S-9 |

## When you have finished

Once finished changing your values, turn the radio off and on again to save them to memory. If you like, you can disable full test mode again by de-selecting the Full Test Mode check box in the AT Options application and writing back to the radio. Or, you can de-select both Full Test Mode and Band Select check boxes, which will totally inhibit test mode completely. The values you changed or adjusted will not be erased by doing this; it simply prevents you from accessing the full test mode and inadvertently changing them again. These values will not be overwritten, changed or restored to default by resetting of the radio. Once you change them, you can not get the original value back unless you wrote it down before making adjustments.

!!! warning
    Finally, as you go through the adjustment values, it becomes apparent that the 878 (only) has adjustments for the 222 MHz band. Do not attempt to use these radios on that band for TX as the hardware is not designed for it.
