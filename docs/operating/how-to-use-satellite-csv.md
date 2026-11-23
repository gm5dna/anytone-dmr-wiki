---
title: How to use Satellite CSV v2
item: "173"
source_url: https://hamradiosouthernrepeaters.co.uk/images/Anytone/How_to_use_Satellite_CSV.pdf
original: ../originals/images/Anytone/How_to_use_Satellite_CSV.pdf
tags: [AT-D878UV, AT-D168UV]
---

# How to use Satellite CSV v2

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/Anytone/How_to_use_Satellite_CSV.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/Anytone/How_to_use_Satellite_CSV.pdf) Hub item 173.

- From CPS version 3.08 for 878/878IIPlus
- From CPS version 1.07 for 168

## Download and export

Via the CPS, open **Satellite Data Updating**.

1. Select your **Satellite Http Url**.
2. Click on **Http Download**.

    Via the main window you can edit your SATs (or you can edit the CSV after export).

3. Click on **Export CSV** and save the CSV.

Now you can edit the CSV if you want.

## How to use the CSV

Always best to close the CPS and open again.

1. Click on **Load CSV** and open the saved CSV.
2. Select your **Satellite Http Url** (should be the same as step 1 of the first procedure).
3. Click on **Http CSV Update**.
4. Click on **Write Data to Radio**.

This will only update the TLE_LINE1 and TLE_LINE2 (the SAT Telemetry Data).

Now you can use the CSV as your template for the SATs you wish to use.

If the SAT is listed in the main window, you can also add Frequencies, add or remove CTC etc, to meet your needs.

!!! note
    You can not add new SATs that are not listed, as the Telemetry Data will not be added or updated.

If you run into any issues, or things do not look correct, restart the CPS and start over.
