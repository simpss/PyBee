__author__ = 'siim'

from enum import Enum


class XbeeAddress:
    """
    A class to represent the xbees address.
    """
    @property
    def bit16(self):
        """
        The 16 bit address.
        """
        return self._address16bit

    @property
    def bit64high(self):
        """
        The high part for the 64 bit address.
        """
        return self._address64bit_high

    @property
    def bit64low(self):
        """
        The low part for the 64 bit address.
        """
        return self._address64bit_low

    @property
    def serialize(self):
        """
        Serializes the whole address, ready to be sent via Serial.
        :rtype : bytearray
        :return: the whole address for the Xbee.
        """
        address = bytearray()
        address.extend(self._address64bit_high)
        address.extend(self._address64bit_low)
        address.extend(self._address16bit)
        return address

    def __init__(self, bit64high, bit64low, bit16=(0xFF, 0xFE)):
        """
        Create an XbeeAddress object.
        :param bit64high: the high part of the 64 bit address.
        :param bit64low: the low part of the 64 bit address.
        :param bit16: the 16 bit address, defaults to 0xFF, 0xFE if unknown
        """
        self._address64bit_high = bit64high
        self._address64bit_low = bit64low
        self._address16bit = bit16


class PresetAddress(Enum):
    coordinator = XbeeAddress([0x00, 0x00, 0x00, 0x00], [0x00, 0x00, 0x00, 0x00], [0xFF, 0xFE])
    broadcast = XbeeAddress([0x00, 0x00, 0x00, 0x00], [0x00, 0x00, 0xFF, 0xFF], [0xFF, 0xFE])