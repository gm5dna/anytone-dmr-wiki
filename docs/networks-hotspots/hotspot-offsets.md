---
title: Hotspot Offsets
item: "K"
source_url: https://hamradiosouthernrepeaters.co.uk/images/Anytone/Hotspot_Offsets.pdf
original: ../originals/images/Anytone/Hotspot_Offsets.pdf
tags: []
---

# Hotspot Offsets

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/Anytone/Hotspot_Offsets.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/Anytone/Hotspot_Offsets.pdf) Hub item K.

First I want to make it clear that the **radio is not off frequency**. It is the hotspot that is, and that is why all hotspots offer offsets to bring them in line with each radio.

| Hotspot | Setting |
|---|---|
| Pi-Star | Offsets (Run Calibration) |
| OpenSpot | AutoCal (Run AutoCal) |
| BlueDV | QRG (default is -50) |

You could have a hotspot and 5 DMR radios. If you're lucky all 5 will fall within 0 to minus -250, but on the other hand all 5 could require different offsets. This is 100% normal.

You also could have 5 hotspots and two radios. If you're lucky all 5 will fall within 0 to minus -250, but on the other hand all 5 could require different offsets. This is 100% normal.

## What happens if two radios require different offsets to work with the hotspot?

You have two options.

1. Change the offset in the hotspot each time for each radio.
2. Anytone radios let you set the offset in each channel rather than in the hotspot. (*Anytone radios are one of a few manufacturers I know of that let you do this.*)

![CPS Channel Information Edit with the Correct Frequency [Hz] field highlighted](../assets/img/hotspot-offsets/img-01.jpeg)

*Channel Information Edit: Channel Name Hot 9, Receive Frequency 434.00000, Transmit Frequency 434.00000, Correct Frequency[Hz] = 0 (underlined in red).*

You work out the correction and then enter it. Repeat this on each hotspot channel. Save the channel and now send the codeplug to the radio.

## A post by Markus Große-Schware

### The problem

MMDVM hotspots usually are somewhat off frequency (often some 100 Hz), but very picky if radios don’t hit their frequency. To do the job with only one radio, adjust the hotspot frequency (see above).

If you use more than one radio with a hotspot, you might find that radios often are a little off frequency too, not all in the same direction and by different amounts. Therefore, always changing the offset of the MMDVM makes no sense.

### The easy way

You should adjust the second (3rd, 4th, …) radio to the hotspot by tuning it in with the offset setting you can find in the channel setting of that radio (your hotspot channel).

### The perfect way

The „golden“ solution would be to adjust the MMDVM and all of your radios 100% exactly to the target frequency. This is possible too, but you need a reliable and quite exact frequency counter for it.

If you need further help you should ask in the Facebook groups for your hotspot: Pi-Star, OpenSpot, BlueDV etc.

## See also

- [Hotspot Offset Calibration](../dmr-nxdn/hotspot-offset-calibration.md)
- [Hotspot Users BER rate V2](hotspot-users-ber-rate.md)
