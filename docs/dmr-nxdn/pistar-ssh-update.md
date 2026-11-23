---
title: "PiStar SSH Update"
source_url: https://hamradiosouthernrepeaters.co.uk/dmr-info/2-uncategorised/57-pistar-ssh-update.html
tags: []
---

# PiStar SSH Update

!!! info "Source"
    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Source](https://hamradiosouthernrepeaters.co.uk/dmr-info/2-uncategorised/57-pistar-ssh-update.html)

| Setting | Value |
|---|---|
| Default Username | `pi-star` |
| Default Password | `raspberry` |

`xxx.xxx.xxx/admin/expert/`

Login over SSH, run:

```text
rpi-rw
```

Other commands as required:

```text
sudo pistar-expand
sudo reboot
```

<http://www.pistar.uk/index.php>

### Duplex Firmware Update

```text
sudo pistar-mmdvmhshatflash hs_dual_hat
```

or download the flash script:

```text
curl -OL https://github.com/juribeparada/MMDVM_HS/releases/download/v1.4.7/install_fw_hsdualhat.sh
```

4. Make runnable:

    ```text
    chmod +x install_fw_hsdualhat.sh
    ```

5. Stop MMDVMHost service:

    ```text
    sudo pistar-watchdog.service stop; sudo systemctl stop mmdvmhost.timer; sudo systemctl stop mmdvmhost.service
    ```

6. Flash to latest version (make sure you copy the full stop in front of `./install`):

    ```text
    ./install_fw_hsdualhat.sh
    ```

7. Start up MMDVMHost service:

    ```text
    sudo pistar-watchdog.service start; sudo systemctl start mmdvmhost.timer; sudo systemctl start mmdvmhost.service
    ```

8. Reboot:

    ```text
    sudo reboot
    ```

### Edit MMDVM.ini & Gateway

```text
rpi-rw
sudo su
nano /etc/mmdvmhost

nano /etc/dmrgateway

sudo nano /usr/local/etc/DMR_Hosts.txt
```

**Ctrl+X** for save.

`/usr/local/etc/`

### Nextion Drivers

[HOW TO INSTALL THE NEXTION DRIVER](https://github.com/PD0DIB/Nextion_HAM-radio-screens/wiki/FAQ-Nextion.driver-by-ON7LDS)

[How to enable reconnect to default reflector](https://forum.pistar.uk/viewtopic.php?t=310)

```text
# Prefixes=234,235
# Slot1TGWhiteList=
# Slot2TGWhiteList=
# IDWhiteList=
# BlackList=1234567,
```

Blacklist, Whitelist, Slot1TGWhitelist, Slot2TGWhitelist, SelfOnly, Prefixes, ID.

[Rewrite Rules](https://github.com/g4klx/DMRGateway/wiki/Rewrite-Rules)

### STM32_DVM_PiHat V3 (BLUE) Board

If using SSH, proceed as below.

```text
pi-star@pi-star(rw):~$ sudo su       *gives ROOT permissions
root@pi-star(rw): rpi-rw                *makes file system read/write
root@pi-star(rw): mv /etc/mmdvmhost /etc/mmdvmhost.save     *rename mmdvmhost so it won't auto
root@pi-star(rw): reboot
```

Wait for the Pi to reboot, log into the Raspberry Pi via SSH or via web SSH access as above; then:

```text
pi-star@pi-star(rw):~$ sudo su
root@pi-star(rw): rpi-rw
root@pi-star(rw): cd /home/pi-star    *go to pi-star directory
root@pi-star(rw): wget -N http://dvswitch.org/files/HAM/MMDVM/stm32flash    *get flash utility
root@pi-star(rw): wget -N http://dvswitch.org/files/HAM/MMDVM/Version_3_Firmware/mmdvm_f4.hex    *get Firmware
root@pi-star(rw): chmod +x stm32flash    *make flash utility executable
root@pi-star(rw): ./stm32flash -v -w mmdvm_f4.hex -i  20,-21,21,-20 -R /dev/ttyAMA0
```

The above line does the actual flash programming. The response to the above command should be:

```text
stm32flash 0.5
http://stm32flash.sourceforge.net/
Interface serial_posix: 57600 8E1
Version      : 0x31
Option 1     : 0x00
Option 2     : 0x00
Device ID    : 0x0421 (STM32F446xx)
- RAM        : 128KiB  (12288b reserved by bootloader)
- Flash      : 512KiB (size first sector: 1x16384)
- Option RAM : 16b
- System RAM : 30KiB
Write to memory
Erasing memory
Wrote and verified address 0x0800fec8 (100.00%) Done.
```

Once writing is successful, do some clean up:

```text
root@pi-star(rw): mv /etc/mmdvmhost.save /etc/mmdvmhost     *"re-enable" mmdvmhost
root@pi-star(rw): reboot
```

### Add a host to DMR_Hosts.txt

```text
rpi-rw;sudo bash -c 'printf "BM_Nerja_DMR_SVR        31665   tgif.network     passw0rd        62031" >> /usr/local/etc/DMR_Hosts.txt'
```

### ModeHang settings in mmdvmhost

In Pi-Star you can do this via SSH login > `rpi-rw` > `sudo nano /etc/mmdvmhost`, to:

```ini
[General]
Callsign=XXXXX
Id=xxxxxxx
Timeout=600
Duplex=1
ModeHang=10                 <<< added, This acts for all modes not otherwise defined below ;
#RFModeHang=300        <<< disabled with #
#NetModeHang=300       <<< disabled with #
Display=None
Daemon=1

[D-Star]
Enable=1
Module=B
SelfOnly=0
AckReply=1
AckTime=750
ErrorReply=1
RemoteGateway=0
#ModeHang=20   <<<< disabled

[DMR]
Enable=1
Beacons=0
BeaconInterval=60
BeaconDuration=3
ColorCode=1
SelfOnly=0
EmbeddedLCOnly=1
DumpTAData=0
CallHang=3
TXHang=4
#ModeHang=20      <<<< disabled

[System Fusion]
Enable=1
LowDeviation=0
SelfOnly=0
TXHang=4
RemoteGateway=0
#ModeHang=20     <<<< disabled

[P25]
Enable=1
NAC=293
SelfOnly=0
OverrideUIDCheck=0
RemoteGateway=0
#ModeHang=20    <<<< disabled

[NXDN]
Enable=1
RAN=1
RemoteGateway=0
SelfOnly=0
#ModeHang=20    <<<< disabled

[D-Star Network]
Enable=1
GatewayAddress=127.0.0.1
GatewayPort=20010
LocalPort=20011
Debug=0
#ModeHang=10    <<<< disabled

[DMR Network]
Enable=1
Address=127.0.0.1
Port=62031
Local=62032
Jitter=360
Password="none"
Slot1=0
Slot2=1
Debug=0
#ModeHang=20    <<<< disabled

[System Fusion Network]
Enable=1
LocalAddress=127.0.0.1
LocalPort=3200
GatewayAddress=127.0.0.1
GatewayPort=4200
Debug=0
#ModeHang=20    <<<< disabled

[P25 Network]
Enable=1
GatewayAddress=127.0.0.1
GatewayPort=42020
LocalPort=32010
Debug=0
#ModeHang=20    <<<< disabled

[NXDN Network]
Enable=1
LocalAddress=127.0.0.1
LocalPort=14021
GatewayAddress=127.0.0.1
GatewayPort=14020
Debug=0
#ModeHang=20    <<<< disabled
```
