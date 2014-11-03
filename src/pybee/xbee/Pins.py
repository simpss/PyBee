from pybee.xbee import AtCommand

__author__ = 'siim'

from enum import Enum


class Pin(Enum):

    DIO_0 = AtCommand((0x44, 0x30))
    DIO_1 = AtCommand((0x44, 0x31))
    DIO_2 = AtCommand((0x44, 0x32))
    DIO_3 = AtCommand((0x44, 0x33))
    DIO_4 = AtCommand((0x44, 0x34))
    DIO_6 = AtCommand((0x44, 0x36))
    DIO_7 = AtCommand((0x44, 0x37))
    DIO_8 = AtCommand((0x44, 0x38))
    PWM_0 = AtCommand((0x50, 0x30))
    DIO_11 = AtCommand((0x50, 0x31))
    DIO_12 = AtCommand((0x50, 0x32))
    DIO_13 = AtCommand((0x50, 0x33))