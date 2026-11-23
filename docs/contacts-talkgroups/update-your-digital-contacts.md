---
title: How to Update Your Anytone DMR Contact List
item: "2b"
source_url: https://hamradiosouthernrepeaters.co.uk/images/Anytone/Update_your_digital_contacts.pdf
original: ../originals/images/Anytone/Update_your_digital_contacts.pdf
tags: [AT-D868UV, AT-D878UV, AT-D578UV]
---

# How to Update Your Anytone DMR Contact List

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](../originals/images/Anytone/Update_your_digital_contacts.pdf) · [Source](https://hamradiosouthernrepeaters.co.uk/images/Anytone/Update_your_digital_contacts.pdf) Hub item 2b.

*By Jim Blocker KF5IW*

1. Open your current codeplug in CPS. As an example, this codeplug has 189,411 contacts:

    ![CPS Digital Contact List showing contact number 189411 as the last entry](../assets/img/update-your-digital-contacts/img-01.png)

2. Open <https://kf5iw.com/contactdb.php> and click on the "ALL" link to download the complete DMR contact list.

    ![kf5iw.com contact database page with the ALL row circled in red; 213249 DMR IDs and 188805 unique callsigns](../assets/img/update-your-digital-contacts/img-02.png)

3. Save the .zip file.

    ![Firefox dialog opening contacts_ALL_20211222051101.zip with Save File selected](../assets/img/update-your-digital-contacts/img-03.png)

4. Find your downloaded file.

    ![Windows Explorer showing the contacts_ALL zip containing a .csv file](../assets/img/update-your-digital-contacts/img-04.png)

5. Extract the .zip file to a .csv.

    ![Extract Compressed (Zipped) Folders dialog with the Extract button](../assets/img/update-your-digital-contacts/img-05.png)

6. You should now have an extracted .csv file.

    ![Windows Explorer showing the extracted contacts_ALL .csv file](../assets/img/update-your-digital-contacts/img-06.png)

7. Back in CPS, select **Tool → Import**.

    ![CPS Tool menu with Import highlighted](../assets/img/update-your-digital-contacts/img-07.png)

8. In the Import window, click on "Digital Contact List".

    ![CPS Import window with the Digital Contact List button](../assets/img/update-your-digital-contacts/img-08.png)

9. Navigate to your CSV that you downloaded from kf5iw.com, select the file and click "Open".

    ![File open dialog with the contacts_ALL csv selected, file type Digital Contact List (*.CSV)](../assets/img/update-your-digital-contacts/img-09.png)

10. The CSV file should now show in the Import window.

    ![Import window with the CSV file path shown next to Digital Contact List](../assets/img/update-your-digital-contacts/img-10.png)

11. Click on "Import" on the bottom of the Import window. You will see a progress indicator. Please be patient for the import process to complete.

    ![Progress - Import Data bar](../assets/img/update-your-digital-contacts/img-11.png)

12. Click on "OK" when "Import Complete" appears.

    ![D878UVII dialog reading Import Complete! with an OK button](../assets/img/update-your-digital-contacts/img-12.png)

13. Wait for the Digital Contact List display to update.

    ![Progress - Display Data bar partly filled](../assets/img/update-your-digital-contacts/img-13.png)

14. Once complete, the number of contacts displayed should match the number of contacts downloaded. The correct number of contacts is displayed on the kf5iw.com contact download page.

    ![kf5iw.com table with 213249 DMR IDs circled](../assets/img/update-your-digital-contacts/img-14.png)

    ![CPS Digital Contact List with the last contact, number 213249, circled](../assets/img/update-your-digital-contacts/img-15.png)

15. **Important:** now select **File → Save As** and save your updated codeplug.

    I save each new version of my codeplug as a new file so that it's easy to go back to a prior version if needed. You can create a unique filename based on today's date. For example, a codeplug created on December 30, 2021 could have a filename of "20211230.rdt".

16. Update your radio's contact list by selecting **Program → Write To Radio**. Make sure that the "Digital Contact List" option is checked.

    ![Read or Write Objects dialog with Digital Contact List and Other Data ticked, an arrow pointing at Digital Contact List](../assets/img/update-your-digital-contacts/img-16.png)

Enjoy having an updated contact list! You should now start seeing callsigns and names instead of just numbers.

*© 2021 Jim Blocker KF5IW · jim@kf5iw.com · Version 20211222*
