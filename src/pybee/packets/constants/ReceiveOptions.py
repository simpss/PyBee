__author__ = 'siim'

from enum import Enum


class ReceiveOption(Enum):
    packet_acknowledged = 0x01
    packet_was_broadcast = 0x02
    packet_encrypted = 0x20
    packet_from_end_device = 0x40