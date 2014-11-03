from pybee.packets import BaseResponse
from pybee.xbee import XbeeAddress

__author__ = 'siim'

import serial


class Xbee:
    """
    A class to represent an Xbee.
    """

    def __init__(self):
        self._address = None
        self._port = None
        self._baud = None
        self._serial = None

    @property
    def address(self):
        """
        The address for the Xbee.
        :rtype: XbeeAddress
        """
        return self._address

    @property
    def port(self):
        """
        The port address for the serial connection(eg: /dev/ttyUSB0)
        """
        return self._port

    @property
    def baud(self):
        """
        The Baud rate for the serial connection.
        """
        return self._baud

    @property
    def serial(self):
        """
        The serial connection for the Xbee.
        """
        return self._serial

    def setup_remote(self, address):
        """
        set up the xbee as a remote node.
        :rtype: Xbee
        :return: the set up xbee, itself.
        """
        self._address = address
        return self

    def setup_local(self, port, baud):
        """
        set up the xbee as a local node that can be communicated with a serial connection.
        :rtype: Xbee
        :return: the set up Xbee, itself.
        """
        self._port = port
        self._baud = baud
        self._serial = serial.Serial(self.port, self.baud)
        return self

    def send_request(self, request):
        """
        Sends the given request to the xbees Serial port.
        :type request: BaseRequest
        :param request: The request to be sent, usually extends BaseRequest
        """
        self.serial.write(request.serialize)

    def listen_for_response(self, expected_response):
        """
        Reads the response from the Serial port specified in settings.py, returns the packets as a string. This is a BLOCKING call
        :type expected_response: BaseResponse
        :param expected_response: an empty response with the expected response implementation.
        :return: the expected_response with data filled from the serial communication.
        """
        #read serial until the packet start is found.
        packet_start = b'~'
        while self.serial.read(1) != packet_start:
            pass

        read_length = self.serial.read(2)
        #calculate the length of the packets
        length = (read_length[0] * 0xFF) + read_length[1] + 1

        #read in the rest of the packet
        data = self.serial.read(length)
        #fill the response with data.
        expected_response.fill_data(packet_start + read_length + data)
        return expected_response