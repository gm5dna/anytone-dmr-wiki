---
title: "Expanding RX frequencies Easy"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#ExpandRX
tags: [AT-D868UV, AT-D878UV]
---

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, unchanged, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#ExpandRX)

**Expanding RX frequencies** Easy
*Suitable for 868 / 878 / 878-II / 6X2 / DJ-MD5 / DJ-MD5X*
As delivered by the factory, the 868 covers 136-174 MHz and 400-480 MHz and the 878 covers up to 520 MHz. There are countries around the world that make use of the radio spectrum above 480 MHz for two way radio, and this modification will allow you to hear those transmissions. TX is intentionally inhibited in these expanded areas. *The modification only opens up the radio hardware, some tricks are still necessary to program out of band frequencies with the software.*
At the heart of the 878 is an AT1846S 'radio-on-a-chip' that is designed to work from 134-174 MHz, 400-520 MHz and 200-260 MHz. In practice, the chip will cover even more than that, as you will soon see.

![](../../originals/images/878Mods/freqexpandLCD.jpg)


To carry out this modification do the following:
PLEASE GO TO THIS PAGE FOR MORE UPTO DATE INFO AND FILES - [https://hamradiosouthernrepeaters.co.uk/20-expanding-rx-frequencies.html](../expanding-rx-frequencies.md)

1.  
2.  Download **frequency expanded modified firmware package (6.0Mb)** which contains firmware packages for all models 868 / 878 / 878-II / 6X2 / DJ-MD5 / DJ-MD5X from:
    [Download via Mega](https://mega.nz/file/T5NHCaLZ#H1qSJiLNFck_5wg6a3mrUuayXA60RA66VPjR8NVzj-Q)
    [Download via Google Drive](https://drive.google.com/file/d/1wzIPMA75ZUsbt_iwF7sCLmtLPJsXo-gh/view?usp=sharing)
    [Download via Sabercat host](https://sabercathost.com/a1ge/mod_firmware.zip)
3.  Unzip the package, and look for your model radio in the folders
4.  Make sure you have saved your codeplug (rdt) configuration file
5.  Using the regular firmware updating software & process, send this frequency expanded firmware to the radio.
6.  If necessary, update your codeplug / rdt configuration file to be compatible with the version of firmware you have downloaded. If you want to reuse your saved codeplug rdt configuration file, you may need to modify one byte with a hex editor as detailed below in italics.
7.  Enjoy ***actual*** extra receive frequency coverage of around **130-178 MHz, 195-290 MHz (with a gap between 200-210 MHz on the 868 & 6X2) and 390-527 MHz (varies from individual radio to radio)**

Your mileage may vary of course, due to individual radio & component manufacturing tolerances. You can use the VFO and add memory channels to use these new expanded receive frequency ranges. Sometimes, you can't enter frequencies via keypad direct entry that start with a 2, 3 or 5 (e.g. any frequency in the 200, 300 or 500 MHz range) the only way to get to them is via lots of knob twisting in VFO mode or use the up/down buttons to tune in 1 MHz steps.

***To enter out of band frequencies in the CPS programming software***, you will need to use the export-edit-import method: program some dummy channels with valid but easy to recognise frequencies, for example 456 MHz, then use the export feature (tool \> export \> channel \> give it a name \> export) and save your exported channels. Open the exported channels file with a text editor - look for your dummy channels you had previously entered, and edit the frequencies as you require, and save the file. Back in the CPS software, use the import feature (tool \> import \> channel \> find your edited csv file \> import) to bring the channels with out of band edited frequencies into the radio.

***But how do we know it is actually working, not just displaying a frequency and nothing else?*** Conveniently, the 878 has a quirk that will tell you if the receiver is 'unlocked' and not working at that frequency: program a button as FM monitor, or turn the squelch level to off. If the radio makes a pulsing or popping noise, the receiver is unlocked and is too far out of band to work. If you hear a constant rush of noise, that indicates the receiver is locked and is working as well as it can do.
If you have a signal generator, you can test that the 878 is actually receiving this signal, or you can use an off air signal to confirm reception is working.
*Transmit remains standard according to each MODE.* Typically, the receiver locks and actually works around 130-178 MHz, 195-290 MHz (with a gap between 200-210 MHz on 868 / 6X2) and 390-527 MHz, though note that frequencies between 210-400 MHz vary in sensitivity quite a bit.

Also included with the frequency expanded firmware package is an alternate font which can be a bit easier to see than the original. Here is an example of what the new alternate font looks like if you are interested.

![](../../originals/images/878Mods/newfontexample.jpg)
