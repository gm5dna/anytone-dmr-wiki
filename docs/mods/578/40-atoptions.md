---
title: "Colin G4EML has created an application called AT Options, which will allow you to enable t"
source_url: https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#ATOptions
tags: [AT-D578UV]
---

[← All 578 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, unchanged, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#ATOptions)

Colin G4EML has created an application called AT Options, which will allow you to enable the full test mode, enable a programming password (more about this below) and to edit other text such as the dealer you purchased your radio from, or any maintenance notes you might like to add. For example, you can enter your name, phone number and callsign in this text area in case your radio is stolen.
Download Colin G4EML **AT Options version 8 (17kb) software** from:

- 
- [Download from this webpage here](../../originals/anytonetechzone/AT_Options_v8.zip)
- [Download via Mega](https://mega.nz/file/HxVUTbbI#zUdyTNjXF1gOdanSrRALbWiajamGf6Yey_Gcn2z-wqM)
- [Download via Google Drive](https://drive.google.com/file/d/1zRj035TWc_1y3VavoLrgUmdsoBGGTF_A/view?usp=sharing)
- [Download via Sabercat host](https://sabercathost.com/a1gd/AT_Options_v8.zip)


*\*As always, this software is provided without any warranties, and you use it entirely at your own risk. Using this application to write any changes to your radio is also likely invalidate the manufacturer’s warranty*
(The application is also suitable for the AnyTone 878, 878-II & 868, Btech 6X2, Alinco DJ-MD5 & DJ-MD5X, and Alinco DR-MD500/MD520 - thanks to Jason Alexander for assistance with the Alinco models)

Ensure that you do not have any power on password active. If you do, you must use the CPS software to remove it first. Use of AT Options while a power on password is active can, under certain circumstances, cause some data to be overwritten with default data.
When you run the software, select your COM port and READ from the radio. Then edit any text fields you may want, and make sure Band Select and Full Test Mode check boxes are ticked. Finally, WRITE the settings back to the radio - this only takes a fraction of a second to do, and the radio will reboot. It may take a few extra seconds more than normal to boot up, this is OK as it is reconfiguring internal memory.

To activate test mode, turn off the radio, hold down the P4 and dial buttons while turning on the radio until TEST MODE is displayed on the radio screen (this takes a few seconds to happen), then let the two buttons go. The radio will boot up into it’s full test / self adjustment mode.
Once you start test mode, scroll up and down between different test adjustment points using the zone up/down button. The following adjustments are available:

**I strongly recommend you go through each setting and write down what they are before making any adjustments** \\

|  |  |  |  |  |
|----|----|----|----|----|
|  | 578 Setting | Adj. range | Description | Typical value |
| 1 | UHF AL | nil | A-VFO Low UHF test frequency |  |
| 2 | UHF AM | nil | A-VFO Mid UHF test frequency |  |
| 3 | UHF AH | nil | A-VFO High UHF test frequency |  |
| 4 | VHF AL | nil | A-VFO Low VHF test frequency |  |
| 5 | VHF AM | nil | A-VFO Mid VHF test frequency |  |
| 6 | VHF AH | nil | A-VFO High VHF test frequency |  |
| 7 | UHF BL | nil | B-VFO Low UHF test frequency |  |
| 8 | UHF BM | nil | B-VFO Mid UHF test frequency |  |
| 9 | UHF BH | nil | B-VFO High UHF test frequency |  |
| 10 | VHF BL | nil | B-VFO Low VHF test frequency |  |
| 11 | VHF BM | nil | B-VFO Mid VHF test frequency |  |
| 12 | VHF BH | nil | B-VFO High VHF test frequency |  |
| 13 | FQCA | 0-255 | A-VFO Frequency fine tune | 41 \* |
| 14 | TXDAU | 0-255 | Unknown UHF analogue adjustment | 150 |
| 15 | PAHU | 0-255 | UHF RF power output turbo setting | 180 |
|  |  |  |  |  |
| 16 | PAMU | 0-255 | UHF RF power output high setting | 130 |
| 17 | PALU | 0-255 | UHF RF power output medium setting | 85 |
| 18 | PASU | 0-255 | UHF RF power output low setting | 25 |
| 19 | MODU | 0-255 | Overall deviation setting for UHF | 105 |
| 20 | MIC | 0-63 | Microphone gain set | 54 |
| 21 | TONEU | 0-255 | Transmit audio tone level, push PTT to transmit a test 1000 Hz tone on displayed UHF FM frequency | 98 |
| 22 | TONEV2 | 0-255 | Transmit audio tone level, push PTT to transmit a test 1000 Hz tone on displayed VHF FM frequency | 40 |
| 23 | CTCW | 0-128 | Deviation setting for CTCSS in both UHF & VHF | 39 |
| 24 | DCSW | 0-128 | Deviation setting for DCS in both UHF & VHF | 28 |
| 25 | BPFLUA | 0-255 | UHF A-VFO receive tracking gain, low end of band | 35 |
| 26 | BPFMUA | 0-255 | UHF A-VFO receive tracking gain, mid band | 135 |
| 27 | BPFHUA | 0-255 | UHF A-VFO receive tracking gain, top end of band | 253 |
| 28 | BPFLUB | 0-255 | UHF B-VFO receive tracking gain, low end of band | 35 |
| 29 | BPFMUB | 0-255 | UHF B-VFO receive tracking gain, mid band | 145 |
| 30 | BPFHUB | 0-255 | UHF B-VFO receive tracking gain, top end of band | 253 |
| 31 | AGCUA | 0-255 | UHF A-VFO AGC (suspect receiver gain related) | 180 |
| 32 | AGCUB | 0-255 | UHF B-VFO AGC (suspect receiver gain related) | 170 |
| 33 | SQTHUA | 0-255 | UHF A-VFO squelch threshold | 90 |
| 34 | SQTHUB | 0-255 | UHF B-VFO squelch threshold | 100 |
| 35 | RSSIUA | nil, only displays current value | UHF RSSI A-VFO, inject RF at desired level for 1 bar reading, rotate dial to sample and lock in value | 72 |
| 36 | RSSIUB | nil, only displays current value | UHF RSSI B-VFO, inject RF at desired level for 1 bar reading, rotate dial to sample and lock in value | 75 |
| 37 | A OBH | 0-65535 | unknown A+D adjustment | 3000 \* |
| 38 | A OBL | 0-65535 | unknown A+D adjustment | 2700 \* |
| 39 | D OBH | 0-65535 | unknown D+A adjustment | 3000 \* |
| 40 | D OBL | 0-65535 | unknown D+A adjustment | 2700 \* |
| 41 | D FSKLU | nil | Push PTT to send test FSK signal (heard as 2400 Hz on FM receiver) at low end of UHF band |  |
| 42 | D FSKMU | nil | Push PTT to send test FSK signal (heard as 2400 Hz on FM receiver) at mid UHF band |  |
| 43 | D FSKHU | nil | Push PTT to send test FSK signal (heard as 2400 Hz on FM receiver) at high end of UHF band |  |
| 44 | D 600HzU | nil | Push PTT to send test 600Hz signal UHF band (heard on FM as 200 & 400 Hz?) |  |
| 45 | D 300HzU | nil | Push PTT to send test 300Hz signal UHF band (heard on FM as 800 Hz?) |  |
| 46 | D 1031U | nil | Push PTT to send 1031 test sequence UHF band, heard on DMR as 1031 Hz |  |
| 47 | D BERU | nil | Display received BER of received UHF DMR signal |  |
| 48 | D DIGI | nil | Test UHF DMR for both TX & RX as if it were on a regular DMR channel |  |
| 49 | TXDAV | 0-255 | Unknown VHF analogue adjustment | 145 |
| 50 | PAHV | 0-255 | VHF RF power output turbo setting | 150 |
| 51 | PAMV | 0-255 | VHF RF power output high setting | 100 |
| 52 | PALV | 0-255 | VHF RF power output medium setting | 60 |
| 53 | PASV | 0-255 | VHF RF power output low setting | 20 |
| 54 | MODV | 0-255 | Overall deviation setting for VHF | 50 |
| 55 | MODV2 | 0-255 | Overall deviation setting for 222 MHz | 105 |
| 56 | BPFLVA | 0-255 | VHF A-VFO receive tracking gain, low end of band | 3 |
| 57 | BPFMVA | 0-255 | VHF A-VFO receive tracking gain, mid band | 135 |
| 58 | BPFHVA | 0-255 | VHF A-VFO receive tracking gain, top end of band | 253 |
| 59 | BPFLVB | 0-255 | VHF B-VFO receive tracking gain, low end of band | 0 |
| 60 | BPFMVB | 0-255 | VHF B-VFO receive tracking gain, mid band | 135 |
| 61 | BPFHVB | 0-255 | VHF B-VFO receive tracking gain, top end of band | 253 |
| 62 | AGCVA | 0-255 | VHF A-VFO AGC (suspect receiver gain related) | 170 |
| 63 | AGCVB | 0-255 | VHF B-VFO AGC (suspect receiver gain related) | 170 |
| 64 | SQTHVA | 0-255 | VHF A-VFO squelch threshold | 70 |
| 65 | SQTHVB | 0-255 | VHF B-VFO squelch threshold | 80 |
| 66 | RSSIVA | nil | VHF RSSI A-VFO, inject RF at desired level for 1 bar reading, rotate dial to sample and lock in value | 61 |
| 67 | RSSIVB | nil | VHF RSSI B-VFO, inject RF at desired level for 1 bar reading, rotate dial to sample and lock in value | 68 |
| 68 | D FSKLV | nil | Push PTT to send test FSK signal (heard as 2400 Hz on FM receiver) at low end of VHF band |  |
| 53 | D FSKMV | nil | Push PTT to send test FSK signal (heard as 2400 Hz on FM receiver) at mid VHF band |  |
| 70 | D FSKHV | nil | Push PTT to send test FSK signal (heard as 2400 Hz on FM receiver) at high end of VHF band |  |
| 71 | D 600HzV | nil | Push PTT to send test 600Hz signal VHF band (heard on FM as 200 & 400 Hz?) |  |
| 72 | D 300HzV | nil | Push PTT to send test 300Hz signal VHF band (heard on FM as 800 Hz?) |  |
| 73 | D 1031V | nil | Push PTT to send 1031 test sequence on VHF band, heard on DMR as 1031 Hz |  |
| 74 | D BERV | nil | Display received BER of received VHF DMR signal |  |
| 75 | VBAT | undetermined | Calibrate displayed voltage. Do not adjust, otherwise radio will warn of incorrect voltage and prevent any further adjustments | 109 \* |
| 76 | F1 A0 | 0-65535 | Hex BCD combination of mic gain and mic AGC values, however adjusting has no effect | 42512 |
| 77 | MODE | 0-18 | Changes operational frequency bands of radio |  |
| 78 | FM RSI | nil | RSSI for FM broadcast band, inject RF at desired level for 1 bar reading, rotate dial to sample and lock in value | 5 |
| 79 | 087.50M | nil | Receiver test of FM broadcast band |  |
| 80 | 097.50M | nil | Receiver test of FM broadcast band |  |
| 81 | 108.00M | nil | Receiver test of FM broadcast band |  |
| \- | AM BPFL | 0-255 | AM aircraft band receive tracking gain, low end of band (578PLUS only) | 65 |
| \- | AM BPFM | 0-255 | AM aircraft band receive tracking gain, mid band (578PLUS only) | 110 |
| \- | AM BPFH | 0-255 | AM aircraft band receive tracking gain, low end of band (578PLUS only) | 180 |
| \- | AM AGC | 0-255 | AM aircraft band receive AGC (578PLUS only) | 180 |
| \- | AM RSIV | nil | AM aircraft band, inject RF at desired level for 1 bar reading, rotate dial to sample and lock in value (578PLUS only) | 24 |

*The typical values listed above are unique to one radio, and should not be used to create a complete alignment profile. It is highly unlikely that your radio will work properly using values from another radio, including these typical values. You need proper test & alignment equipment to be able to accurately set each value. As such, the typical values given here are only to provide context for any adjustments you may wish to make. Critical values are marked with an asterisk.*

For the squelch threshold values, lower values results in a more sensitive squelch (to a point!) and higher values require a progressively stronger signal to open the squelch.
The RSSI (received signal strength indicator - in other words the signal meter) has a fairly compressed range of 15dB. I’d have preferred to see at least 30dB range in the signal meter, but I’ve found an acceptable compromise has been to set one bar at -113dBm which equates to values of RSSIU of 36 and RSSIV of 39. The signal meter then reads:

- 1 bar -113 dBm or about S-5
- 2 bars -108 dBm or about S-6
- 3 bars -103 dBm or about S-7
- 4 bars -98 dBm or about S-9

Once finished changing your values, turn the radio off and on again to save them to memory. If you like, you can disable full test mode again by de-selecting the Full Test Mode check box in AT Options application and writing back to the radio. Or, you can de-select both Full Test Mode and Band Select check boxes, which will totally inhibit test mode completely. The values you changed or adjusted will not be erased by doing this, it simply prevents you from accessing the full test mode and inadvertently changing them again. These values will not be overwritten, changed or restored to default by resetting of the radio. Once you change them, you can not get the original value back unless you wrote it down before making adjustments.

You can download a more comprehensive memory map of how each individual adjustment setting is stored in memory, and see more hidden values that are obviously used for RF alignment purposes, but are not available in this test mode.
To experiment and adjust those you will need to use [Flash Utility](53-flash-utility.md) to create your own custom binary image, and [write your own custom CDI and SPI files](58-cdd.md) to enable that data to be written to the radio (Flash Utility can’t write to that area of memory directly, it is safest to write using the Icon update mode with a CDD, CDI & SPI file set).
Download the more comprehensive memory map (11 kb) from here:

- [Download from this webpage here](../../originals/anytonetechzone/Anytone-578-Flash-memory-map.zip)
- [Download via Mega](https://mega.nz/file/KgNgRJib#ivILwXi1zmUypsoiGaTesJFH_m540WqeLpZ3QCLnJE8)
- [Download via Google Drive](https://drive.google.com/file/d/1a6wDJ-PeOgufrEinIk97kTTAxD7DnxG7/view?usp=sharing)
- [Download via Sabercat host](https://sabercathost.com/e850/Anytone-578-Flash-memory-map.zip)


------------------------------------------------------------------------
