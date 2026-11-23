---
title: "Hints & tips for upgrading firmware"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#FWupgrade
tags: [AT-D868UV, AT-D878UV]
---

# Hints & tips for upgrading firmware

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#FWupgrade)

Upgrading firmware on the AnyTone radio is easy, so long as you follow these general steps:

1. Under the original firmware, before you do any upgrades, export everything (**Tool → Export → Export All**).
2. Go through all your Optional Settings and write them down or take screenshots of all the settings there. If you are using encryption, also record all your encryption keys. These settings and encryption keys are not saved by the Export All process.
3. Power up the radio holding the **PTT** and top blue / orange button, and ensure the top LED is flashing red. Upload the new firmware using the CPS software menu **Tool → Firmware and Icon Update**.
4. **Reset the radio – this step is very important!** If you do not do this, the old data in the radio could conflict with the way the firmware expects the memory to be formatted after upgrading.
5. If there is a baseband update with the new firmware release, do this now. Power up the radio holding the top orange / blue button and the **\#** button until the message "This is Boot Mode for SCT!!!" is displayed. Use a freshly installed version of the SCT_PORT Host Controller software on your PC to send the new SCT3258 hex file to the radio. Older versions of the SCT_PORT Host Controller software may not be able to load all the required information, despite giving no error or other failure indication.
6. If there is an icon update with the new firmware release, do this now. Power up the radio holding the **PTT** and the lower side button until the message "UPDATE MODE" is displayed. Upload the new icon file using the CPS software menu **Tool → Firmware and Icon Update**.
7. Install the new version of the CPS.
8. Go to **Tools → Options** and tick the GPS / Bluetooth / 500 Hours record / APRS options that apply to your radio.
9. Now read from the freshly reset radio (yes, you are reading a 'blank' radio, that is OK).
10. Import everything saved from step 1.
11. Finish off your codeplug by attending to the Optional Setting & encryption keys if applicable, and confirm all is correct.
12. Send the freshly rebuilt codeplug to the radio.
13. If you had a custom start-up picture or background pictures, send those to the radio now.
14. Finally, save the codeplug and ensure you use this saved file as the basis for any further changes you may make.

Yes, the thing will work with the last firmware version's codeplug, but strange things can & do happen. Laggy transmit, distorted alert tones, features not working as they should, freezing, lockups and other miscellaneous issues have all been fixed by a fresh codeplug rebuild – a process made a lot easier with the export & import features of the software. This ensures the underlying data that your codeplug is built upon is fresh and consistent with the CPS and firmware version in use. Take the time to do this to ensure the best result.
