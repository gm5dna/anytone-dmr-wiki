---
title: How to update CPS and Firmware V8
item: "17"
source_url: https://hamradiosouthernrepeaters.co.uk/images/Anytone/How_to_update_CPS_and_Firmware.pdf
original: ../originals/images/Anytone/How_to_update_CPS_and_Firmware.pdf
tags: [AT-D168UV, AT-D868UV, AT-D878UV, AT-D578UV]
---

# How to update CPS and Firmware V8

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/Anytone/How_to_update_CPS_and_Firmware.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/Anytone/How_to_update_CPS_and_Firmware.pdf) Hub item 17.

## Before you start

Make sure you have a backup of your old code plug saved.

Do the following (see \*encryption below):

1. Install New CPS.
2. Open New CPS.
3. Read Radio to the NEW CPS and **Save** Code plug.
4. Start radio in Firmware mode. (Read Documents in Download)
5. Flash New Firmware.
6. Turn radio OFF.
7. Turn radio ON to let the firmware load.
8. Turn radio OFF.

<!-- -->

8. Do MCU Reset. ([168](at-d168uv-firmware-update-and-mcu-reset.md)) ([868 & 878](http://hamradio.joomla.com/images/Anytone/MCU_Reset__868__878.pdf)) and ([578](http://hamradio.joomla.com/images/Anytone/D578UV_FW_and_MCU_Reset.pdf)) - this step is very important!
9. **Close CPS and re-open the CPS and CP again.**
10. Send your NEW Saved Code plug to radio.
11. If you had a custom start up picture or background pictures, send those to the radio now if required.
12. Read radio back to CPS.
13. Send CP back to radio.
14. Finally, save the Code plug and ensure you use this saved file as the basis for any further changes you may make.

That is it.

## \*Encryption

!!! warning
    Some encryptions **cannot** be read from the radio back to a CPS.

    - AES256/ARC4 encryption code can only be written to the radio, not read from the radio.

Read this on [how to Export/Import CSV](../encryption/aes256-arc4-encryption-csv-export-import.md) on newer CPS versions.

You might need to rebuild your code plug if you have any issues. See link below.

You might also want to read: [Strange or odd things happening](../troubleshooting/strange-or-odd-things-happening.md)

## See also

- [MCU Reset – 868 & 878](mcu-reset-868-878.md)
- [D578UV Mobile Radio Firmware Update Instructions](d578uv-fw-and-mcu-reset.md)
- [D168UV Firmware Update](at-d168uv-firmware-update-and-mcu-reset.md)
- [Strange or odd things happening v3](../troubleshooting/strange-or-odd-things-happening.md)
