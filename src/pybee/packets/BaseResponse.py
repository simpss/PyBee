from pybee.packets import Helpers



class BaseResponse():
    """
    A base class for an incoming response.
    Can be used directly if the response type needed isn't implemented yet.
    """

    @property
    def data(self):
        """
        The whole data for the response.
        :return:
        """
        return self._data

    @property
    def frame_data(self):
        """
        The frame data for the response
        """
        return self._frame_data

    @property
    def data_length(self):
        """
        Number of bytes between the length and the checksum.
        read from the response.
        :return: the data length.
        """
        return self._data_length

    @property
    def checksum(self):
        """
        The checksum, read form the response.
        :return:
        """
        return self._checksum

    @property
    def calculated_checksum(self):
        """
        The checksum, Recalculated.
        :return:
        """
        return Helpers.calculate_checksum(self.frame_data)

    def __init__(self):
        self._data = None

        self._data_length = None
        self._frame_data = None
        self._checksum = None

    def fill_data(self, data):
        """
        Fill the packets data properties. To be overwritten while extending the packets.
        :param data: The whole data for the packets.
        """
        self._data = data

        self._data_length = data[1:3]
        self._frame_data = data[3:-2]
        self._checksum = data[-1]
        #raise NotImplementedError("This method should have been implemented when extending the BaseResponse class.")