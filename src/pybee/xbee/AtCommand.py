__author__ = 'siim'


class AtCommand:
    """
    A class to represent a single AT command for the xbee.
    """
    disabled = 0x00
    unmonitored_digital_input = 0x00

    NA = 0x01
    RSSI_PWM = 0x01
    commissioning_btn_enabled = 0x01
    associated_indication_led = 0x01
    CTS_flow_control = 0x01

    analog_input_single_ended = 0x02

    monitored_digital_input = 0x03
    digital_input = 0x03

    digital_output_low = 0x04

    digital_output_high = 0x05

    RS_485_transmit_low_enable = 0x06
    RS_485_transmit_high_enable = 0x07

    @property
    def get_command(self):
        """
        Property to keep the command value.
        :return: command value.
        """
        return self._value

    def __init__(self, value):
        """
        create an AtCommand object.
        :type value: tuple
        :param value: the numerical value of the command.
        """
        self._value = value