---
title: "Hardware faults with the 868 / 878 / 6X2"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#HWFault
tags: [AT-D868UV, AT-D878UV]
---

# Hardware faults with the 868 / 878 / 6X2

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#HWFault)

The 868 / 878 / 6X2 are generally very reliable radios, but sometimes faults will arise. The following is a list of hardware failures noted with the radio so far:

- **Charger constantly flashing red-green-red, even without a battery inserted:** charger base has failed.
- **Radio displays "Checking Flash" or "Bad Block":** faulty or corrupt flash memory; can sometimes be fixed with a reset of the radio.
- **Radio LCD display goes fuzzy or strange during transmit:** faulty display or loose connecting ribbon cables. If you are confident enough, try re-seating the ribbon cables and firmly lock their header retainer into place to fix.
- **Radio freezes on power up:** this is sometimes due to the SCT3258 baseband IC going bad, but sometimes can be fixed by the 'defrost' solutions ([Quick defroster](79-frozen.md) and [Full defroster](80-full-defrost.md)).

These are generally *hardware* issues, which mean the radio needs to go back to your dealer for attention.

99.9% of problems encountered are usually the result of poor 'codeplug' practices. Using other people's codeplugs, originating from several CPS versions back, and then added to piecemeal, is almost certain to cause problems. The solution to this is to ensure your codeplug is rebuilt every time a new CPS or firmware version is released: use the export all function, start a brand new codeplug and quickly rebuild it with the import all feature. This ensures the underlying data that your codeplug is built upon is fresh and consistent with the CPS and firmware version in use.
