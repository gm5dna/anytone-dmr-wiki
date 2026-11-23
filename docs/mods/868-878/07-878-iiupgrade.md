---
title: "Can you upgrade an 878 to an 878-II SUPER Advanced"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#878-IIupgrade
tags: [AT-D868UV, AT-D878UV]
---

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, unchanged, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#878-IIupgrade)

**Can you upgrade an 878 to an 878-II** SUPER Advanced
Technically, yes this could be done, however it would be beyond the capabilities of 99.99% of people. You would need to:

- Change the WSON8 epad surface mount 1Gbit flash chip to a 2Gbit flash chip. The 878-II firmware checks for the presence of 2Gb of flash, and if it does not find it, will abort power up. Swapping this IC requires specialist equipment like SMD hot air reworking station and you need to be highly skilled in SMD reworking to safely achieve this swap without damaging the main board or other surrounding components
- Obtain the new combination FSK / Bluetooth daughter board and fit. There is a small wire to also solder from the daughter board to the main PCB as well
- And lastly, you'll need to force the 878-II firmware into the 878. The QX-update software used for this purpose has checks to prevent the user from doing that, but they can by bypassed if you know what you are doing

Considering these points, I definitely do not recommend doing this, it would be safer and easier to just buy the 878-II if you really want analog APRS receive or 500000 digital ID contacts.

------------------------------------------------------------------------
