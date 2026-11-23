---
title: Strange or odd things happening v3
item: "21"
source_url: https://hamradiosouthernrepeaters.co.uk/images/Anytone/Strange_or_odd_things_happening.pdf
original: ../originals/images/Anytone/Strange_or_odd_things_happening.pdf
tags: [AT-D168UV, AT-D868UV, AT-D878UV, AT-D578UV]
---

# Strange or odd things happening v3

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/Anytone/Strange_or_odd_things_happening.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/Anytone/Strange_or_odd_things_happening.pdf) Hub item 21.

Seems like lots of people are suffering lots of strange or odd things happening with their Radios. Can't program buttons with functions you want / APRS not working etc

I found this process helps in many cases:

## How to rebuild Codeplug

1. In CPS, export everything (**Tool → Export → Export All**)
   \*Also write down or photograph all the Optional Settings.
2. MCU RESET [868/878](../cps-firmware/mcu-reset-868-878.md) & [578](../cps-firmware/d578uv-fw-and-mcu-reset.md) & [D168 in step 9](../cps-firmware/at-d168uv-firmware-update-and-mcu-reset.md) the radio - this step is very important!
3. Close and re-open the CPS. Now read from the freshly reset radio (yes, you are reading a ’blank’ radio, that is OK)
4. Import everything saved from step 1 (**Tool → Import → Import from File list**)
   (In newer CPS you can export and import Optional Settings. DO NOT re import Optional Settings. Go to the folder you saved the Exported CSVs and Delete OptionalSetting.CSV)
5. \*Finish off your codeplug by filling in the Optional Settings you took down in No1.
6. Send the freshly rebuilt codeplug to the radio.
7. If you had a custom start up picture or background pictures, send those to the radio now.
8. Finally, save the codeplug and ensure you use this saved file as the basis for any further changes you may make.

Also you might want to read [AES256/ARC4 encryption CSV Export/Import](../encryption/aes256-arc4-encryption-csv-export-import.md)
