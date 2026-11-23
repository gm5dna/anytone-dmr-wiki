---
title: DMR is like a Phone Call
item: "103"
source_url: https://hamradiosouthernrepeaters.co.uk/images/Anytone/DMR_is_like_a_Phone_Call.pdf
original: ../originals/images/Anytone/DMR_is_like_a_Phone_Call.pdf
tags: []
---

# DMR is like a Phone Call

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/Anytone/DMR_is_like_a_Phone_Call.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/Anytone/DMR_is_like_a_Phone_Call.pdf) Hub item 103.

DMR is very much like using a mobile phone. *([Also see this link](dmr-is-like-making-a-phone-call-2.md))*

**Radio** is the phone you make calls from.

**Hotspots and DMR repeaters** are the exchange that routes the phone number / talk group to a group chat (conference call) that anyone can join. That is why it is called Group Call (conference call).

**Frequencies** are your RF phone line that your traffic is passed on. So the freq never changes, just the phone number (talk group). Hotspots use frequencies 434.000 and/or 438.800. Repeaters have their own frequencies.

Look at it this way:

- **Talk group** is a phone number you wish to call (91, 3100, 2350, etc).
- Then a **4000** group call is the hang-up request (disconnect/unlink).

So **channels/talk groups** are pre-set phone numbers. This is the list of phone numbers (talk groups):

- FreeDMR: <http://www.freedmr.uk/index.php/talkgroups/>
- Brandmeister: <https://brandmeister.network/?page=talkgroups>
- Phoenix UK: <https://dvsph.net/>

**Zone** is like an address book for your favourite phone numbers (talk groups). So we make a zone "Hotspot" that has the channels/phone numbers you wish to use.

## How to make a channel

1. Add the talk group number (phone number) to **Talk Groups/Contacts**.
2. Make channels on the frequencies you need to use. Point that channel to the talk group (phone number).
3. Add it to the zone you want it in (address book).

## Slots

**Slots** are like a shared phone line that can have two using it at the same time. One can be on Slot 1 while another can be on Slot 2.

- *Simplex hotspots do not use slots. Set all channels to Slot 2.*
- *Duplex hotspots and repeaters use slots and you need to look up how they want them used.*

## Private calls

You can do a [Private Call](../operating/private-call-anytone.md) between you and one other.

1. Take the other party's ham radio 7-digit ID number (phone number).
2. Add it to **Talk Groups/Contacts** as a **Private Call**.
3. Make the channel up the same as above and add it to a zone.

(Downside is the other party must be on the same network and have the radio turned on.)

!!! note "Side note"
    Private Call is no longer private. The Anytone will decode private calls if Digi Moni is turned on. Even on hotspots, if someone is on the same freq and within range of your hotspot.
