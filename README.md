# KlikAanKlikUit TPC-300 MQTT service

Control individual KaKu lights through the TPC-300, exposed as an MQTT service. This is an alternative to building your own `433.92MHz` radio on eg. an Arduino.

## Usage

### Directly on HASS

(This is temporary, until the script is converted to a proper integration to supersede manual MQTT switch configuration below).

Clone this repository inside your `/addons` folder, and [install the _local_ addon from the HassIO store](https://my.home-assistant.io/redirect/supervisor_addon/?addon=local_tpc-300-mqtt).

### On an external machine (with access to MQTT)

#### Install Python packages on the target (or pre-download on host)

Easiest is `pip install -r requirements.txt` on the target machine, but if there is "network trouble" here, download and copy files from the host:

```console
$ pip download -r "../requirements.txt"
```

Now copy the files to the target (if you didn't download them into an `sshfs` on the host already)

Then, install them on the target:

```console
$ sudo python3 -m pip install packages/*
Installing collected packages: paho-mqtt, pyusb
  Running setup.py install for paho-mqtt ... done
Successfully installed paho-mqtt-1.6.1 pyusb-1.2.1
```

#### UDEV rules be broken

Workaround:

```console
$ chmod -R a+rwx /dev/bus/usb/
```

#### Finally, start the server

```console
$ ./tpc-server.py <mqtt broker address>
```

And in the background:

```console
$ PYUSB_DEBUG=debug nohup ./tpc-server.py <mqtt broker address> &
```

## Configure lights in Home Assistant

```yaml
switch:
  - platform: mqtt
    name: Tafel
    icon: mdi:lamp
    command_topic: "tpc-300/light/0/set"
  # More lights
```
