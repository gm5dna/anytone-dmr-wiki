---
title: "Compatibility of encryption"
source_url: https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#Encryption
tags: [AT-D578UV]
---

[← All 578 mods](index.md)

!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"
    © Jason Reilly 2018–2022. Jason's pages were preserved by Norman Williams on hamradiosouthernrepeaters.co.uk and are reproduced here, unchanged, so that his work stays available. They will be removed on request from his family. [Original page](https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html#Encryption)

**Compatibility of encryption**
Starting at firmware version 1.03, there are two voice encryption types available on the 578.
First is AES (Advanced Encryption Standard) which is definitely compatible with Motorola and Hytera products that also have AES enabled. To set this sort of encryption and have it successfully communicate to another AES encrypted radio you need to:

- Ensure the radio is updated with baseband version SCT3258 V2.01.07BA or later; AES was not available on earlier versions
- Go to Options \> Other \> Encryption Type set to AES
- Program in the encryption keys under menu ’AES Encryption Code’ using the same key ID index (Encryption ID) and key value as other radios programmed with AES encryption
- If the key value has less than 64 hex characters, you need to pad out the key with leading zeros
- Finally, in each channel you want to encrypt, select the required key ID index number in the ’AES Digital Encryption’ setting for those channels.
- *Note that SMS messages are not encrypted, so be aware of this.*

The other encryption type is called ’Common’. This encryption system is set up slightly differently:

- Go to Options \> Other \> Encryption Type set to Common
- Program in the encryption keys under menu ’Encryption Code’ (not AES Encryption Code) using the same key value
- Finally, in each channel you want to encrypt, select ’Digital Encryption’ setting to on, and select ’Encryption TYPE’ to be the same as other radios in the communication group

*You can only select one type of encryption in the 578 at a time: either AES or Common (Normal or Enhanced), not both at the same time. Also, encryption obviously only works on DMR digital channels.*
Regarding compatibility, as already mentioned, AnyTone AES encryption is compatible with Motorola & Hytera AES encryption.
With the ’Common’ encryption - either in standard or enhanced mode - this is only compatible with other AnyTone 578 and 878s with the same settings. It is **not** compatible with other Chinese brand radios encryption, and it is **not** compatible with Motorola Basic Privacy or RC4 Enhanced Privacy.
The AnyTone radios will never be able to be compatible with Motorola Basic Privacy because that is a proprietary system that Motorola would not permit others to copy; and will never be compatible with RC4 Enhanced Privacy because the SCT3258 is physically unable to process DMR in the same way necessary to enable that particular encryption system.

------------------------------------------------------------------------
