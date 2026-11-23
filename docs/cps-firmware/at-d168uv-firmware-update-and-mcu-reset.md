---
title: D168UV Firmware Update
item: "13"
source_url: https://hamradiosouthernrepeaters.co.uk/images/Anytone/AT-D168UV_Firmware_update_and_MCU_Reset.pdf
original: ../originals/images/Anytone/AT-D168UV_Firmware_update_and_MCU_Reset.pdf
tags: [AT-D168UV]
---

# D168UV Firmware Update

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/Anytone/AT-D168UV_Firmware_update_and_MCU_Reset.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/Anytone/AT-D168UV_Firmware_update_and_MCU_Reset.pdf) Hub item 13.

!!! warning
    Before starting, **back up your codeplug file!** Also, if your radio model is equipped with APRS and GPS, please make sure they are turned off to prevent CPU or memory IC damage in the radio.

1. In the CPS software click **Set → Set Com**, choose the correct Com port for your radio.

    ![CPS Set menu with Set COM highlighted and the Communication Setting window listing COM12 and COM1](../assets/img/at-d168uv-firmware-update-and-mcu-reset/img-09.jpeg)

2. Use the USB C cable to connect PC and radio.
3. Hold down the **PF1** key and **PF2** key (two keys below **PTT**) at the same time, power on the radio, and the red LED will begin blinking.
4. In **CPS → Tool → Firmware and Icon Update**, choose “Open Update File” and select the FW or Icon SPI file you want to update to:

    ![CPS Tool menu with Firmware and Icon Update highlighted, and the Firmware_Update window](../assets/img/at-d168uv-firmware-update-and-mcu-reset/img-11.png)

    *Firmware_Update window: Open Update File and Com Speed = 921600 highlighted.*

5. Click Open Update File and choose the appropriate SPI file:

    ![Firmware_Update window with Open Update File, Com Port, Com Speed 921600 and Write](../assets/img/at-d168uv-firmware-update-and-mcu-reset/img-15.jpeg)

    *Firmware_Update: Com Speed = 921600, Duplex ticked.*

    - For FW update use the SPI file from the FW Update Folder.
    - For Icon update please see the separate Icon Update instructions.

6. Once you have the file selected, click Write to update the radio to the latest firmware. After the firmware update, the radio will reboot and should return to normal display on screen.
7. **Important!** You must do a MCU reboot to the radio to activate the new firmware. Failure to do so can cause erratic behavior or freezes.

## 9. Rebooting the MCU (radio reset)

!!! warning "Important notice"
    Again, please make sure before performing the steps below that your codeplug is backed up off your radio.

After updating the firmware, you need to reset the radio Main Control Unit (MCU) as follows:

1. Power off the radio first.

    ![AT-D168UV showing the Calibrate Date screen, with arrows at the PTT and PF1 keys and the green MENU key boxed](../assets/img/at-d168uv-firmware-update-and-mcu-reset/img-16.jpeg)

2. With the radio off, push the **PTT** button and the button directly below it. That button is also called the **PF1** key. Then, while holding both buttons, turn the power on and wait for the radio to boot. Don’t release them yet.

    !!! warning
        Please wait, and do not turn the radio off while it restarts.

3. The radio will start up and the display will show:

    > Are you sure you want to Initialize the radio?
    > Confirm · Exit

    Push the black key with the green (also known as the **MENU** key) to confirm the MCU reboot / initialisation.

4. After the MCU reboot is confirmed, you will have to set the time zone, date and time information as follows:

    - Use the **PF1** key to scroll or navigate through the GMT date / time fields.
    - The active field for data set will be shown in red text.
    - The **Up** and **Down** arrow keys will allow you to change the information in the fields.
    - After you have all the correct information entered, use the green **MENU** key to confirm the settings and the radio will restart.

    ![AT-D168UV showing the Calibrate Date screen, with arrows at the PTT and PF1 keys and the green MENU key boxed](../assets/img/at-d168uv-firmware-update-and-mcu-reset/img-17.jpeg)

5. You will now have to reload your saved codeplug as the final step.

## See also

- [How to update CPS and Firmware V8](how-to-update-cps-and-firmware.md)
- [MCU Reset – 868 & 878](mcu-reset-868-878.md)
- [D578UV Mobile Radio Firmware Update Instructions](d578uv-fw-and-mcu-reset.md)
- [Strange or odd things happening v3](../troubleshooting/strange-or-odd-things-happening.md)
