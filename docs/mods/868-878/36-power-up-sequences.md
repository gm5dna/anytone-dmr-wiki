---
title: "Known button held during power up sequences"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#PowerUpSequences
tags: [AT-D868UV, AT-D878UV]
---

# Known button held during power up sequences

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#PowerUpSequences)

There are several power up sequences which involve holding down buttons to invoke certain modes on the 878 as follows:

| Hold while powering up | Mode |
|---|---|
| Top orange / blue button + **PTT** | Main firmware update mode |
| Top orange / blue button + **#** | DSP SCT update mode (equivalent on Alinco DJ-MD5 is **PTT** + **#**) |
| Top orange / blue button + **PF1** (878 only) | Enters a 'Record USB mode' where you can manage playback of recorded DMR audio via the CPS **Tool → Record** menu, but you need a custom programming cable to do this. Credit to Juan EB2DVG & Francesco IK8JHL |
| **PTT** + **PF1** | Enters the reset radio confirmation menu – but ONLY if this option is enabled in CPS first! |
| **PTT** + **PF2** | Enters a display icon update mode |
| **PTT** + **1** | Enters test mode where you can select operational bands ("modes") and/or adjust alignment parameters – but ONLY if enabled by use of the AT Options v8 application first! |
| **PTT** + **2** | Enters a GPS signal strength (RSSI) test mode – only on 878 from firmware V1.10 onward. Credit to IK8JHL |
| **PTT** + **3** | Enters a GPS module test mode |
| **PTT** + **7** | Enters an adjustment mode, equivalent to **PTT** + **1** (Alinco DJ-MD5 only) |

Some of these sequences require you to hold the buttons for up to ten seconds before they take effect.

## Test mode access levels

The test mode (**PTT** + **1**) has three levels of access:

1. Normally, test mode will be completely inhibited as delivered by the factory.
2. With 'band select' test mode, you will only be able to select MODE to change operational frequency bands of the radio.
3. In full unlocked test mode, some degree of calibration / alignment is possible from the front panel of the radio for deviation levels, power output levels, received signal strength indication (RSSI) levels, squelch levels, frequency fine setting and more.

See [Enabling full test / self adjustment mode](64-full-test-mode.md) for more detail.
