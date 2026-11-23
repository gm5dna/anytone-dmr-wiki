---
title: D578UV Mobile Radio Firmware Update Instructions
item: "14"
source_url: https://hamradiosouthernrepeaters.co.uk/images/Anytone/D578UV_FW_and_MCU_Reset.pdf
original: ../originals/images/Anytone/D578UV_FW_and_MCU_Reset.pdf
tags: [AT-D578UV]
---

# D578UV Mobile Radio Firmware Update Instructions

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/Anytone/D578UV_FW_and_MCU_Reset.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/Anytone/D578UV_FW_and_MCU_Reset.pdf) Hub item 14.

!!! warning
    Once the radio is put in the FW update mode you must complete the FW update write, to prevent the radio from staying in the update mode.

1. Power the radio on.
2. Press and hold both the **MENU** and **EXIT** keys. Now power the radio off.
3. The red LED light should now be blinking, and the radio has entered firmware update mode.
4. Use the USB cable to connect the radio to your PC.
5. Open the radio Computer Programming Software (CPS) and go to **TOOLS → Firmware Update**.

    ![CPS Firmware_Update window with Open Update File, Model, Version, Com Port, Com Speed, Duplex and Write and Exit buttons](../assets/img/d578uv-fw-and-mcu-reset/img-01.jpeg)

    *Firmware_Update: Com Port = COM3, Com Speed = 921600, Duplex ticked, Encrypt greyed out.*

6. Select the **Open File** button and select the appropriate D578UV.spi file in the FW Update folder.
7. Check and set the Com Port that is correct for your PC connected to the radio.
8. Select the **Write** button to write the new FW to the radio.
9. After the firmware update is finished, you must perform a reset of the radio (MCU reboot).

## Radio Reset / MCU Reboot

1. To reset the radio: press and hold the two front panel keys **P2** and the **Channel Knob** (the one above the microphone connector). Hold these two keys while turning on the radio and it will reboot the radio into the reset mode.
2. The radio reset screen will appear and ask you to confirm the reset by pressing the **Menu** key on the front panel. The reset itself will take a minute or more.

    ![D578UV front panel showing the prompt "Are you sure you want to initialize radio?" with Confirm and Exit, an arrow pointing at the MENU key](../assets/img/d578uv-fw-and-mcu-reset/img-02.jpeg)

3. After completing the reset, the Calibration Date settings screen will open. You need to set the correct information by using the **Channel Knob**: pushing the Channel Knob will navigate through the GMT, Date and Time fields; rotating the Channel Knob will allow you to change the settings. When finished setting the data, use the **Menu** button to confirm and the radio will reboot.

    ![D578UV Calibrate Date screen with GMT, date and time fields; callouts read "Press Menu key to confirm when you are finished setting the data" and "Push Channel Knob to navigate fields, Rotate Channel Knob to change and set information"](../assets/img/d578uv-fw-and-mcu-reset/img-03.jpeg)

4. After successfully resetting the radio, your codeplug will be gone and the factory smaller version loaded. You should now load your saved codeplug into the radio. Check the Com Port, and from the CPS write your codeplug into the radio. No special set-up is required to write a codeplug into the radio.

## If the radio does not let you do an MCU reset

1. Make sure **Power-on Password** is turned off.
2. Save the codeplug.
3. Now send the codeplug to the radio.
4. Follow the instructions as above in the second part of this document.

## See also

- [How to update CPS and Firmware V8](how-to-update-cps-and-firmware.md)
- [MCU Reset – 868 & 878](mcu-reset-868-878.md)
- [D168UV Firmware Update](at-d168uv-firmware-update-and-mcu-reset.md)
- [Strange or odd things happening v3](../troubleshooting/strange-or-odd-things-happening.md)
