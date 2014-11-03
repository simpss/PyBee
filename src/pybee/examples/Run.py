from pybee.xbee.AtCommand import AtCommand
from pybee.xbee.XbeeAddress import XbeeAddress
from pybee.xbee.Xbee import Xbee

from pybee.examples.pinRead import read_pin
from pybee.examples.pinChange import change_pin
from pybee.xbee.Pins import Pin

#local xbee information
port = "/dev/ttyUSB0"
baud = 9600

#remote xbee information
addrH = [0x00, 0x13, 0xa2, 0x00]
addrL = [0x40, 0xab, 0x97, 0xC1]
addr16bit = [0xFF, 0xFE]

#create the xbees.
address = XbeeAddress(addrH, addrL, addr16bit)

xbee_local = Xbee().setup_local(port, baud)
xbee_remote = Xbee().setup_remote(address)

read_pin(xbee_local, xbee_remote)
change_pin(xbee_local, xbee_remote, Pin.DIO_1, AtCommand.digital_output_low)