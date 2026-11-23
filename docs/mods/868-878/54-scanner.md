---
title: "Can the 878 be used as a scanner?"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#Scanner
tags: [AT-D868UV, AT-D878UV]
---

# Can the 878 be used as a scanner?

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#Scanner)

The AnyTone 868 & 878s can be used as a scanner for FM & DMR in some circumstances. Here's a quick run-down of what you will need to know for using the AnyTones for scanning DMR:

## Simplex / direct mode DMR

This is easy, just program in the frequency, set the channel as DMR MODE = Simplex, set digital monitor mode to on and you'll hear everything.

## Simplex Dual Capacity Direct Mode (DCDM) DMR

This is easy, just program in the frequency, set the channel as DMR MODE = Double Slot, set digital monitor mode to on and you'll hear everything.

## Standard Tier2 repeater

This is also easy, program in the repeater output TX frequency, set the channel as DMR MODE = Repeater and tick the DataACK Disable box, set digital monitor mode on and you'll hear everything. Sometimes the top LED will light but no voice will come out, this is fine, that is just the repeater sending idle or beacon packets to let the radios know the repeater is still alive.

## Motorola IP Site Connect DMR repeater scanning

This is the same as a standard Tier2 repeater, just with multiple repeaters linked by an internet connection. Same setup applies: program in the repeater output TX frequency, set the channel as DMR MODE = Repeater and tick the DataACK Disable box, set digital monitor mode on and you'll hear everything. Sometimes the top LED will light but no voice will come out, this is fine, that is just the repeater sending idle or beacon packets to let the radios know the repeater is still alive.

## Motorola Capacity Plus (previously known as Linked Capacity Plus)

This is a Motorola unique pseudo trunking system that uses no control channel. Rather, radios listen on a 'rest channel' and when a call is made, the 'rest channel' becomes a voice channel for the call. All other radios not involved in that call then listen out on the next defined 'rest channel' until the original call clears. Since Capacity Plus uses the same CAI (Common Air Interface) as regular DMR for voice calls, the AnyTone DMR radios can listen only to such a system by entering each frequency of the system and scanning those frequencies while using digital monitor. Following a voice call as it progresses & jumps frequencies due to trunking nature of the system results in discontinuity of listening at times. Program in all the repeater output TX frequencies, setting each channel as DMR MODE = Repeater and tick the DataACK Disable box, set digital monitor mode on and you'll hear everything. Sometimes the top LED will light but no voice will come out, this is fine, that is just the repeater sending idle or beacon packets to let the radios know the repeater is still alive.

## Motorola Connect Plus

This is a Motorola unique full trunking system that has a dedicated control channel. Since Connect Plus uses the same CAI (Common Air Interface) as regular DMR for voice calls, the AnyTone DMR radios can listen only to such a system by entering each frequency of the system and scanning those frequencies while using digital monitor. Following a voice call as it progresses & jumps frequencies due to trunking nature of the system results in discontinuity of listening at times. Program in all the repeater output TX frequencies except the control channel frequency, setting each channel as DMR MODE = Repeater and tick the DataACK Disable box, set digital monitor mode on and you'll hear much of what is available. Sometimes the top LED will light but no voice will come out, this is fine, that is just the repeater sending idle or beacon packets to let the radios know the repeater is still alive.

## Motorola Capacity Max

This is a Motorola unique full trunking system that has a dedicated control channel and is typically used in very large, wide area networked systems. Since Capacity Max uses the same CAI (Common Air Interface) as regular DMR for voice calls, the AnyTone DMR radios can listen only to such a system by entering each frequency of the system and scanning those frequencies while using digital monitor. Following a voice call as it progresses & jumps frequencies due to trunking nature of the system results in discontinuity of listening at times. Program in all the repeater output TX frequencies except the control channel frequency, setting each channel as DMR MODE = Repeater and tick the DataACK Disable box, set digital monitor mode on and you'll hear much of what is available. Sometimes the top LED will light but no voice will come out, this is fine, that is just the repeater sending idle or beacon packets to let the radios know the repeater is still alive.

## Exceptions

If any sort of encryption or privacy is being used, you will not be able to listen in. Also, if RAS (Restricted Access to System) is being used on a Motorola DMR repeater, the AnyTone radio will remain silent. RAS isn't encryption, it is an intentional corruption of a checksum being used by radios to determine if the transmitted DMR packets are valid or not. With RAS corrupting this checksum intentionally, any radio not equipped to deal with RAS will remain silent, as they consider the transmissions to be corrupted. Scanners from Uniden etc. will ignore this and can hence listen in OK, but real DMR radios - other than Motorola equipped with RAS - will not.

!!! note
    Also note that the AnyTone DMR radios are **not** compatible with any other digital standard such as P25 phase 1, P25 phase 2, TETRA, TETRAPOL, NXDN, NexEdge, iDAS, OpenSky, Provoice etc. They are only DMR / MotoTRBO and FM radios.
