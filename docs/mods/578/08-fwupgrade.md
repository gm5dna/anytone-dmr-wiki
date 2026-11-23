---
title: "Hints & tips for upgrading firmware"
source_url: https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#FWupgrade
tags: [AT-D578UV]
---

# Hints & tips for upgrading firmware

[← All 578 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#FWupgrade)

Upgrading firmware on the AnyTone radio is easy, so long as you follow these general steps:

1. Under the original firmware, before you do any upgrades, export everything (**Tool → Export → Export All**).
2. Go through all your Optional Setting and write them down or take screen shots of all the settings there. If you are using encryption, also record all your encryption keys. These settings and encryption keys are not saved by the Export All process.
3. Identify the correct firmware you should be using. For the AnyTone family of 578 radios, there are two different basic models: the 578 using v1.xx firmware and the 578-II using v2.xx firmware. In addition, 578s manufactured before mid-2022 use a GD32 type MCU, and those manufactured after mid 2022 will use an equivalent AT32 type MCU – and each have their own matching firmware. Look for GD or AT in the firmware file name and make sure you select the right one for your radio.
4. Power up the radio normally, then hold down the **MENU** and **EXIT** keys and power off the radio. Ensure the LED is flashing red, indicating firmware upload mode is active. Upload the new firmware using the CPS software menu **Tool → Firmware Upgrade** (if this doesn't automatically launch a new window with the firmware updater, you can manually find and run file `QX_Firmware_Update.exe` which does the same thing).
5. Reset the radio.

    !!! warning
        This step is very important! If you do not do this, the old data in the radio could conflict with the way the firmware expects the memory to be formatted after upgrading.

6. If there is a baseband update with the new firmware release, do this now. Power up the radio holding the top orange / blue button and the **#** button until the message "This is Boot Mode for SCT!!!" is displayed. Use a freshly installed version of the SCT_PORT Host Controller software on your PC to send the new SCT3258 hex file to the radio. Older versions of the SCT_PORT Host Controller software may not be able to load all the required information, despite giving no error or other failure indication.
7. If there is an icon update with the new firmware release, do this now. Power up the radio while holding in the **DIAL** and **P1** key until the message "UPDATE MODE" is displayed. Upload the new icon file using the CPS software menu **Tool → Firmware Upgrade** (while this selection doesn't specifically mention 'Icon', this is definitely the correct process to use) and select the icon update file to write to the radio.
8. Install the new version of the CPS.
9. Go to **Tools → Options** and tick the GPS / Bluetooth / 500 Hours record / APRS options that apply to your radio.
10. Now read from the freshly reset radio (yes, you are reading a 'blank' radio, that is OK).
11. Import everything saved from step 1.
12. Finish off your codeplug by attending to the Optional Setting & encryption keys if applicable and confirm all is correct.
13. Send the freshly rebuilt codeplug to the radio.
14. If you had a custom start up picture or background pictures, send those to the radio now.
15. Finally, save the codeplug and ensure you use this saved file as the basis for any further changes you may make.

Yes, the thing will work with the last firmware version's codeplug, but strange things can & do happen. Laggy transmit, distorted alert tones, freezing, lockups and other miscellaneous issues have all been fixed by a fresh codeplug rebuild – a process made a lot easier with the export & import features of the software. This ensures the underlying data that your codeplug is built upon is fresh and consistent with the CPS and firmware version in use. Take the time to do this to ensure the best result.

## If the update goes wrong

If something goes wrong with the firmware update process, like a power failure in the middle of writing or the USB cable gets knocked, and corrupts the update to the point where the 578 won't turn on or reset any more, follow this process that Sergey UA3ARF passed along:

1. Remove power from the 578 by unplugging its power cord, or turn off your power supply. Wait for a minute to allow things to settle.
2. You will need to get the help of a second person here: hold down the **POWER**, **MENU** and **EXIT** buttons. While holding in those buttons, reconnect power (or turn on your power supply) and then first release just the **MENU** and **EXIT** buttons, and then release the **POWER** button quickly after.
3. If you've done this right, the front panel LED will be flashing red, indicating the 578 is ready to accept a firmware update. Carefully redo the firmware update again.
