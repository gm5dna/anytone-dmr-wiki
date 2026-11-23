---
title: "How to Install the No-IP DUC on Raspberry Pi"
source_url: https://hamradiosouthernrepeaters.co.uk/dmr-info/2-uncategorised/30-no-ip-duc-on-raspberry-pi.html
tags: []
---

# How to Install the No-IP DUC on Raspberry Pi

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Source](https://hamradiosouthernrepeaters.co.uk/dmr-info/2-uncategorised/30-no-ip-duc-on-raspberry-pi.html)

Make an account with [No-IP](https://www.noip.com/) and Create Host Name.  

You will be able to install No-IP’s Dynamic Update Client on Raspberry Pi in just a few minutes using Terminal.  
Installing the service is simple to do, and requires little knowledge of Linux.  

You will need to create a directory for the client software to be installed.  

Open Terminal and type the following. After each entry press “Enter“.  

```text
rpi-rw
```

```text
mkdir /home/pi
```

```text
mkdir /home/pi/noip
```

```text
cd /home/pi/noip
```

After creating the folders for the DUC it is time to download the software.  

Within the Terminal window  type the following. After each entry you will press “Enter”.  

```text
wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
```

```text
tar vzxf noip-duc-linux.tar.gz
```

Next navigate to the directory you created to locate the downloaded files.  

```text
cd noip-2.1.9-1
```

Now install the program.  

```text
sudo make
```

```text
sudo make install
```

After typing “sudo make install” you will be prompted to login with your No-IP account username and password.  
After logging into the DUC answer the questions to proceed. When asked how often you want the update to happen you must choose 5 or more. The interval is listed in minutes, if you choose 5 the update interval will be 5 minutes. If you choose 30 the interval will be 30 minutes.  

Please select the Internet interface from this list.  

```text
By typing the number associated with it.
0       eth0
1       ztugazdlxe
2       ztugazdlxe
3       wlan0_ap
4       wlan0_ap
0

Please enter the login/email string for no-ip.com  ***********
Please enter the password for user '**********'  **********

2 hosts are registered to this account.
Do you wish to have them all updated?[N] (y/N)  n
Do you wish to have host [one.ddns.net] updated?[N] (y/N)  ^M
Do you wish to have host [two.ddns.net] updated?[N] (y/N)  y
Please enter an update interval:[30]  5
Do you wish to run something at successful update?[N] (y/N)  n
```

```text
sudo /usr/local/bin/noip2
```

To confirm that the service is working properly you can run the following command.  

```text
sudo noip2 ­-S (Capital “S”)
```
