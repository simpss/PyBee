from pybee.packets import Helpers
import struct


class BaseRequest:
    """
    A base class for an outgoing request to the Xbee.
    Can be used directly if the request type needed isn't implemented yet.
    """
    start_delimiter = 0x7E

    @property
    def frame_data(self):
        """
        the frame data content property.
        :return:
        """
        return self.frame_data

    @frame_data.setter
    def frame_data(self, frame_data):
        """
        the frame data content property setter.
        :param frame_data:
        """
        self.frame_data = frame_data

    @property
    def length(self):
        """
        Number of bytes between the length and the checksum.
        calculates and returns the length.
        :return: two bytes in big endian format.
        """
        return struct.pack("> h", len(self.frame_data))

    @property
    def checksum(self):
        """
        Checksum property. Calculates the checksum.
        :return: the checksum for frame data.
        """
        return Helpers.calculate_checksum(self.frame_data)

    @property
    def serialize(self):
        """
        Creates the whole request from the data it has.
        :return: A bytearray that can be sent to the xbee via serial.
        """
        data = bytearray()
        data.append(self.start_delimiter)
        data.extend(self.length)
        data.extend(self.frame_data)
        data.append(self.checksum)
        return data