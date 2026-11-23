---
title: Add Talk Groups
item: ["32", "J"]
source_url: https://hamradiosouthernrepeaters.co.uk/images/Anytone/Add_Talk_Groups.pdf
original: ../originals/images/Anytone/Add_Talk_Groups.pdf
tags: [AT-D578UV]
---

# Add Talk Groups

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/Anytone/Add_Talk_Groups.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/Anytone/Add_Talk_Groups.pdf) Hub items 32 and J.

[TOT (Radio Timeout Timer)](../hardware/radio-timeout-timer-180s.md) Must be set to 180s

**CPS → Optional Settings → Other**

![CPS Other tab showing the TOT field](../assets/img/add-talk-groups/img-01.jpeg)

*Optional Settings → Other: TOT = 180s.*

TX Permit = Same, Channel Free, Different Color Code - "Never set to Always"

![CPS channel settings for a digital channel](../assets/img/add-talk-groups/img-02.jpeg)

*Receive Frequency = 434.00000, Transmit Frequency = 434.00000, Correct Frequency [Hz] = 0, Channel Type = D-Digital, Transmit Power = Low, Band Width = 12.5K, TX Permit = Different Color Code.*

---

1st you need to add the Talk Group to TALK GROUPS as a GROUP CALL

![CPS Talk Groups list with numbered entries 9, 91, 2350 and so on, all Call Type Group Call](../assets/img/add-talk-groups/img-03.jpeg)

Double click the next empty line and fill in

![Talk Group Edit dialog for entry 47](../assets/img/add-talk-groups/img-04.jpeg)

*Talk Group Edit: Name = TAC 310, Call Type = Group Call, TG/DMR ID = 310, Call Alert = None (greyed out).*

- (907 - Group Call)
- (91 - Group Call)
- (4000 - Group Call)

Save by clicking OK

Make up a channel for each Talk Group you wish to use.

![CPS channel Digital section showing the Contact field](../assets/img/add-talk-groups/img-05.jpeg)

*Digital: Contact = 9.*

Add each channel to a Zone List.

![CPS Zone list with zones Home, Simplex, DH and Repeater](../assets/img/add-talk-groups/img-06.jpeg)

![Zone channel selection with Available Channel on the left and Zone Channel Member on the right, including BH - TG9 -1, BH - TG9 -23510, BH - TG9 -2, BH - TG9 -4000 and GB7BC - 9 -1](../assets/img/add-talk-groups/img-07.jpeg)

Save Codeplug
Send Codeplug to radio

Turn radio to required ZONE and channel.
TX to open that Talk Group.
Now you can TX and RX in that Talk Group.

4000 - "Group Call" Disconnect from TG

[Brandmeister World Wide Talk Groups](https://brandmeister.network/?page=talkgroups)

[Add Talkgroup via Keypad](https://www.youtube.com/watch?time_continue=5&v=5C_ah-n0Mng&feature=emb_logo)
