---
title: Remove Spaces
item: "94"
source_url: https://hamradiosouthernrepeaters.co.uk/images/Anytone/Remove_Spaces.pdf
original: ../originals/images/Anytone/Remove_Spaces.pdf
tags: []
---

# Remove Spaces

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/Anytone/Remove_Spaces.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/Anytone/Remove_Spaces.pdf) Hub item 94.

How to remove spaces in Channels, Zones, Scan list etc. The following procedure applies to all; I will just show how to do channels.

![CPS Channel list with channels in rows 6, 7 and 13 and empty rows 1 to 5 and 8 to 12](../assets/img/remove-spaces/img-01.jpeg)

## 1. You need to export the Channel CSV file

1. **CPS, top line → Tool → Export**
2. Click on the **Channel** tab.
3. Point to a place you wish to save the CSV and name it.
4. Click **Save**.
5. At the bottom of the page click on **Export**.

## 2. Open the CSV file

![Channel CSV file open in a spreadsheet](../assets/img/remove-spaces/img-02.jpeg)

1. Delete Column A = No.

    ![Channel CSV file with column A deleted](../assets/img/remove-spaces/img-03.jpeg)

2. Save the CSV.

## 3. Now import the Channel CSV

1. **CPS, top line → Tool → Import**
2. Click on the **Channel** tab.
3. Point to the place you saved the CSV.
4. Click **Open**.
5. At the bottom of the page click on **Import**.

Now your Channels look like this, with no spaces.

![CPS Channel list after import with the channels in rows 1 to 3](../assets/img/remove-spaces/img-04.jpeg)

**Save your codeplug.**

You might wish to look at this also: [Export and Import All CSV](../cps-firmware/export-and-import-all-csv.md)

## See also

- [Export and Import All CSV](../cps-firmware/export-and-import-all-csv.md)
- [AES256/ARC4 encryption CSV Export/Import](../encryption/aes256-arc4-encryption-csv-export-import.md)
