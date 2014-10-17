__author__ = 'siim'

from enum import Enum


class AtStatus(Enum):
    """
    An enum to represent different AT response statuses.
    """
    ok = 0X00
    error = 0X01
    invalid_command = 0X02
    invalid_parameter = 0X03
    tx_failure = 0X04