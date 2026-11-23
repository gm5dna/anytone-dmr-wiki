---
title: Radio Timeout Timer 180s
item: "18"
source_url: https://hamradiosouthernrepeaters.co.uk/images/Anytone/Radio_Timeout_Timer_180s.pdf
original: ../originals/images/Anytone/Radio_Timeout_Timer_180s.pdf
tags: []
---

# Radio Timeout Timer 180s

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/Anytone/Radio_Timeout_Timer_180s.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/Anytone/Radio_Timeout_Timer_180s.pdf) Hub item 18.

!!! warning "TOT (Radio Timeout Timer) must be set to 180s"
    **Anytone → CPS → Digital Fun → Other → TOT = 180**

This is set to 180 seconds so repeaters, bridges etc do not time out.

When you talk past 180s, the repeaters, bridges etc time out and they stop receiving you. They think you have stopped your TX and reply back, but both sides miss each other's QSO.

This also applies if you use a hotspot and the other party is on a repeater or bridge.

So please always set your TOT to 180 seconds. A 3 minute maximum QSO is a long over. It also lets others reply back.

## Why 180?

1. When you open a talk group or reflector, i.e. 4401, you will not hear anything until the 1st over is finished and the next one starts. The longest you should have to wait is 180s or less.
2. If someone talks longer than 180s and the reply does a quick key, repeaters might not have reset and will continue till it hits 240s and then drops out, and you're left talking to yourself.

    If one talks for 180 and the next quick keys and talks for 60s then un-keys, then the repeaters reset but nothing was lost between users.

3. This is why at the end of an over a 1 to 5 sec gap should be left, so repeaters and bridges can reset. It also lets others break in.
4. If you are using a hotspot and you have TOT set to Always, and you talk on any reflector that is linked to a repeater and talk over 240s, that repeater drops out and they think you have finished and reply. Both sides are no longer talking to each other.

    This happens on a daily basis and they keep blaming the network, when it is user error.

5. Having mixed mode repeaters set to unlimited means the other modes can be locked out. Also bridges will drop out as they also have time-outs set.
6. If a repeater gets into a loop or stuck, it should stop all TX at 240s and reset.
