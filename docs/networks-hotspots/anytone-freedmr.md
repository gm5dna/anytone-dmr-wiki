---
title: Anytone FreeDMR
item: "147"
source_url: https://hamradiosouthernrepeaters.co.uk/images/Anytone/Anytone_FreeDMR.pdf
original: ../originals/images/Anytone/Anytone_FreeDMR.pdf
tags: []
---

# Anytone FreeDMR

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/Anytone/Anytone_FreeDMR.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/Anytone/Anytone_FreeDMR.pdf) Hub item 147.

Two ways to use an Anytone Radio on FreeDMR without adding Talk Groups as Channels.

## 1. Manual Dial Talk Groups Direct

### In the CPS

**CPS → Optional Settings → Digital Func**

Set your hang time to 30mins in this section.

![CPS Manual Dial - Group TG Hold Time set to 30min](../assets/img/anytone-freedmr/img-01.png)

*Manual Dial - Group TG Hold Time = 30min.*

### Now via the radio

1. Go to ANY channel for your HotSpot or Local Repeater on the FreeDMR Network. This can be Slot 1 or Slot 2.
2. Long press **0** key – display will show **Private ID**.
3. Press **#** key – display will show **Talk Group ID**.
4. Type in the Talk Group you want to use – 2350.
5. **PTT** for 3 sec.

You are now on Talk Group 2350.

The radio will stay on that Talk Group for 30 mins from your last PTT. After 30mins it will default back to the Talk Group of the Channel you started with.

You can link to any Talk Group as described above.

!!! note
    You could set the hang time to Infinite. But I would not recommend this.

![CPS Manual Dial - Group TG Hold Time set to Infinite](../assets/img/anytone-freedmr/img-02.png)

*Manual Dial - Group TG Hold Time = Infinite.*

**OR this way:**

## 2. Dial-a-TG on FreeDMR

<http://www.freedmr.uk/index.php/linking-to-talk-groups-via-tg9/>

### In the CPS

**CPS → Optional Settings → Digital Func**

Set your hang time to 3sec in this section.

![CPS Manual Dial - Private TG Hold Time set to 3s](../assets/img/anytone-freedmr/img-03.png)

*Manual Dial - Private TG Hold Time = 3s.*

CPS make a channel:

1. Add 9 in Contact/Talk group as **GROUP CALL**.
2. Make a Channel up for Talk Group 9 on Slot 2 and then add to a Zone you wish to use it in.

This is the only Talk group you will need for a QSO on Dial-a-TG.

### Now via the radio

1. Go to channel TG9 on Slot 2 for your HotSpot or Local Repeater on FreeDMR Network.
2. Long press **0** key – display will show **Private ID**.
3. Type in the Talk Group you want to use – 2350.
4. **PTT** for 3 sec.

The repeater/hotspot will respond with a voice announcement “Linked to 2350.“ “Voice announcements come back on 5000.”

Then via Talk Group 9 you can QSO on that Talk Group. You can link to any Talk Group as described above.

## 4000 Unlink

FreeDMR you can move to a new Talk Group without doing a 4000. PTT for up to 3 seconds on the new Talk Group you wish to use. Now you can TX and RX in that Talk Group.

### Via TG9 Slot 2 Enhanced Talk Groups Dial-a-TG

Manual Dial **4000 Private Call** transmit for up to 3 sec. The repeater / hotspot will respond with a voice announcement “Not Linked”.

!!! tip
    You can move to a new Talk Group without doing a 4000. Just call the next Talk Group and PTT for up to 3 sec.

Would be recommended to make a 4000 unlink channel. Add 4000 as a Private call to the radio. Set TG9 in the RX Group. Now when you get a GAP in RX you can PTT and unlink.

<http://www.freedmr.uk>
