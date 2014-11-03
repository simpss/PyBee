from pybee.packets.BaseRequest import BaseRequest
from pybee.packets.request import LocalAtCommand
from pybee.packets.constants.FrameTypes import FrameType


class RemoteAtCommand(LocalAtCommand):
    """
    Represents the AT command request to a remote Xbee.
    """
    frame_type = FrameType.remote_command_request

    @property
    def address(self):
        """
        The address of the xbee where the packets should be sent.
        :return: the Address.
        """
        return self._address

    @property
    def command_options(self):
        """
        Bit field to enable various remote command options. Supported
        values include:
        0x01 – Disable ACK.
        0x02 – Apply changes on remote. (If not set, AC command must
        be sent before changes will take effect.)
        0x40 – Use the extended transmission timeout for this
        destination.
        Setting the extended timeout bit causes the stack to set the ex-
        tended transmission timeout for the destination address.
        All unused and unsupported bits must be set to 0.
        :return: the command options
        """
        return self._command_options

    @BaseRequest.frame_data.getter
    def frame_data(self):
        """
        Calculates the whole Frame Data for the request from the data it has.
        :rtype : bytearray
        :return: A bytearray that contains all the information for the packets.
        """
        data = bytearray()
        data.append(self.frame_type.value)
        data.append(self.frame_id)
        data.extend(self.address.serialize)
        data.append(self.command_options)
        data.extend(self.at_command)
        try:
            data.append(self.parameter)
        except TypeError:
            pass
        return data

    def __init__(self, frame_id, address, command_options, at_command,
                 parameter=None):
        self._frame_id = frame_id
        self._address = address
        self._command_options = command_options
        self._at_command = at_command
        self._parameter = parameter