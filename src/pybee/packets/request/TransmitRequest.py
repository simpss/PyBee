from pybee.packets import BaseRequest
from pybee.packets.constants.FrameTypes import FrameType

class TransmitRequest(BaseRequest):

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
    def address(self):
        """
        The address of the xbee where the packets should be sent.
        :rtype: XbeeAddress
        :return: the Address.
        """
        return self._address

    @property
    def broadcast_radius(self):
        """
        Sets maximum number of hops a broadcast transmission can take.
        If set to 0, the broadcast radius will be set to the maximum hops
        value.
        """
        return self._broadcast_radius

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

    @property
    def rf_data(self):
        """
        Data that is sent to the destination device.
        :rtype: bytearray
        """
        return self._rf_data

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
        data.extend(self.address.serialize)
        data.append(self.command_options)
        data.extend(self.rf_data)
        return data