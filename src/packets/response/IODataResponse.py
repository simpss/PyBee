__author__ = 'siim'

from packets.BaseResponse import BaseResponse
from packets.response.Sample import Sample
from packets.constants.FrameTypes import FrameType
from packets.constants.ReceiveOptions import ReceiveOption
from packets.constants.AtStatuses import AtStatus
from xbee.XbeeAddress import XbeeAddress
from xbee.AtCommands import AtCommands

class IODataResponse(BaseResponse):
#TODO might want to consider making Samples a separate class.
    frame_type = FrameType.remote_command_response

    def __init__(self):
        self._data = None

        self._frame_id = None
        self._address = None
        self._at_command = None
        self._status = None
        self._receive_options = None
        self._samples = None
        self._checksum = None

    @property
    def frame_id(self):
        """
        Allows for the identification of the response. This is the same value passed in to the sent request.
        :return: the Frame id.
        """
        return self._frame_id

    @property
    def address(self):
        """
        Address for the xbee, where the response originated from.
        :return: The Address.
        """
        return self._address

    @property
    def at_command(self):
        """
        The At command that this responds to.
        """
        return AtCommands(self._at_command)

    @property
    def status(self):
        """
        Status of the response
        """
        return AtStatus(self._status)

    @property
    def receive_options(self):
        return ReceiveOption(self._receive_options)

    @property
    def samples(self):
        return self._samples

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
        self._status = data[17]
        self._receive_options = data[18]
        self._samples = Sample(data[18:-1])
        self._checksum = data[-1]

    def __str__(self):
        return "frame_id: {}, Status: {}, receive options: {}".format(self.frame_id, self.status, self.receive_options)