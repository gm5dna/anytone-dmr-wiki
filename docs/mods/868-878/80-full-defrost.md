---
title: "Full defroster"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#FullDefrost
tags: [AT-D868UV, AT-D878UV]
---

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, unchanged, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#FullDefrost)

*Full defroster*
If the above quick defroster didn't work, then you can try using this more comprehensive process to un-freeze your radio. Follow the steps carefully and exactly.
*This process will completely erase & over-write your radio flash memory, and you proceed at your own risk. While it has helped un-freeze a couple of 878s, it can not be absolutely guaranteed to work for you. This will also wipe your codeplug, so make sure you have a saved copy somewhere.*

Test that your frozen radio can power up in the Icon Update mode: turn the radio off, hold the PTT & PF2 buttons down while powering on the radio. You should see a white screen with "UPDATE MODE" displayed. If you do not see this screen, this process will not work for you.

Turn the radio off for now, and fully charge the battery

Download the defrost pack from:
**878 full defroster (2.1 Mb):**
[Download via Mega](https://mega.nz/file/ypsDDTqY#eEeP1wJuat1HJzVsHj4oj59Yp1mqhsySaWp6YxSpQOg)
[Download via Google Drive](https://drive.google.com/file/d/1yzFSkx__zN2AyfqTMClZucElLVenhQim/view?usp=sharing)
[Download via Sabercat host](https://sabercathost.com/efP4/878_full_defrost_pack.zip)

**868 full defroster (2.1 Mb):**
[Download via Mega](https://mega.nz/file/es0VCCDY#dHGo5AiKeQLs09GFI8SjoimB_haumQYglFitnCNbcwQ)
[Download via Google Drive](https://drive.google.com/file/d/1bzV0XYronrygVPCS7anTSqp0DBjI7SpX/view?usp=sharing)
[Download via Sabercat host](https://sabercathost.com/e853/868_defrost_pack.zip)

**6X2 full defroster (1.8 Mb):**
[Download via Mega](https://mega.nz/file/vpdUiSgT#8fvlZxa8wkpinWnyYpLuvoVdYP7O9seE-wVE8g-ud9M)
[Download via Google Drive](https://drive.google.com/file/d/1Xwjhbw-Sqwd9WuQmMeRvBK8wzkhupXja/view?usp=sharing)
[Download via Sabercat host](https://sabercathost.com/edqG/6X2_full_defrost_pack.zip)

**Alinco DJ-MD5X full defroster (3.4 Mb):**
[Download via Mega](https://mega.nz/file/T4FU2QSB#GCgFmWacPKxwyWAw5UNnwi0yPov48110WzyyELJSLe0)
[Download via Google Drive](https://drive.google.com/file/d/1epBT7u3_v-MLYv7jAje2E_j_LNIb5i-z/view?usp=sharing)
[Download via Sabercat host](https://sabercathost.com/edqH/DJ-MD5X_full_defrost_pack.zip)
Note: \*\*\*NOT\*\*\* SUITABLE FOR DJ-MD5T OR DJ-MD5E. This will only work on the DJ-MD5XE / DJ-MD5XT / DJ-MD5XEG / DJ-MD5XTG models. I do not have a full defroster available for the DJ-MD5T / DJ-MD5E models.

Unzip the contents into a new directory

With a fully charged battery, plug in your programming cable to the radio and your computers USB port, hold down PTT & PF2 while powering on the radio, and confirm the display shows "UPDATE MODE" with a white background

Start AT_Flash_Utility_v3.exe In the Start Address (Hex) box type 2F00000 \[ 2F and five zeros \] and in the Length (Hex) box type E0000 \[ E and four zeros \]. Then click the Select File button, and navigate to the directory you have unzipped the defrosting files into. Enter a file name of "myvital.bin" then select Save.

Select your usual Com Port, and then click the Read button. You will get two error messages, this is fine, just click on OK. AT Flash Utility will then read some vital flash memory and save it to a file called myvital.bin and takes about 55 seconds to complete.

After the read is complete, click on the OK button. Confirm that your myvital.bin file is in the working directory and that its size is 896kb. If not, go back to step 6 again, making absolutely sure you have given the correct Hex address and length values.

Close down AT Flash Utility.

Rename the file myvital.bin to myvital.CDD (i.e. change the file extension from .bin to .CDD) This step is very important, do not skip this step


Turn off your radio, and again hold down the PTT & PF2 buttons while powering on. Confirm the display shows "UPDATE MODE" with a white background

Start up the CPS, preferably using the most current version CPS available for your model. Go to menu Set \> Set Com. Select the Com Port you normally use to program your radio.

In the CPS, go to menu Tool \> Firmware and Icon Update. Click on the Open Update File button, navigate to the working directory and select the total flash fresh reset .spi file and click Open. Click on OK below the File Open Succesed! message.

Ensure Duplex box is ticked, and that Com Speed is set to 921600. Click on Write. This step will totally wipe your flash memory clean, and takes around 40-45 minutes to complete.


Turn off your radio, and again hold down the PTT & PF2 buttons while powering on. Confirm the display shows "UPDATE MODE" with a white background

In the CPS, go to menu Tool \> Firmware and Icon Update. Click on the Open Update File button, navigate to the working directory and
for 868 users, select the D868_1G_ICON_V1.20_20190226.spi file, click Open
for 878 users, select the D878_1G_ICON_V1.21_20201230.spi file, click Open
6X2 users, your icon file is called DMR_6X2_PIC_V1.1a.spi select it and click Open
and Alinco DJ-MD5 users your icon file is called Alinco_DJMD5XEG_icon_backup.spi
Click on OK below the File Open Succesed! message.

Ensure Duplex box is ticked, and that Com Speed is set to 921600. Click on Write. This step will rebuild icons and text bitmaps in flash memory, and takes 50 seconds to complete.


Turn off your radio, and yet again hold down the PTT & PF2 buttons while powering on. Confirm the display shows "UPDATE MODE" with a white background

In the CPS, go to menu Tool \> Firmware and Icon Update. Click on the Open Update File button, navigate to the working directory and select the myvital.spi file and click Open. Click on OK below the File Open Succesed! message.

Ensure Duplex box is ticked, and that Com Speed is set to 921600. Click on Write. This step will restore vital RF tuning data that is unique to your radio back in flash memory, and takes 25 seconds to complete. This is another very important step that you should not skip, otherwise your radio will not properly transmit on DMR.


Power cycle the radio normally this time, without holding any buttons. It should boot up somewhat normally this time. You may need to set the time & date. The radio might also power up in Chinese language mode, this is OK, after writing your codeplug to the radio that will be corrected. You may need to power up the radio in test mode to change the band (MODE) or set the band with AT Options software to match the band you were using before, if you get [Band Error](02-band-error.md) when sending your codeplug back to the radio.

You are now done!

I recommend updating to the latest firmware version available for your model after doing this process, if you have not already done so. You MUST reset the radio with PTT & PF1 after updating the firmware, this is extremely important.
If these suggestions still do not un-freeze your radio then, sadly, it it likely the problem is a hardware fault, and no amount of resets, reloading of firmware or codeplugs, or performing any special procedure will fix that. You should get in touch with the seller of the radio to discuss repair.

------------------------------------------------------------------------
