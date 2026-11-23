---
title: "Resetting your power on password Easy"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#LostPassword
tags: [AT-D868UV, AT-D878UV]
---

# Resetting your power on password Easy

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#LostPassword)

*Only tested on 868 & 878*

If you've forgotten your power on password where the radio displays PLEASE INPUT THE PASSWORD! and will not let you go any further until you do, this will help you recover it and remove the password. Resetting of the radio will be inhibited while ever this password check is active and so a reset will not help.

1. Power up the radio and wait until it asks for the password.
2. Connect your programming cable, and using the CPS software, read from the radio.
3. Go to the CPS menu **Optional Setting → Power-on → Power-on Password Char** and you will see what your password is set to. Record your password somewhere safe if you intend to continue using a power on password.
4. If you wish to remove the password check, delete every digit in the Power-on Password Char field, save the codeplug, and write it back to the radio.
5. Power cycle the radio again and confirm you are not asked for a password this time.

If your password has become corrupted in memory and the password read is anything other than pure digits, and over-writing or deleting the password does not work, then your only option is to do a [full defrost](80-full-defrost.md) of the radio. A quick defrost will not work.
