from pybee.packets import BaseResponse

__author__ = 'siim'

from pybee.packets.constants.FrameTypes import FrameType
from pybee.packets.constants.AtStatuses import AtStatus


class LocalAtResponse(BaseResponse):
    """
    A class that represents the xbees AT command response.
    """
    frame_type = FrameType.at_command_response

    @property
    def frame_id(self):
        """
        Allows for the identification of the response. This is the same value passed in to the sent request.
        :return: the Frame id.
        """
        return self._frame_id

    @property
    def at_command(self):
        """
        Responses at_command data.
        :return: At command.
        """
        return self._at_command

    @property
    def command_status(self):
        """
        Responses command status.
        :return: Command Status.
        """
        return AtStatus(self._command_status)

    @property
    def command_data(self):
        """
        Register data in binary format. If the register was
        set, then this field is None.
        :return: register data or None.
        """
        return self._command_data

    def __init__(self):
        self._data = None

        self._frame_id = None
        self._at_command = None
        self._command_status = None
        self._command_data = None

    def fill_data(self, data):
        """
        Fill the packets data properties.
        :param data: The Frame Data for the packets.
        """
        self._data = data
        #TODO check and fix data locations.
        self._frame_id = data[4]
        self._at_command = data[5:6]
        self._command_status = data[7]
        try:
            self._command_data = data[8:len(data)]
        except IndexError:
            self._command_data = None