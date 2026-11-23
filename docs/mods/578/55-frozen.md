---
title: "Fix a frozen during boot up AnyTone 578 or Alinco DR-MD500 / DR-MD520 Easy"
source_url: https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#Frozen
tags: [AT-D578UV]
---

# Fix a frozen during boot up AnyTone 578 or Alinco DR-MD500 / DR-MD520 Easy

[← All 578 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#Frozen)

Some people have found that their radios have frozen on boot, that the radio displays the startup message "Booting... Please Wait!" or displays the startup picture and does nothing else. Try the following steps, in this order, to clear the problem:

1. Turn the radio off, leave it off for ten seconds, and turn back on.
2. Turn the radio off, remove all power to the radio for 5 minutes, then reconnect and power on.
3. Attempt a reset: turn the radio off, and then hold **P2** and the dial knob in while turning the radio on.
4. Reflash firmware: turn the radio off, then hold the **MENU** and **EXIT** buttons down together just after power off, the LED will flash red and you can then use the CPS software to load your firmware file using **Tool → Firmware Upgrade**.
5. Reflash the SCT3258 baseband: Download the **SCT3258 software, instructions and baseband files (3.18 Mb)** from:
    - [Download via Mega](https://mega.nz/file/XgVy0LyD#Rd1xzH7p9sj_xe3BIUL4_euJLy0PRw8G9yhdlOigQnM)
    - [Download via Google Drive](https://drive.google.com/file/d/1b9GJoFSDs6I9gEM6SBXDjFqL-HdFNWDT/view?usp=sharing) – note Google has recently tightened security for downloads and this file may or may not be available to download by you entirely at Google's discretion
    - [Download via Sabercat host](https://sabercathost.com/irdE/D8x8UV_Base_Band_Update_SCT3258.zip)

    To enter the SCT update mode, hold down the dial knob and **MENU** keys while turning the radio on. From there, follow the instructions included in the download to write the latest baseband file V2.01.07BF to the SCT3258.

## Rebuild your codeplug

Once you have managed to regain control of the radio, the first thing to do is re-build your ’codeplug’ to remove any hidden corruption that caused the freeze in the first place. 99.9% of problems encountered are usually the result of poor ’codeplug’ practices. Using other people’s codeplugs, originating from several CPS versions back, and then added to piecemeal, is almost certain to cause problems. The solution to this is to ensure your codeplug is rebuilt which ensures the underlying data that your codeplug is built upon is fresh and consistent with the CPS and firmware version in use. Do not take any shortcuts in the following process!

1. In CPS, load your old saved codeplug and export everything (**Tool → Export → Export All**).
2. Go through all your Optional Setting and write them down or take screen shots of all the settings there. If you are using encryption, also record all your encryption keys. These settings and encryption keys are not saved by the Export All process.
3. RESET the radio – this step is very important! If you do not do this, the old & possibly problematic data in the radio is not removed.
4. In CPS, read from the freshly reset radio (yes, you are reading a ’blank’ radio, that is OK).
5. Import everything saved from step 1.
6. Finish off your codeplug by attending to the Optional Setting & encryption keys if applicable and confirm all is correct.
7. Send the freshly rebuilt codeplug to the radio.
8. If you had a custom start up picture or background pictures, send those to the radio now.
9. Finally, save the rebuilt codeplug and ensure you use this saved file as the basis for any further changes you may make, and make sure you delete your old problematic codeplug file.

If these steps have not worked, there is a procedure that may help un-freeze your radio and get you going again. Note that this defroster will only work if the freezing is caused by memory corruption. If the problem is a hardware failure, then this will not work.

## Quick defroster

*Credit to Francesco IK8JHL & Andres CD2KDT and thanks to Jason Alexander for assistance with the Alinco models.*

This process is quick and simple, forcing the radio to undergo a reset.

!!! warning
    You will lose your codeplug, so make sure you have a saved copy first.

Download the **AnyTone 578 fast defroster (1 kb):**

- [Download from this webpage here](../../originals/anytonetechzone/578-Fast-defrost.zip)
- [Download via Mega](https://mega.nz/file/3lU1BCAZ#AF6GTSSi-koxV9bq6QF84EbvFG2Z2nbF-vSlpzj25EM)
- [Download via Google Drive](https://drive.google.com/file/d/15suIT4NJjCtmqViPMWWQYVtrNnob97yz/view?usp=sharing)
- [Download via Sabercat host](https://sabercathost.com/ike1/578-Fast-defrost.zip)

Download the **Alinco DR-MD500 fast defroster (1 kb):**

- [Download from this webpage here](../../originals/anytonetechzone/DR-MD500-Fast-defrost.zip)
- [Download via Mega](https://mega.nz/file/j11BCLxA#0NkyZp7dcZJBqcrQnRPUHZ3jkyHf8FC2n12gayqUN8I)
- [Download via Google Drive](https://drive.google.com/file/d/1cO2H6mFpLAU2jwtPFYlBb_r4qH48fmn2/view?usp=sharing)
- [Download via Sabercat host](https://sabercathost.com/edqO/DR-MD500-Fast-defrost.zip)

Download the **Alinco DR-MD520 fast defroster (1 kb):**

- [Download from this webpage here](../../originals/anytonetechzone/DR-MD520-Fast-defrost.zip)
- [Download via Mega](https://mega.nz/file/a01UBbzb#VL3X7LgCNFImG7oxdgvVjlyYkkLIteAX7Cm2NZBYbxc)
- [Download via Google Drive](https://drive.google.com/file/d/1Hot7CKVGMOlihoFXQCCpiePnBLKNtwgp/view?usp=sharing)
- [Download via Sabercat host](https://sabercathost.com/edqP/DR-MD520-Fast-defrost.zip)

Then:

1. Unzip the contents of the fast defroster for your model radio.
2. Confirm that your frozen radio can power up in the Icon Update mode: turn the radio off, hold the **P1** and dial knob down while powering on the radio. You should see a screen with "UPDATE MODE" displayed. If you do not see this screen, this process will not work for you and the radio will have to go back to the supplier for repair or replacement.
3. Start up the CPS, preferably using the latest version you can get. Go to menu **Set → Set Com**. Select the Com Port you normally use to program your radio.
4. In the CPS, go to menu **Tool → Firmware Upgrade**. Click on the Open Update File button, navigate to the directory where you have unzipped the files and select the 578-Fast-defrost.spi file and click Open. Click on OK below the File Open Succesed! message.
5. Ensure Duplex box is ticked, and that Com Speed is set to 921600. Click on Write. The data only takes a fraction of a second to be written to the radio.
6. Turn off the radio, wait ten seconds, then turn it back on again. The radio should immediately go through a reset.
7. You may need to set the time & date. The radio might also power up in Chinese language mode, this is OK, after writing your codeplug to the radio that will be corrected. You may need to power up the radio in test mode to change the band (MODE) or set the band with AT Options software to match the band you were using before, if you get [Band Error](02-band-error.md) when sending your codeplug back to the radio.
8. You are now done!
