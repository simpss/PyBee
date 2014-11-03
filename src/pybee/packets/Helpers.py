from itertools import tee


def calculate_checksum(data):
    """
    Calculates the checksum for the packets.
    :param data: Packet data content.
    :return: Packet Checksum.
    """
    res = 0
    #sum the data bytes
    for byte in data:
        res += byte
    #keep the last byte
    res = res & 0xFF
    #subtract
    return 0xff - res


def calculate_analog_voltage(values):
    """
    Calculates the analog voltage from given values.
    :param values: the response data that indicates the value.
    :return: analog voltage of the inputted data values.
    """
    reading = values[1] + (values[0] * 256)
    voltage = reading / 1019 * 1.19
    return voltage


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return __izip(a, b)


def __izip(*iterables):
    # izip('ABCD', 'xy') --> Ax By
    iterators = map(iter, iterables)
    while iterators:
        yield tuple(map(next, iterators))