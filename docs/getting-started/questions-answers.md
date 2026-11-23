---
title: "Questions & Answers 868 - 878 - 578"
item: "1"
source_url: https://hamradiosouthernrepeaters.co.uk/50-questions-answers.html
tags: [AT-D868UV, AT-D878UV, AT-D578UV]
---

# Questions & Answers 868 - 878 - 578

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Source](https://hamradiosouthernrepeaters.co.uk/50-questions-answers.html) Hub item 1.

Short URL to this page: [http://tiny.cc/AnytoneDMR-QA](http://tiny.cc/AnytoneDMR-QA)

### 1. Why my 168/868/878/578 does not show people’s name and call sign, instead it’s just showing DMR id

[You need to load the User Data Base to your radio.](https://kf5iw.com/contactdb.php)

### 2. Analogue frequencies are nothing but noise, how do you alter the squelch?

**CPS → Optional Setting → Other → SQL A and B**, or **Radio Menu → Settings → Radio Set → No 21 Ana Sq Level**.

### 3. Windows 10 and 11 drivers

!!! warning
    Do not, do not, do not install the drivers.

1. Via the USB cable, plug your radio into the USB on your Windows 10/11 machine.
2. Turn the radio on and let Windows 10/11 install the drivers.
3. You might have to run Windows Update so it can find the drivers.

### 4. How to update firmware and CPS

In the folder you download, you will find PDF files with full instructions.

### 5. UK: can I use this type of radio on PMR 446?

The simple answer is no. [Analogue and Digital PMR446 Information Sheet.](https://www.ofcom.org.uk/__data/assets/pdf_file/0025/85156/ir_2009_analogue_and_digita1.pdf)

### 6. BT PTT keeps dropping connection

Turn Bluetooth on in the radio. Turn the radio off. Hold down the **PTT** on the BT button and turn the radio on. Keep holding down the **PTT** until the radio says BT PTT connected.

### 7. Radio freezes up

- Turn off Date & Time.
- Turn off Power Save.
- If scanning, turn off Sub Channel.
- In **CPS → Digital Func**, set *Prewave Time* and *Wake Head Period* = 0ms.

[Also have a look at this PDF as it could be a bad codeplug.](../cps-firmware/codeplug-update-to-new-version-of-cps.md) This is the [setting](settings-i-use.md) I use.

### 8. 578: UK, can I use Cross Band on a Foundation or Intermediate licence?

The simple answer is no. You would have to get the TX power under 500mW to stay within your licence.

- You also can not leave it untended if you do get it under 500mW.
- No 3rd party traffic permitted.
- Intermediate can look into getting a NoV for a Simplex Gateway.

### 9. How do you program it so that you can scroll through all 4000 channels manually using the rotary knob?

You can not. You need to use Zones. Zones can hold up to 250 channels. For 4000 channels you would need 16 zones.

### 10. UK: what frequencies should I use for my hotspot?

434.0000 and 438.8000 – Low Power Non-NoV Personal Hot-Spot.

### 11. All of a sudden an alarm activates and the screen flashes "Alarming", how do I stop it?

Lone worker alarm… turn it off in the codeplug.

### 12. How do you know if APRS is working?

Look yourself up on [APRS.fi.](https://aprs.fi/)

### 13. How do you change from both bands to just one band on the display?

Set up a side or front key via **CPS → Optional Settings → Key Function** for Sub Ch On/Off.

### 14. What aftermarket antennas are people using?

Nagoya 701 (but cheap copies around) or [MRW-205R 2/70cm.](https://www.moonraker.eu/mrw-205r-2-70cm-supergainer-with-reverse-sma)

### 15. How to take off the recorded audio files

In the CPS under **Tools → Record**.

### 16. How to add Zones purely using the keypad?

**Menu → Zones → Key UP → Add Zone**.

### 17. Can the radios be used on standard FM and repeaters?

Yes.

### 18. Difference between 168, 868, 878, 878plus and 578

| Model | Features |
|---|---|
| 868 | DMR APRS |
| 878 | DMR & Analog APRS, Talker Alias, AES Encryption, Roaming, CCTS/DCS scan |
| 878Plus | DMR & Analog APRS, Digi APRS RX, Talker Alias, AES Encryption, Roaming, CCTS/DCS Scan, Bluetooth |
| 878IIPlus | Same as 878Plus, with Analog APRS RX added |

All 878s have many more features over the 868.

![Table comparing the D868UV, D878UV, D878UV PLUS, D878UVII and D878UVII PLUS (GPS, BT, APRS, memory, digital contacts, firmware/CPS)](../originals/images/Anytone/868.jpg)

![Table comparing the D878UV, D878UV PLUS, D878UVII, D878UVII PLUS and D168UV features](../originals/images/Anytone/D168UV_.jpg)

| Model | Features |
|---|---|
| 578pro | DMR & Analog APRS, Digi APRS RX, Talker Alias, AES Encryption, Roaming, CCTS/DCS Scan, Bluetooth |
| 578plus | Same as Pro, with Analog APRS RX and AM AIR Band RX added |

![Table comparing the D578UV, D578UVG, D578UV PRO and D578UV PLUS (GPS, BT, APRS, air band RX)](../originals/images/Anytone/578_Plus_With_Air_Bands.jpg)

### 19. What is Roaming?

[Google Videos & Info.](https://www.google.com/search?client=firefox-b-d&q=Anytone+878+roaming)

### 20. 868 878 Test/Change Mode

Turn the radio off. Hold **PTT** and **1** key in and turn the radio on. Change mode. Turn the radio off and on.

!!! note "Update"
    This has changed in newer radios and now requires software. How to use: [Document](../cps-firmware/change-mode-868878578.md).

!!! warning
    Doing this mod can void your warranty.

### 21. 578 Test/Change Mode

Turn the radio off. Hold **P4** and **Channel** knob in and turn the radio on. Change mode. Turn the radio off and on.

!!! note "Update"
    This has changed in newer radios and now requires software. How to use: [Document](../cps-firmware/change-mode-868878578.md).

!!! warning
    Doing this mod can void your warranty.

### 22. Icons missing

[This could help fix the issue.](../cps-firmware/codeplug-update-to-new-version-of-cps.md)

### 23. Icon R is missing when Roaming is on

If you activate Bluetooth from CPS or via keyboard, the R icon disappears… The BT icon is in the same place as R.

### 24. How many channels to a Zone?

The radio has 250 Zones. A Zone can have the maximum of 160 analog and/or digital channels.

### 25. "Please Charge the Battery!" when you PTT

This is due to RF. You most likely changed to a different antenna. [More info on this link](../hardware/correct-antenna-for-anytone-868-878-878plus.md).

### 26. Can not MCU Reset 868 or 878

Read the 2nd part of this [Document](../cps-firmware/mcu-reset-868-878.md).

### 27. Can not write codeplug to the radio

- Turn off APRS, GPS and BT in the radio.
- In CPS make sure you have **Set → Set COM** → selected the Com port number.

### 28. Green irregular blinking LED

[All it means is RF is being detected.](../troubleshooting/green-irregular-blinking-led.md)

### 29. Where do I put my callsign in the software?

Radio ID List. [Also read this for Talker Alias on the 878 and 578](../contacts-talkgroups/anytone-878-sending-receive-talker-alias.md)

### 30. How to scan between two sets of frequencies

[Read this Document](../scanning-monitoring/how-to-scan-between-two-sets-of-frequencies.md)

### 31. How to do a 4000 disconnect

- 4000 as a *Private Call* will only disconnect Reflectors (Hytera and Moto Repeaters).
- 4000 as a *Group Call* will disconnect Reflectors and Talk Groups (Hotspots and Repeaters Slot 1).
- 4000 will not disconnect [Static Talk Groups](../networks-hotspots/dynamic-talkgroup-and-static-talkgroup-on-brandmeister.md).

### 32. Echo/Parrot via 9990

This is down as a Private call, not a group call.

### 33. SetCommDataByOptionError, SetCommDataBy2toneError, SetCommDataByAutoRepFreqsError

All mean a bad/corrupt codeplug. [Try this and it should fix](../cps-firmware/codeplug-update-to-new-version-of-cps.md).

### 34. Manually input your DMR ID

**Menu → Settings → Chan Set → Radio ID → Select → Option → Edit ID → Enter new ID → Confirm → Save → Select Radio ID**

### 35. Bluetooth app issues

The app supports Android 4.3 or higher version. Also does not work on Samsung S10. Anytone is working on a fix.

### 36. Bluetooth app: how to use

All info is in the download file.
