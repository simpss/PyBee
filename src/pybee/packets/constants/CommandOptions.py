__author__ = 'siim'

from enum import Enum


class CommandOption(Enum):
    none = 0x00
    disable_ack = 0x01
    apply_changes = 0x02
    use_extended_transmission_timeout_to_this_destination = 0x40