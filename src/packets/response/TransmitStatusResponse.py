__author__ = 'siim'

from packets.BaseResponse import BaseResponse
from packets.constants.FrameTypes import FrameType
from packets.constants.DeliveryStatuses import DeliveryStatus
from packets.constants.DiscoveryStatuses import DiscoveryStatus
from xbee.XbeeAddress import XbeeAddress


class TransmitStatusResponse(BaseResponse):

    frame_type = FrameType.tx_response

    def __init__(self):
        self._frame_id = None
        self._address = None
        self._transmit_retry_count = None
        self._delivery_status = None
        self._discovery_status = None

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
        this only has the 16-bit network address the packets was delivered to.
        If not successful, matches the destination network address that was provided in the Transmit Request frame.
        :return: The Address.
        """
        return self._address

    @property
    def transmit_retry_count(self):
        """
        The number of application transmission retries that took place.
        """
        return self._transmit_retry_count

    @property
    def delivery_status(self):
        return DeliveryStatus(self._delivery_status)

    @property
    def discovery_status(self):
        return DiscoveryStatus(self._discovery_status)

    def fill_data(self, data):
        """
        Fill the packets data properties.
        :param data: The Frame Data for the packets.
        """
        self._data = data
        #TODO check if the data locations make sense.
        self._frame_id = data[4]
        self._address = XbeeAddress(None, None, data[5:6])
        self._transmit_retry_count = data[7]
        self._delivery_status = data[8]
        self._discovery_status = data[9]