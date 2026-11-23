---
title: "Introduction to hex editing. Moderate"
source_url: https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#HexIntro
tags: [AT-D868UV, AT-D878UV]
---

[← All 868-878 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, unchanged, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html#HexIntro)

**Introduction to hex editing.** Moderate
Hexadecimal - more commonly abbreviated to just 'hex' - is a system of counting with sixteen symbols. We humans are used to counting from one to ten with our ten symbols we call numbers, those being 0-9. If we want to go above 9, we join two numbers together e.g. 1 and 0 to be 10, and so on. Hexadecimal begins with 0 and goes up to 9, but instead of moving on to 10, hexadecimal uses letters A through to F, so A in hex would be 10, B=11, C=12 and so on up to F which is equal to 15, then hex "10" is equal to 16, 11 in hex = 17 and so on. Once 19 in hex is reached, the next number is 1A. Get the picture? Have a play around with a scientific calculator to convert hex numbers to decimal numbers, and you'll soon see how it all works.

OK, so why hex? As you probably know, computers use digital logic circuits which have just two values: on and off. These can be thought of as a 1 or 0, and computers 'talk' with lots of 1s and 0s - that's called binary. For us humans to try and make inputs to a computer in binary with just 1s and 0s would be mind-numbingly tedious, but using hexadecimal is a compromise. You've probably heard the term 'byte' before, and it turns out that two hexadecimal numbers fits perfectly into a byte. So 00, 3A, D2 and FF (all examples of hex numbers) can be represented with one byte of memory.

If you were to open a new text document with simply the word "HELLO" in it, and save that text document, you could open the text document in Notepad and edit it at a later time. But that's not the only way you can edit this text document. By opening the text document in a hex editor application, you can edit the document in it's raw form as it is stored on your hard disc. What you would see is the word HELLO represented by it's hex numbers: 48 45 4C 4C 4F. Now lets say you want to change HELLO to APPLE instead. In the hex editor, you would change those hex values to 41 50 50 4C 45, and then save the file.

The advantage of hex editing a file is that it doesn't matter what created the file or what the file contents are, they all get stored on hard disc the same way, and with hex editing you're editing the raw data and there are no limitations to making those edits, rather than any artificial limits a program might impose.

One more thing to know before moving on to your first software modification is to know about the concept of little-endian formatting. Little-endian formatting is listing a value with it's least significant bytes first. Take a number like 490 for example. First break the number up into two bytes: 04 and 90 (add a zero in front of the first number if it's not already two digits). Now simply reverse the order of the bytes, so that is 90 04. That is little-endian format of (0)490. Another example with a bigger number: 12345678. Broken up into bytes, that's 12 34 56 78. Now reverse the order of those groups: 78 56 34 12. Not hard, is it? Little-endian formatting can be equally applied to decimal or hex numbers, simply break the number down into two digit groups (i.e. bytes) and then reverse the order of the groups.

To make edits in hex, you'll want to use a hex editor. It's just like a word processor, only it edits in hexadecimal. I recommend using a hex editor called HxD. It's free to download at:
[https://mh-nexus.de/en/downloads.php?product=HxD (about 860kb)](https://mh-nexus.de/en/downloads.php?product=HxD)

------------------------------------------------------------------------
