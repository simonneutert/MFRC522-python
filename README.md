MFRC522-python
==============
A small class to interface with the NFC reader Module MFRC522 on the Raspberry Pi.
This is a Python port of the example code for the NFC module MF522-AN.

**Important notice:** This library has not being actively updated in almost four years.
It might not work as intended on more recent Raspberry Pi devices. You might want to 
take a look to the open pull-requests and forks to see other implementations and bug-fixes.

## Requirements
### 1. Enable SPI on your host machine (undockered / base system)

    `$ sudo echo "dtparam=spi=on" >> /boot/config.txt && sudo reboot now`

### 2. Install SPI-Py

    This code requires you to have SPI-Py installed from the following repository:
    https://github.com/lthiery/SPI-Py

## Examples
This repository includes a couple of examples showing how to read, write, and dump data from a chip. They are thoroughly commented, and should be easy to understand.

## Pins
You can use [this](http://i.imgur.com/y7Fnvhq.png) image for reference.

| Name | Pin # | Pin name   |
|:------:|:-------:|:------------:|
| SDA  | 24    | GPIO8      |
| SCK  | 23    | GPIO11     |
| MOSI | 19    | GPIO10     |
| MISO | 21    | GPIO9      |
| IRQ  | None  | None       |
| GND  | Any   | Any Ground |
| RST  | 22    | GPIO25     |
| 3.3V | 1     | 3V3        |


![https://www.raspberrypi-spy.co.uk/wp-content/uploads/2018/02/rc522_rfid_raspberry_pi_wiring.png](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2018/02/rc522_rfid_raspberry_pi_wiring.png)

Image taken from: https://www.raspberrypi-spy.co.uk/2018/02/rc522-rfid-tag-read-raspberry-pi/

## Usage
Import the class by importing MFRC522 in the top of your script. For more info see the examples.

## License
This code and examples are licensed under the GNU Lesser General Public License 3.0.
