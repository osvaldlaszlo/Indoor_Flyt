# Indoor_Flyt
This repo is the port of flyt, configurations and informations for the original project https://github.com/AlexisTM/Indoor_Position_lasers

## Installation

- Write FlytOS image on the eMMC
- Replace the [boot.ini](root/boot.ini) file to match the screen configuration
- boot
- user : flytpod:flytpod
- root : root:flyfly
- resize partition via Odroid-Utility.sh
- `ssh-keygen`
- Wifi setup (UCLouvain : Tunneled TLS)
- Don't write keyring password, so we can boot directly and autoconnect WiFi
- `sudo su - # change account to root`
- `passwd # set root password`
- as root (not sudo): `apt-key adv --keyserver keyserver.ubuntu.com --recv-keys AB19BAC9`
- as root (not sudo): `wget -O- http://oph.mdrjr.net/meveric/meveric.asc | apt-key add -`
- as root (not sudo): ` cd /etc/apt/sources.list.d/ && wget http://oph.mdrjr.net/meveric/sources.lists/meveric-all-XU3.list`
- update FlytOS

```bash
# install Pip
cd
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py

# upgrade installation
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade

apt-get install ros-indigo-image-proc ros-indigo-image-transport-plugins ros-indigo-image-transport ros-indigo-rosbridge-suite ros-indigo-control-toolbox ros-indigo-octomap-ros ros-indigo-octomap-msgs libgoogle-glog-dev ros-indigo-pyros-setup ros-indigo-eigen-conversions python-serial python-flask python-wtforms python-sqlalchemy python-concurrent.futures python-mock python-zmq python-twisted tmux

pip install flask-security

dpkg -i flytsim_0.4-3_amd64.deb
```

- Add additionnal configuration

## More FLYT configurations

### Modify global namespace

You have to change the namespace on the namespace (flytpod) on the last line of `/flyt/flytos/flytcore/share/core_api/param_files/flyt_params.yaml` and on the first line of `/flyt/flytos/flytcore/share/core_api/param_files/global_namespace.yaml`

### Aliases

You should add aliases for easier use in .bash_aliases

> alias flyt_start='sudo $(rospack find core_api)/scripts/start_flytOS.sh'
> alias flyt_kill='sudo $(rospack find core_api)/scripts/kill_flytOS.sh'

### Launch files

Go to : `sudo $(rospack find core_api)/launch` and you find all the informations you need

### Add UDEV rules for terminals :

On Linux the default name of a USB FTDI would be like `\dev\ttyUSB0`. If you have a second FTDI linked on the USB or an Arduino, it will registered as `\dev\ttyUSB1`. To avoid the confusion between the first plugged and the second plugged, we recommend you to create a symlink from `ttyUSBx` to a friendly name, depending on the Vendor and Product ID of the USB device.

Using `lsusb` we can get the vendor and product IDs.

```sh
$ lsusb

Bus 006 Device 002: ID 0bda:8153 Realtek Semiconductor Corp.
Bus 006 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 005 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 004 Device 002: ID 05e3:0616 Genesys Logic, Inc.
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 004: ID 2341:0042 Arduino SA Mega 2560 R3 (CDC ACM)
Bus 003 Device 005: ID 26ac:0011
Bus 003 Device 002: ID 05e3:0610 Genesys Logic, Inc. 4-port hub
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 001 Device 002: ID 0bda:8176 Realtek Semiconductor Corp. RTL8188CUS 802.11n WLAN Adapter
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

The Arduino is `Bus 003 Device 004: ID 2341:0042 Arduino SA Mega 2560 R3 (CDC ACM)`

The Pixhawk is `Bus 003 Device 005: ID 26ac:0011`

> If you do not find your device, unplug it, execute `lsusb`, plug it, execute `lsusb` again and see the added device.

Therefore, we can create a new UDEV rule in a file called `/etc/udev/rules.d/99-pixhawk.rules` with the following content, changing the idVendor and idProduct to yours.

```sh
SUBSYSTEM=="tty", ATTRS{idVendor}=="2341", ATTRS{idProduct}=="0042", SYMLINK+="ttyArduino"
SUBSYSTEM=="tty", ATTRS{idVendor}=="26ac", ATTRS{idProduct}=="0011", SYMLINK+="ttyPixhawk"
```

Finally, after a **reboot** you can be sure to know which device is what and put `/dev/ttyPixhawk` instead of `/dev/ttyUSB0` in your scripts.

> Be sure to add yourself in the `tty` and `dialout` groups via `usermod` to avoid to have to execute scripts as root.

```sh
usermod -a -G tty ros-user
usermod -a -G dialout ros-user
```

## Tools

* MavYaml - Allow to convert QGroundControl params (from export menu) to a flyt yaml config file known as `/flyt/flytos/flytcore/share/core_api/param_files/flyt_params.yaml`
