---
title: Anytone Updates (Allan VK3SLR)
item: "67"
source_url: https://hamradiosouthernrepeaters.co.uk/images/Anytone/Anytone_Update_Instructions_by_Allan_VK3SLR.pdf
original: ../originals/images/Anytone/Anytone_Update_Instructions_by_Allan_VK3SLR.pdf
tags: [AT-D868UV]
---

# Anytone Updates (Allan VK3SLR)

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/Anytone/Anytone_Update_Instructions_by_Allan_VK3SLR.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/Anytone/Anytone_Update_Instructions_by_Allan_VK3SLR.pdf) Hub item 67.

Hello to all Anytone Owners,

I put together this document to help me learn the processes to do the various updates to my Anytone Radios. I have followed these steps for over 2 years now; it all started when I had the Anytone AT-D868UV. I only recently added the Base Band update process to this document with help with clarification from Duane N6DMR.

Update Instructions for:

1. CPS Update
2. Base Band Update
3. Firmware Update
4. Icon Update

## Section 1: CPS

1. Uninstall Previous CPS **first**.
2. Install New CPS.
3. Read Radio with new CPS to backup your Codeplug.
4. Perform MCU Reset (see note below).
5. During the MCU Reset you need to set the Time Zone, Date & Time.
6. You are now ready to install the Firmware.

!!! note
    The reason I do the MCU Reset during this process is to make sure there is no accidental Transmitting of the radio while it's connected to the PC. During Flashing steps you need to make sure GPS/APRS beaconing are disabled.

## Section 2: Base Band

If there is no Base Band update in your Downloaded Update Package, you may be able to skip this step.

!!! warning "Important"
    - Check your SCT 3258 Base Band version in the radio menu **Settings → Device Info**. Make sure the SCT3258 listed in the radio version matches the SCT 3258 Base Band version in the FW update Change Log in the **“A Read First…”** folder. FW and Base Band interact and they must match the version in the change log.
    - **Always** uninstall any older versions of the SCT_PORT.MSI program before doing this update.
    - Always use the latest version of the SCT update program that is supplied in the firmware package.

!!! tip "Good tip"
    When finished updating the SCT 3258 Base Band, go ahead and uninstall the SCT_PORT.MSI Program to avoid using an older version next time.

1. Hold pressing the **#** key and orange/blue top key, at the same time power on the radio. Screen display: “WARNING This is Boot Mode for Sct!!!”
2. Use the USB cable to connect radio and your PC.
3. Install SCT Port.exe.
4. Run SCT_PORT.exe.
5. Select Platform as SCT3258.
6. In the SCT_PORT.MSI program **Tool Menu → Config → Set Com**.
7. In the SCT_PORT.MSI program **Tool Menu → Flash Update**.
8. Open New .Hex File.
9. Click on “Init Port” to check the com port connection is correct.
10. Click on “Flash Update” to start the SCT update.
11. The update is done.

## Section 3: Firmware

1. Hold pressing **PTT** & **PF3** Key (top Blue/Orange button) while Power On Radio (Red LED Blinking).
2. In CPS **Set Menu** → Click Set Com Port.
3. In CPS **Tools Menu** → Click Firmware & Icon Update. Click “Open Update File” and select the New Firmware.spi File.

<!-- source numbering continues at 7 -->

7. Click "Write" to update the radio to the latest firmware. After the Firmware update, the radio should return to normal display on screen.
8. Complete the MCU Reset process below.

### MCU Reset

After updating the firmware, you need to MCU Reset to the radio as follows:

a) Power off the radio first.

b) Then while holding down the **PTT** and the **PF1** button down at the same time, Power the radio ON.

- Please Wait – and do not turn the radio off while it restarts.
- Select the Green menu key to confirm the MCU Reboot / Initialization.

c) After the MCU reboot is confirmed, you will have to set the Time Zone, Date & Time and information as follows:

- Use the **P1 key** to scroll or navigate through the GMT date / time fields.
- Note the active field for data set will be shown in Red text.
- Up and Down arrow keys will allow you to change the information in the fields.
- After you have all the correct information entered, use the Green menu key to confirm the settings and the radio will restart.

d) You will now have to reload your saved code plug as the final step.

## Section 4: Icon

If there is no Icon update in your Downloaded Update Package, please skip this step, re-load your saved codeplug and you're done!

1. Hold pressing **PTT** key and **PF2** key (the bottom side key), at the same time power on. LCD display: "UPDATE MODE".
2. Use the USB cable to connect radio to PC.
3. In **CPS → Set Menu → Set Com Port**.
4. In **CPS → Tool Menu →** choose the Firmware & Icon Update.
5. Click Open Icon Update File, choose the .sip (choose either Anytone Start up or Welcome Start up).
6. Com Speed set as 921600, tick on Duplex.
7. Click Write to update the radio the latest firmware.
    - Note: The Radio Display will not change after the update until you turn the radio off and back on.
8. Reboot the radio when the update is finished.
9. You're Done!

*Created by Allan VK3SLR on 1<sup>st</sup> January 2020. Information from Duane N6DMR. Proof read by Paul VK3CRT.*
