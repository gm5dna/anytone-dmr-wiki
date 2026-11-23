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

First I want to make it clear that the RADIO is not off Frequency.
It is the Hotspot that is, and why all hotspots offer Offsets to bring them inline with each radio.

Pi-Star = Offsets. (Run Calibration)
OpenSpot = AutoCal (Run AutoCal)
BlueDV = QRG (Default is -50)

You could have a Hotspot and 5 DMR radios.
If your lucky all 5 will fall within 0 to minus -250
But on the other hand all 5 could require different offsets.
This is 100% normal.

You also could have 5 hotspots and two radios.
If your lucky all 5 will fall within 0 to minus -250
But on the other hand all 5 could require different offsets.
This is 100% normal.

**What happens if two radios require different offsets to work with the hotspot?**
You have two options.

1. Change the offset in the hotspot each time for each radio.
2. Anytone radio lets you set the offset in each channel rather than in the hotspot. (*Anytone radios are one of a few manufacture I know off that lets you do this.*)

![CPS Channel Information Edit with the Correct Frequency [Hz] field highlighted](../assets/img/hotspot-offsets/img-01.jpeg)

*Channel Information Edit: Channel Name Hot 9, Receive Frequency 434.00000, Transmit Frequency 434.00000, Correct Frequency[Hz] = 0 (underlined in red).*

You work out the correction and then enter it.
Repeat this on each Hotspot Channel.
Save the channel and now send Codeplug to radio.

## A post by Markus Große-Schware

The problem:
MMDVM hotspots usually are somewhat off frequency (often some 100 Hz), but very picky, if radios don’t hit their frequency.
To do the job with only one radio, adjust the hotspot frequency (see above).
If you use more than one radio with a hotspot, you might make the experience that radios often are a little off frequency too, not all in the same direction and in different amounts.
Therefore, always changing the offset of the MMDVM makes no sense.
The easy way:
You should adjust the second (3rd, 4th,…) to the hotspot by tuning it in with the offset setting You can find in the channel setting of that radio (your hotspot channel).
In the perfect way:
The „golden“ solution would be to adjust the MMDVM and all of Your radios 100% exactly to the target frequency. This is possible too, but You need a reliable and quite exact frequency counter for it:

If you need further help you should ask in the Facebook groups for your hotspot. Pi-Star, OpenSpot, BlueDV etc
