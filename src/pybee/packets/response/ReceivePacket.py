from pybee.packets import BaseResponse
from pybee.xbee import XbeeAddress

__author__ = 'siim'

from pybee.packets.constants.FrameTypes import FrameType
from pybee.packets.constants.ReceiveOptions import ReceiveOption


class ReceivePacket(BaseResponse):

    frame_type = FrameType.rx_received

    def __init__(self):
        self._address = None
        self._receive_options = None
        self._received_data = None

    @property
    def address(self):
        """
        64-bit address of sender. Set to 0xFFFFFFFF 0xFFFFFFFF
        (unknown 64-bit address) if the sender’s 64-bit
        address is unknown.
        :return: The Address.
        """
        return self._address

    @property
    def receive_options(self):
        return ReceiveOption(self._receive_options)

    @property
    def received_data(self):
        """
        Received RF data.
        """
        return self._rf_data

    def fill_data(self, data):
        """
        Fill the packets data properties.
        :param data: The Frame Data for the packets.
        """
        self._data = data
        #TODO check if the data locations make sense.
        self._address = XbeeAddress(data[4:8], data[8:12], data[12:14])
        self._receive_options = data[14]
        self._received_data = data[14:20]