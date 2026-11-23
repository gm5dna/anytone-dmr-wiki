---
title: "Future developments & ideas"
source_url: https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#Future
tags: [AT-D578UV]
---

# Future developments & ideas

[← All 578 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#Future)

- Exploiting the capabilities of the TLV320AIC3204 audio codec chip. This is a very powerful chip with the possible scope to facilitate DSP noise reduction, equalisation, tone control and digital AGC audio.
- Explore some new fonts, perhaps some screen colour changes and icon customisation.
- Investigate if the display unit could be remote mounted by use of a longer 40 pin ribbon cable and a custom 3D printed backing plate for physically mounting the head.
- Patching the vocoder in the SCT3258 for something else entirely. There is a very strong resemblance between AnyTone’s SCT3258TD_UpdateFlash_v2_01_05NJ.hex and Hytera’s PD36x series SCT3928_UpdateFlash_V2_01_05PD.hex - both in name and hex content. The Hytera can already load different hex files for AMBE, SELP, NVOC & COMM vocoders, but this is slightly dependant on the different hardware installed in the Hytera radios. It would be very interesting to experiment with an open source ham vocoder like FreeDV’s Codec2, and see if this could be used to replace the AMBE2+ vocoder in the SCT3258. Sadly the SiComm hex code that gets sent to the SCT3258 is encrypted, so for the moment any patching is unlikely.

---

© Copyright Jason Reilly, 2018-2022

*Except as permitted by the copyright law applicable to you, you may not reproduce or communicate any of the content on this website, including files downloadable from this website, without the permission of the copyright owner.*
