from pybee.packets.BaseRequest import BaseRequest
from pybee.packets.constants.FrameTypes import FrameType


class LocalAtCommand(BaseRequest):

    frame_type = FrameType.remote_command_request

    @property
    def frame_id(self):
        """
        Identifies the UART data frame for the host to correlate with a subsequent ACK (acknowledgment).
        If set to 0, no response is sent.
        :return: the frame ID.
        """
        return self._frame_id

    @property
    def at_command(self):
        """
        The AT command name for the packets.
        :rtype: bytearray
        :return: the At command.
        """
        return self._at_command

    @property
    def parameter(self):
        """
        If present, indicates the requested parameter value to set the
        given register. If no characters present, the register is queried.
        :return: the parameter
        """
        return self._parameter

    @BaseRequest.frame_data.getter
    def frame_data(self):
        """
        Calculates the whole Frame Data for the request from the data it has.
        :rtype : bytearray
        :return: contains all the information for the packets.
        """
        data = bytearray()
        data.append(self.frame_type.value)
        data.append(self.frame_id)
        data.extend(self.at_command)
        data.append(self.parameter)
        return data

    def __init__(self, at_command, frame_id=0x0,
                 parameter=None):
        """
        Creates a LocalAtComman object.
        :type at_command: list
        :param at_command: the at
        :param frame_id:
        :param parameter:
        """
        self._frame_id = frame_id
        self._at_command = at_command
        self._parameter = parameter