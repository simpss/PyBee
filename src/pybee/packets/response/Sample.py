__author__ = 'siim'

from pybee.packets.Helpers import pairwise, calculate_analog_voltage
from pybee.xbee.Pins import Pin


class Sample():

    def __init__(self, sample_data):
        self._sample_data = sample_data

        self._number_of_samples = sample_data[0]
        self._digital_channel_mask = sample_data[1:3]
        self._analog_channel_mask = sample_data[3:4]
        if self._digital_channel_mask == b'\x00\x00':
            self._digital_samples = None
            self._analog_samples = sample_data[4:len(sample_data)]
        else:
            self._digital_samples = sample_data[4:6]
            self._analog_samples = sample_data[6:len(sample_data)]

    @property
    def sample_data(self):
        """
        The whole data of the sample.
        """
        return self._sample_data

    @property
    def number_of_samples(self):
        """
        Number of sample sets included in the payload.
        """
        return self._number_of_samples

    @property
    def digital_channel_mask(self):
        """
        Bit mask field that indicates which digital I/O lines on
        the remote have sampling enabled (if any).
        """
        return self._digital_channel_mask

    @property
    def analog_channel_mask(self):
        """
        Bit mask field that indicates which analog I/O lines on
        the remote have sampling enabled (if any).
        """
        return self._analog_channel_mask

    @property
    def digital_samples(self):
        """
        If the sample set includes any digital I/O lines (digital
        channel mask > 0), these two bytes contain samples
        for all enabled digital I/O lines.
        DIO lines that do not have sampling enabled return 0.
        Bits in these two bytes map the same as they do in the
        Digital Channels Mask field.
        """
        return self._digital_samples

    @property
    def analog_samples(self):
        """
        If the sample set includes any analog input lines
        (analog channel mask > 0), each enabled analog input
        returns a 2-byte value indicating the A/D measurement
        of that input. Analog samples are ordered
        sequentially from AD0/DIO0 to AD3/DIO3, to the supply
        voltage.
        """
        return self._analog_samples

    @property
    def analog_samples_voltage(self):
        """
        these are the voltages calculated from the analog samples
        :rtype: dict
        :return: voltages. each pin with a value has the Pins enum as the key.
        """
        result = {}
        pairs = pairwise(self.analog_samples)

        activated_pins = self.activated_analog_pins

        for pin in activated_pins:
            result[pin] = calculate_analog_voltage(next(pairs))

        return result

    @property
    def activated_analog_pins(self):
        pins = []
        binary = bin(int.from_bytes(self.analog_channel_mask, byteorder='little'))
        on = '1'

        if binary[-1] == on:
            pins.append(Pin.DIO_0)
        if binary[-2] == on:
            pins.append(Pin.DIO_1)
        if binary[-3] == on:
            pins.append(Pin.DIO_2)
        if binary[-4] == on:
            pins.append(Pin.DIO_3)
        return pins

    @property
    def activated_digital_pins(self):
        pins = []
        bit_masks = [bin(self.digital_channel_mask[0]), bin(self.digital_channel_mask[1])]
        on = '1'
        try:
            if bit_masks[0][-3] == on:
                pins.append(Pin.PWM_0)
            if bit_masks[0][-4] == on:
                pins.append(Pin.DIO_11)
            if bit_masks[0][-5] == on:
                pins.append(Pin.DIO_12)
        except IndexError:
            pass

        try:
            if bit_masks[1][-1] == on:
                pins.append(Pin.DIO_0)
            if bit_masks[1][-2] == on:
                pins.append(Pin.DIO_1)
            if bit_masks[1][-3] == on:
                pins.append(Pin.DIO_2)
            if bit_masks[1][-4] == on:
                pins.append(Pin.DIO_3)
            if bit_masks[1][-5] == on:
                pins.append(Pin.DIO_4)
            if bit_masks[1][-6] == on:
                pins.append(Pin.DIO_5)
            if bit_masks[1][-7] == on:
                pins.append(Pin.DIO_6)
            if bit_masks[1][-8] == on:
                pins.append(Pin.DIO_7)
        except IndexError:
            pass

        return pins