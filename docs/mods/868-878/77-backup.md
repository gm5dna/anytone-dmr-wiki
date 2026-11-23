---
title: "Backing up or restoring vital alignment & configuration data of your 878 / 868 / 6X2 (unte"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#Backup
tags: [AT-D868UV, AT-D878UV]
---

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, unchanged, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#Backup)

**Backing up or restoring vital alignment & configuration data of your 878 / 868 / 6X2 (untested on DJ-MD5 or DJ-MD5X)**
There is vital RF alignment and configuration data, unique to your radio alone, that is stored in memory. It would be a very good idea to make a backup of this data in case you ever need to restore it at some time in the future. This could be due to flash memory corruption, or any number of other reasons.

*Making a backup*

1.  
2.  Download & unzip **Flash Utility software (10kb)** from:
    [Download from this webpage here](../../originals/anytonetechzone/AT_Flash_Utility_v3.zip)
    [Download via Mega](https://mega.nz/file/v1tVHYIT#r1i82DLy-XRwDGsNnqkcSj2ClME1KvsE2Qr3YaqPFps)
    [Download via Google Drive](https://drive.google.com/file/d/1mV4L8xQSz9GRImEwtNsgjpByWZ_h1MFx/view?usp=sharing)
    [Download via Sabercat host](https://sabercathost.com/e85c/AT_Flash_Utility_v3.zip)
3.  With a fully charged battery, plug in your programming cable to the radio and your computers USB port, and power on the radio
4.  Start AT_Flash_Utility_v3.exe
5.  In the Start Address (Hex) box type 2F00000 \[ 2F and five zeros \] and in the Length (Hex) box type E0000 \[ E and four zeros \]. Take care to correctly enter the hex addresses given in this step.
6.  Click the Select File button, and navigate to the directory you wish to save the data backup file into. Enter a file name of "myvital.bin" then select Save. If you have more than one radio, or perhaps you own another model of radio, make sure you save each backup to a different directory and clearly identify which individual radio that directory and it's backup file belongs to.
7.  Select your usual Com Port, and then click the Read button. AT Flash Utility will then read the vital bits of flash memory and save it to a file called myvital.bin and takes about a minute to complete.
8.  After the read is complete, click on the OK button. Confirm that your myvital.bin file was saved to your directory and that its size is 896kb. If not, go back to step 4 again, making absolutely sure you have given the correct Hex address and length values.
9.  Close down AT Flash Utility.
10. Rename the file myvital.bin to myvital.CDD (i.e. change the file extension from .bin to .CDD) This step is very important, do not skip this step!


*Restoring a saved backup file*
This step shouldn't be carried out unless you have strong reason to believe your RF alignment data is corrupt. There is inherent risk, though very slight, that writing data to parts of flash memory that isn't normally user accessible can make things worse. Follow these steps carefully, and take your time.

1.  It is assumed you already have downloaded Flash Utility as per *Making a backup* step 1 just above.
2.  Download some **supporting files (\<1 kb)** necessary to restoring a backup from:
    [Download from this webpage here](../../originals/anytonetechzone/myvital-support.zip)
    [Download via Mega](https://mega.nz/file/2t0RmCyI#9sc0Em5xwzKw9OTsoaO69TndaKgM8KsblwPOCIaBXe0)
    [Download via Google Drive](https://drive.google.com/file/d/1XSmkgApftUiT709gj40Gr4lb-lE7mXU8/view?usp=sharing)
    [Download via Sabercat host](https://sabercathost.com/e851/myvital-support.zip)
3.  Unzip these support files to your directory holding the backup file. You should now have the following files in there: myvital.CDD (your previously saved & renamed myvital.bin), myvital.CDI & myvital.spi
4.  With a fully charged battery, plug in your programming cable to the radio and your computers USB port, and power on the radio while holding down the PTT & PF2 buttons. Confirm the display shows "UPDATE MODE" with a white background
5.  In the CPS programming software, go to menu Tool \> Firmware and Icon Update. Click on the Open Update File button, navigate to the directory where you saved your backup, select the myvital.spi file and click Open. Click on OK below the File Open Succesed! message. (If you have multiple radios and multiple backup files, make absolutely sure you have selected the correct backup file to send to the connected radio)
6.  Ensure Duplex box is ticked, and that Com Speed is set to 921600. Click on Write. This step will restore vital RF tuning data that is unique to your radio back in flash memory, and takes 25 seconds to complete.
7.  Turn the radio off, then power on the radio normally this time, without holding any buttons.
8.  You may need to set the time & date. The radio might also power up in Chinese language mode, this is OK, after writing your codeplug to the radio that will be corrected. You may need to power up the radio in test mode to change the band (MODE) or set the band with AT Options software to match the band you were using before, if you get [Band Error](02-band-error.md) when sending your codeplug back to the radio.
9.  You are now done!


------------------------------------------------------------------------
