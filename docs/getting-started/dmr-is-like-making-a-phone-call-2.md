---
title: DMR is like making a phone call V3
item: "39"
source_url: https://hamradiosouthernrepeaters.co.uk/images/PDF/DMR_is_like_making_a_phone_call_2.pdf
original: ../originals/images/PDF/DMR_is_like_making_a_phone_call_2.pdf
tags: [AT-D578UV]
---

# DMR is like making a phone call V3

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/PDF/DMR_is_like_making_a_phone_call_2.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/PDF/DMR_is_like_making_a_phone_call_2.pdf) Hub item 39.

[Talk Groups](http://hamradio.joomla.com/dmr-info/2-uncategorised/61-access-talk-groups.html) are just like phone numbers.

Zones are your address book, A to Z.

Channels are the frequency you wish to talk over. This could be your local repeater, simplex or hotspot.

| | Phone lines | Slots |
|---|---|---|
| DMR repeater | 2 phone lines: Line 1 and Line 2 | Line 1 is called Slot 1; Line 2 is called Slot 2 |
| DMR simplex hotspot | 1 phone line: Line 2 normally | Line 2 is called Slot 2 |
| DMR duplex hotspot | 2 phone lines: Line 1 and Line 2 | Line 1 is called Slot 1; Line 2 is called Slot 2 |

Talk Groups are all the phone numbers you wish to call: TG9, TG2350, TG2351, TG2352, TG310, TG91 etc.

## Now for the fun part and making a call

So we will work a local DMR repeater, and at this point we need to know:

1. What phone (DMR) network we will be using.
2. This could be [FreeDMR](http://www.freedmr.uk/index.php/contact-support/how-to/), BrandMeister, Phoenix, DMR+, or another provider.
3. The networks do not talk to other networks in general.
4. You need to know, do they use Talk Groups.
5. As a rule Talk Groups are on Line 1 (Slot 1), but some networks use Slot 2 also.

    *(Simplex / duplex hotspots can use Slot 2 for reflectors or Talk Groups.)*

6. All reflectors only work on Line 2 (Slot 2).
7. You will also need to know what Color Code the repeater is using.

## An example that will work on all networks

In this next stage, I will do an example that will work on all networks.

1. We need to know the frequency of the repeater, RX and TX.
2. We need to know what Talk Groups it offers.
3. (Example) Talk Group 9 is normally the default for local talk to all within range of the repeater.
4. We need to know the repeater's Colour Code.

(TG9 via hotspots is not required, unless you use reflectors on Slot 2.)

### First: add the Talk Group

(Example) First we need to add 9 to the Talk Group list (9 is the phone number). Talk Groups are always added as a **Group Call**.

![CPS Talk Groups list with TG/DMR ID, Call Alert, Name and Call Type columns](../assets/img/dmr-is-like-making-a-phone-call-2/img-01.jpeg)

*Talk Groups: 9, 91, 2350 to 2355, 2357, 4000 (named "4000 Group") and 5000, all with Call Alert = None and Call Type = Group Call.*

### Second: make a channel for the repeater

We will be talking on Talk Group 9 for local chat on Slot 1.

![CPS Channel Information Edit window for channel GB7BC - 9 -1](../assets/img/dmr-is-like-making-a-phone-call-2/img-02.jpeg)

*Channel GB7BC - 9 -1: Receive Frequency 439.65000, Transmit Frequency 430.65000, Channel Type = D-Digital, Transmit Power = Low, Band Width = 12.5K, TX Permit = Different Color Code, Contact = 9, Color Code = 3, Slot = Slot1, DMR MODE = Repeater.*

You will see in the right-hand box **Contact**. This is where you point to the Talk Group you wish to talk on (phone number). Again, in this example it is 9. It can be any number you have added in the step above. We also want it to be on Slot 1 (Line 1).

Name the channel what is best for you. I have used the repeater name – 9 the Talk Group – 1 as it is on Slot 1.

I will skip over all the other settings. You can use the ones as shown in the photo above, apart from the frequency and Color Code.

Radio ID I will go over later in this document.

### Third: add that channel to your address book (Zone)

![CPS Zone Edit window with channel GB7BC - 9 -1 as a Zone Channel Member](../assets/img/dmr-is-like-making-a-phone-call-2/img-03.jpeg)

*Zone Edit: Zone Name = Home, A Channel and B Channel = GB7BC - 9 -1; Zone Channel Member 96 GB7BC - 9 -1.*

That is it. Save the file (“codeplug”) and send it to the radio.

So now, via the radio, you can go to the zone and select the channel that lets you talk on Slot 1 to Talk Group 9. When you PTT the radio you will be talking on Talk Group 9 via that repeater.

If you wish to talk on another Talk Group, you just follow the steps above.

## Radio ID list

This is your personal phone number ([request your DMR ID number](https://www.radioid.net/register#!)). It is made up of 7 digits. This is the ID number that is sent out every time you press the **PTT**.

Radio ID Name is what you want your radio called.

!!! warning
    Without a valid ID number you cannot use ham radio DMR networks.

![CPS Radio ID Edit window](../assets/img/dmr-is-like-making-a-phone-call-2/img-04.jpeg)

*Radio ID Edit: Radio ID = 1234567, Radio ID Name = M6NBP Norman Brighton. UK.*
