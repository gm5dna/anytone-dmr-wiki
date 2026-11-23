---
title: "Hotspot Offset Calibration"
source_url: https://hamradiosouthernrepeaters.co.uk/dmr-info/2-uncategorised/63-hotspot-offset-calibration.html
tags: []
---

# Hotspot Offset Calibration

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Source](https://hamradiosouthernrepeaters.co.uk/dmr-info/2-uncategorised/63-hotspot-offset-calibration.html)

To use pistar-mmdvmcal to calculate TXoffset  
A. Preliminaries:- Set DMR rig to desired hotspot [\*frequency](hotspot-offset-calibration.md), CC1 Slot1 TG9. Call it Fd (in Hz) In Pistar set TXoffset and RXoffset to zero, otherwise they'll screw up the calculation.  

B. connect to your pi-star setup with ssh.  

C. Type:- sudo pistar-mmdvmcal" &lt;enter\>  

D. Tap E key & enter TX frequency, Fd, of your hotspot in Hz  

F. Tap &lt;M\> key. Hotspot generates a dmr tone.  

G. Tap &lt;Space\> Hotspot transmits tone. You should hear tone on rig.  

H. Repeat presses on f key until tone disappears. Note this frequency as f.  

I. Repeat presses on F key until tone reappears, keep going until it disappears again. Note this frequency as F.  

J. Q to quit.  

The calculation:  
You have 3 frequencies, Fd, f and F to play with. f is the lower edge of the hotspot transmission and F is the upper edge of the hotspot transmission. Assuming the transmission is symmetrical around its peak value, the average of f & F gives the peak frequency of the hotspot transmission ie where it is actually transmitting.  

So the hotspot is TXing at freq. {(F+f)/2} Hz  
TXoffset is the difference between rig and hotspot TX frequencies.  

TXoffset = Fd - {(F+f)/2}  

TXOffset & RXoffset don't have to be the same, but for starters set both to the calculated value.  
If ber isn't good, vary RXoffset only until it is. That's about it.  

Thanks to Vic Simpson for this  

You might also want to look at this [link](http://www.k9npx.com/2019/02/hotspot-offset-calibration.html?&m=1)  

![Hotspot offset calibration](../originals/images/RADIO/Hotspot_Offset_Calibration.jpg)

\*UK Hotspot Frequencies  
434.000 [Low Power Non-NoV Personal Hot-Spot](https://rsgb.services/public/bandplans/html/rsgb_band_plan_2019.htm)438.800 [Low Power Non-NoV Personal Hot-Spot](https://rsgb.services/public/bandplans/html/rsgb_band_plan_2019.htm)
