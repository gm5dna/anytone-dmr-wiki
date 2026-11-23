---
title: "Swapping Btech DMR-6X2 firmware into an AnyTone AT-D878UV Moderate"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#SwapFW
tags: [AT-D868UV, AT-D878UV]
---

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, unchanged, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#SwapFW)

**Swapping Btech DMR-6X2 firmware into an AnyTone AT-D878UV** Moderate
(Credit to Ronan EI4KN)
If you would like to experiment with some of the features of the Btech DMR-6X2 (e.g. store & forward repeater) in the AnyTone AT-D878UV, then this simple hex edit hack will permit you to do that. Simply load the Btech DMR-6X2 .SPI file in your favourite hex editor, and shorten it to 14 bytes long. Save it, and then you'll be able to load that firmware into the AnyTone AT-D878UV. There will be a few icons that are blank or missing, the radio might start up in Chinese language but otherwise it functions fine. Newer versions of the Btech DMR-6X2 firmware causes the AnyTone AT-D878UV to 'black screen', but is recoverable by reloading AnyTone AT-D878UV firmware again. This is likely due to minor differences in the contents of flash memory between the 878 and 6X2.
The reverse is also true: AnyTone AT-D878UV firmware can be loaded into the Btech DMR-6X2, but this will require the 878 bootloader to be written into the 6X2 (see the section about converting an 868 to 878)

[If you need a good hex editor, download HxD in your preferred language here (about 860kb)](https://mh-nexus.de/en/downloads.php?product=HxD)

------------------------------------------------------------------------
