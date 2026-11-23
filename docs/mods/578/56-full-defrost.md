---
title: "Full defroster"
source_url: https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#FullDefrost
tags: [AT-D578UV]
---

[← All 578 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, unchanged, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#FullDefrost)

*Full defroster*
If the above quick defroster didn’t work, then you can try using this more comprehensive process to un-freeze your radio. Follow the steps carefully and exactly.
*This process will completely erase & over-write your radio flash memory, and you proceed at your own risk. While it has helped un-freeze a couple of 578s, it can not be absolutely guaranteed to work for you. This will also wipe your codeplug, so make sure you have a saved copy somewhere.*

Test that your frozen radio can power up in the Icon Update mode: turn the radio off, hold the dial knob and P1 buttons down together while powering on the radio. You should see a blank screen with "UPDATE MODE" displayed. If you do not see this screen, this process will not work for you.

Download the **AnyTone 578 full defroster pack (2.1 Mb)** from:

- 
- [Download via Mega](https://mega.nz/file/29NxFShL#fb6cBnqRg_qCJyXch1mbFvyIohsNvzJ-CYgvREW2p4A)
- [Download via Google Drive](https://drive.google.com/file/d/1i1aluXWaZfZr38q4Qk54ecDZ2xLByJEm/view?usp=sharing)
- [Download via Sabercat host](https://sabercathost.com/a1nd/578_full_defrost_pack.zip)


Download the **Alinco DR-MD500 full defroster pack (2.3 Mb)** (Note: not suitable for DR-MD520) from:

- [Download via Mega](https://mega.nz/file/74EGwR7D#gUfFIGC3HzYIo0GYVpXPpiURo1AWUVZfUrnu5KtzfNs)
- [Download via Google Drive](https://drive.google.com/file/d/11b1TIumDgrx3pP1nL94w864MLqOetd7U/view?usp=sharing)
- [Download via Sabercat host](https://sabercathost.com/edqN/DR-MD500_full_defrost_pack.zip)

(There is no full defrost pack for the DR-MD520 as yet)

1.  Unzip the contents into a new directory
2.  Plug in your programming cable to the radio and your computers USB port, hold down dial knob & P1 while powering on the radio, and confirm the display shows "UPDATE MODE"
3.  Start AT_Flash_Utility_v3.exe In the Start Address (Hex) box type 2F00000 \[ 2F and five zeros \] and in the Length (Hex) box type E0000 \[ E and four zeros \]. Then click the Select File button, and navigate to the directory you have unzipped the defrosting files into. Enter a file name of "myvital.bin" then select Save.
4.  Select your usual Com Port, and then click the Read button. You will get two error messages, this is fine, just click on OK. AT Flash Utility will then read some vital flash memory and save it to a file called myvital.bin and takes about 55 seconds to complete.
5.  After the read is complete, click on the OK button. Confirm that your myvital.bin file is in the working directory and that its size is 896kb. If not, go back to step 6 again, making absolutely sure you have given the correct Hex address and length values.
6.  Close down AT Flash Utility.
7.  Rename the file myvital.bin to myvital.CDD (i.e. change the file extension from .bin to .CDD) This step is very important, do not skip this step
    
8.  Turn off your radio, and again hold down the dial knob & P1 while powering on the radio, and confirm the display shows "UPDATE MODE"
9.  Start up the CPS, preferably using the most current version CPS available for your model. Go to menu Set \> Set Com. Select the Com Port you normally use to program your radio.
10. In the CPS, go to menu Tool \> Firmware Upgrade. Click on the Open Update File button, navigate to the working directory and select the flash fresh reset .spi file and click Open. Click on OK below the File Open Succesed! message.
11. Ensure Duplex box is ticked, and that Com Speed is set to 921600. Click on Write. This step will wipe your flash memory clean, and takes quite some time (an hour or more) to complete.
    
12. Turn off your radio, and again hold down the dial knob & P1 while powering on the radio, and confirm the display shows "UPDATE MODE"
13. In the CPS, go to menu Tool \> Firmware Upgrade. Click on the Open Update File button, navigate to the working directory and select the icon .spi file and click Open. Click on OK below the File Open Succesed! message.
14. Ensure Duplex box is ticked, and that Com Speed is set to 921600. Click on Write. This step will rebuild icons and text bitmaps in flash memory, and takes a minute or two to complete.
    
15. Turn off your radio, and yet again hold down the dial knob & P1 while powering on the radio, and confirm the display shows "UPDATE MODE"
16. In the CPS, go to menu Tool \> Firmware Upgrade. Click on the Open Update File button, navigate to the working directory and select the myvital.spi file and click Open. Click on OK below the File Open Succesed! message.
17. Ensure Duplex box is ticked, and that Com Speed is set to 921600. Click on Write. This step will restore vital RF tuning data that is unique to your radio back in flash memory, and takes 25 seconds to complete. This is another very important step that you should not skip, otherwise your radio will not properly transmit on DMR.
    
18. Power cycle the radio normally this time, without holding any buttons. It should boot up somewhat normally this time. You may need to set the time & date. The radio might also power up in Chinese language mode, this is OK, after writing your codeplug to the radio that will be corrected. You may need to power up the radio in test mode to change the band (MODE) or set the band with AT Options software to match the band you were using before, if you get [Band Error](02-band-error.md) when sending your codeplug back to the radio.
19. You are now done!

I recommend updating to the latest firmware version available for your model after doing this process, if you have not already done so. You MUST reset the radio by holding down the dial knob and P2 while powering on the radio after doing a firmware update, this is extremely important.
If these suggestions still do not un-freeze your radio then, sadly, it it likely the problem is a hardware fault, and no amount of resets, reloading of firmware or codeplugs, or performing any special procedure will fix that. You should get in touch with the seller of the radio to discuss repair.

------------------------------------------------------------------------
