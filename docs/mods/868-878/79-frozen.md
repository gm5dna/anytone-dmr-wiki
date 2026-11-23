---
title: "Fix a frozen or stuck during boot up 868 / 878 / 6X2 / DJ-MD5X"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#Frozen
tags: [AT-D868UV, AT-D878UV]
---

# Fix a frozen or stuck during boot up 868 / 878 / 6X2 / DJ-MD5X

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#Frozen)

*Difficulty: Moderate*

Some people have found that their radios have frozen or stuck on boot: the radio displays the startup message "Booting... Please Wait!" or displays the startup picture and does nothing else. Try the following steps, in this order, to clear the problem:

1. Turn the radio off, leave it off for ten seconds, and turn back on.
2. Turn the radio off, remove the battery for ten seconds, replace the battery and turn back on.
3. Attempt a reset: turn the radio off, and then hold **PTT** and the button immediately below the PTT while turning the radio on (don't forget you need to have reset enabled in CPS first).
4. Reflash firmware: turn the radio off, hold the **PTT** and top panel button while turning the radio on. The LED will flash red and you can then use the CPS software to load your firmware file using **Tool → Firmware and Icon Update**.
5. Reflash the SCT3258 baseband: download the **SCT3258 software, instructions and baseband files (3.18 Mb)** from:

    - [Download via Mega](https://mega.nz/file/XgVy0LyD#Rd1xzH7p9sj_xe3BIUL4_euJLy0PRw8G9yhdlOigQnM)
    - [Download via Google Drive](https://drive.google.com/file/d/1b9GJoFSDs6I9gEM6SBXDjFqL-HdFNWDT/view?usp=sharing). Note Google has recently tightened security for downloads and this file may or may not be available to download by you, entirely at Google's discretion.
    - [Download via Sabercat host](https://sabercathost.com/irdE/D8x8UV_Base_Band_Update_SCT3258.zip)

    To enter the SCT update mode, hold down the top orange / blue button and **\#** keys while turning the radio on. On the DJ-MD5, SCT update mode is entered by holding down **PTT** + **\#** keys on power up. From there, follow the instructions included in the download to write the latest baseband file V2.01.07BF to the SCT3258.

## Rebuild your codeplug

Once you have managed to regain control of the radio, the first thing to do is re-build your 'codeplug' to remove any hidden corruption that caused the freeze in the first place. 99.9% of problems encountered are usually the result of poor 'codeplug' practices. Using other people's codeplugs, originating from several CPS versions back, and then added to piecemeal, is almost certain to cause problems. The solution to this is to ensure your codeplug is rebuilt, which ensures the underlying data that your codeplug is built upon is fresh and consistent with the CPS and firmware version in use.

!!! warning
    Do not take any shortcuts in the following process!

1. In CPS, load your old saved codeplug and export everything (**Tool → Export → Export All**).
2. Go through all your Optional Settings and write them down or take screenshots of all the settings there. If you are using encryption, also record all your encryption keys. These settings and encryption keys are not saved by the Export All process.
3. **Reset the radio – this step is very important!** If you do not do this, the old & possibly problematic data in the radio is not removed.
4. In CPS, read from the freshly reset radio (yes, you are reading a 'blank' radio, that is OK).
5. Import everything saved from step 1.
6. Finish off your codeplug by attending to the Optional Setting & encryption keys if applicable, and confirm all is correct.
7. Send the freshly rebuilt codeplug to the radio.
8. If you had a custom start-up picture or background pictures, send those to the radio now.
9. Finally, save the rebuilt codeplug and ensure you use this saved file as the basis for any further changes you may make, and make sure you delete your old problematic codeplug file.

## Defrosters

If these steps have not worked, there are two procedures (the Quick defroster below and the [Full defroster](80-full-defrost.md)) that may help un-freeze your radio and get you going again. Note that these defrosters will only work if the freezing is caused by memory corruption. If the problem is a hardware failure, then these will not work.

### Quick defroster

Credit to Francesco IK8JHL & Andres CD2KDT

This process is quick and simple, forcing the radio to undergo a reset. You will lose your codeplug, so make sure you have a saved copy first.

1. Download the appropriate fast defroster:

    **878 fast defroster (1 kb)**:

    - [Download from this webpage here](http://anytonetechzone.byethost7.com/878-Fast-defrost.zip)
    - [Download via Mega](https://mega.nz/file/W9dEwbgK#bh9NQm_uEdOqK5A2tPQI0qWJfQAjz7NaF4atF_-dJq8)
    - [Download via Google Drive](https://drive.google.com/file/d/1RXW7HHspuwB56WBwTWbg7NkyqRJYiBVp/view?usp=sharing)
    - [Download via Sabercat host](https://sabercathost.com/e858/878-Fast-defrost.zip)

    **868 fast defroster (1 kb)**:

    - [Download from this webpage here](http://anytonetechzone.byethost7.com/868-Fast-defrost.zip)
    - [Download via Mega](https://mega.nz/file/61NWhB5D#uudypd9r6v3p9wKAI5_N9YiCgPTC7-wWB_Lw_XNgbM4)
    - [Download via Google Drive](https://drive.google.com/file/d/1u8fHYIo5fqjUkNLHNJHZxJCvFGns2gb9/view?usp=sharing)
    - [Download via Sabercat host](https://sabercathost.com/e857/868-Fast-defrost.zip)

    **6X2 fast defroster (1 kb)**:

    - [Download from this webpage here](http://anytonetechzone.byethost7.com/6X2-Fast-defrost.zip)
    - [Download via Mega](https://mega.nz/file/GkVkgLSC#EdmzTaQN2bsbTYzsokJKZfIRvhs4ZACD8VcxeUzGoR0)
    - [Download via Google Drive](https://drive.google.com/file/d/1vwkCJZdkQGuEpBz4-XX0AlhJz7S8yWrD/view?usp=sharing)
    - [Download via Sabercat host](https://sabercathost.com/e856/6X2-Fast-defrost.zip)

    **Alinco DJ-MD5 fast defroster (1 kb)**:

    - [Download from this webpage here](http://anytonetechzone.byethost7.com/DJ-MD5-Fast-defrost.zip)
    - [Download via Mega](https://mega.nz/file/fglyxKLZ#kHqdUN1iQBnvKTcDCpN_tITS59Y-wUHiExIiiXbXvPc)
    - [Download via Google Drive](https://drive.google.com/file/d/1H5s0F-vsHq4PM8IGa-N8uKdiXQ-tKxzP/view?usp=sharing)
    - [Download via Sabercat host](https://sabercathost.com/edqE/DJ-MD5-Fast-defrost.zip)

    **Alinco DJ-MD5X fast defroster (1 kb)**:

    - [Download from this webpage here](http://anytonetechzone.byethost7.com/DJ-MD5X-Fast-Defrost.zip)
    - [Download via Mega](https://mega.nz/file/Dh0TSDoZ#2JpSC8FXLuwCvGnBtoL5s92jSY23vlP8BYSh8rfam6M)
    - [Download via Google Drive](https://drive.google.com/file/d/1zAWzoECslFRgyC-4ULbW00V9b1uKc49_/view?usp=sharing)
    - [Download via Sabercat host](https://sabercathost.com/edqF/DJ-MD5X-Fast-Defrost.zip)

2. Unzip the contents into a new directory.
3. Confirm that your frozen radio can power up in the Icon Update mode: turn the radio off, hold the **PTT** & **PF2** buttons down while powering on the radio. You should see a white screen with "UPDATE MODE" displayed. If you do not see this screen, this process will not work for you and the radio will have to go back to the supplier for repair or replacement.
4. Start up the CPS, preferably using the latest version you can get for your model radio. Go to menu **Set → Set Com**. Select the Com Port you normally use to program your radio.
5. In the CPS, go to menu **Tool → Firmware and Icon Update**. Click on the **Open Update File** button, navigate to the working directory and select the Fast-defrost.spi file and click **Open**. Click on **OK** below the File Open Succesed! message.
6. Ensure the **Duplex** box is ticked, and that **Com Speed** is set to 921600. Click on **Write**. The data only takes a fraction of a second to be written to the radio.
7. Turn off the radio, wait ten seconds, then turn it back on again. The radio should immediately go through a reset.
8. You may need to set the time & date. The radio might also power up in Chinese language mode; this is OK, after writing your codeplug to the radio that will be corrected. You may need to power up the radio in test mode to change the band (MODE) or set the band with AT Options software to match the band you were using before, if you get [Band Error](02-band-error.md) when sending your codeplug back to the radio.
9. You are now done!
