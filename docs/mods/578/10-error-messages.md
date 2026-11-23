---
title: "Strange error messages"
source_url: https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#ErrorMessages
tags: [AT-D578UV]
---

# Strange error messages

[← All 578 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#ErrorMessages)

## Band Error

![Band Error message on the radio screen](../../originals/images/578Mods/banderror.jpg)

[Band Error has it’s own section, click here](02-band-error.md) to see five different methods on how to fix this problem.

## Codeplug newer than the CPS

![AnyTone CPS version error message](../../originals/images/578Mods/AnytoneCPSversionerror.jpg)

If you see something similar to this error message, it means you are trying to load a newer codeplug file than what your CPS software version can handle.

You must make sure your CPS software version matches your codeplug file version and matches your firmware version installed in the radio and that you are using it with the correct matching model radio.

## Wrong model

![Model wrong error message](../../originals/images/578Mods/modelwrong.png)

This error means you are trying to use the wrong CPS / wrong codeplug / wrong firmware for the model of radio you have. For example, you might be trying to use the 578 CPS with an 578-PLUS radio.

You must make sure your CPS software version matches your codeplug file version and matches your firmware version installed in the radio and that you are using it with the correct matching model radio.

## CPS version mismatch

![CPS version mismatch error message](../../originals/images/578Mods/CPS_version_mismatch.png)

If you are getting this cryptic error message when trying to read or write to your radio, it means that your PC programming (CPS) software isn’t the same version firmware as what is on your radio. For example, in the screen grab here, this shows v1.09 software trying to interact with a radio with v1.10 firmware.

You must make sure your CPS software version matches your codeplug file version and matches your firmware version installed in the radio and that you are using it with the correct matching model radio.

## Corrupt codeplug

![Codeplug error message](../../originals/images/578Mods/codeplugerror.png)

If you see this error, or something similar to it, this means your codeplug is corrupt. The solution is to reset the radio, [REBUILD](57-prevent.md) your codeplug, and write the rebuilt codeplug to your radio (thanks to Lane KD2TVW for this one).

## Program error

![Program error message](../../originals/images/578Mods/ProgramError.jpg)

This error means your codeplug has become corrupt in memory. All you need do is perform a reset on the radio and reload the codeplug. I also strongly recommend doing a codeplug [REBUILD](57-prevent.md) before reloading it to the radio.

## Checking flash error / Bad Block

![Checking flash error message](../../originals/images/578Mods/CheckingFlashError.jpg)

This error is a little more serious. A similar error message is ’Bad Block.’ Try the following, in order:

1. Reset the radio and then reload the codeplug.
2. If that did not work, reset the radio, reload a fresh copy of firmware and icons, perform another reset, and then reload your codeplug.
3. If you happen to have a backup image of your flash memory, especially of the critical area at addresses 02F00000 and 02FDFFFF, then use the instructions on [writing your own CDD file](58-cdd.md) to restore this image to your radio flash memory. Alternatively, you can use the defroster packs ([Quick defroster](55-frozen.md) and [Full defroster](56-full-defrost.md)) to refresh your flash memory, though you will still need to have a backup of your critical area data first.
4. In the very worst case, this could indicate hardware failure of the flash memory, a fatal problem that can not be recovered from.

## Power-on password in Chinese

![Power-on password prompt in Chinese on an 878](../../originals/images/578Mods/PasswordChinese.jpg)

This message is asking you to "Please enter power on password:" in Chinese. If you know what the password is, enter it, and then you should reprogram the radio codeplug to reset the radio back in to English language. If you don’t know what the password is, you can reset it using the instructions [here](41-lost-password.md).

(Yes, this is a photo of an 878, but the same error could occur on a 578 too - it will display the same.)

## RTC error

![RTC trying error message](../../originals/images/578Mods/RTCTryingError.jpg)

This error, or ’RTC ERROR!’ or ’RTC not run!’ means that, for what ever reason, the radio can not read the Real Time Clock. There is a pair of tiny internal batteries, one of which backs up the Real Time Clock and keeps time when the radio is turned off. If that battery becomes too old, or goes faulty, you may see this error.

If you continue to ignore this error message and the battery becomes so bad that it short circuits itself, then that could start to induce other new random errors such as the radio freezing up, not accepting any codeplug or firmware updates, and finally becoming completely unresponsive. A short circuit battery will drag down the microprocessor voltage supply, causing these random failures.

The RTC backup battery can be replaced by getting access to the bottom side of the PCB and desoldering the old battery and replacing it with a new XH414HG IV01E 3 volt lithium battery. After fitting, a reset of the radio, setting the time & date and reprogramming the codeplug should set everything right. You can find out more information about the little lithium backup batteries [here](45-backup-batteries.md).

## White blocks instead of icons

![White blocks displayed instead of icons](../../originals/images/578Mods/whiteicon.jpg)

Not really an error message as such, if you are seeing white blocks being displayed instead of an icon after you have made a firmware update, this means you need to also do an icon update to the radio. So far, the 578 has not had an icon update issued, but if you still find white squares appearing on the 578, you can use the latest 878 Icon file (it’s the same as what is used in the 578): find Icon V1.21 update download.

You send the icon .spi file to the radio by powering up the 578 in the icon update mode by holding down the **DIAL** and **P1** buttons until UPDATE MODE is displayed. Then use the CPS menu selections **Tool → Firmware Upgrade** (while this selection doesn’t specifically mention ’Icon’ this IS definitely the correct process to use) and select the icon .spi file.

Download the 878 v1.21 icons package which uses the same icon file as the 578 (1003kb) here:

- [Download via Mega](https://mega.nz/file/GtEUTZCY#rqkQB6pwPKixWWQ4VOMK1JNjbTM6exohODKei0nvyZQ)
- [Download via Google Drive](https://drive.google.com/file/d/1KSMqLCuIMry25UstDF0BlSxxgm4zxRqV/view?usp=sharing)
- [Download via Sabercat host](https://sabercathost.com/9Ya9/D878UV_ICONV1.21.zip)
