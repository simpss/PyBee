from pybee.packets.response.LocalAtResponse import LocalAtResponse
from pybee.xbee.XbeeAddress import XbeeAddress

__author__ = 'siim'

from pybee.packets.constants.FrameTypes import FrameType


class RemoteAtResponse(LocalAtResponse):
    """
    A class that represents a remote xbees AT command response.
    """
    frame_type = FrameType.remote_command_response

    @property
    def address(self):
        """
        Address for the xbee, where the response originated from.
        :return: The Address.
        """
        return self._address

    def __init__(self):
        self._data = None

        self._frame_id = None
        self._address = None
        self._at_command = None
        self._command_status = None
        self._command_data = None

    def fill_data(self, data):
        """
        Fill the packets data properties.
        :param data: The Frame Data for the packets.
        """
        self._data = data

        self._data_length = data[1:3]
        self._frame_id = data[4]
        self._address = XbeeAddress(data[5:9], data[9:13], data[13:15])
        self._at_command = data[15:17]
        self._command_status = data[17]
        try:
            self._command_data = data[18:21]
            self._checksum = data[22]
        except IndexError:
            self._command_data = None
            self._checksum = data[18]

    def __str__(self):
        return "Frame id: {}, Status: {}".format(self.frame_id, self.command_status)