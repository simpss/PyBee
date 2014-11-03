from pybee.packets.request import RemoteAtCommand
from pybee.packets.response import RemoteAtResponse
from pybee.xbee import AtCommand

from pybee.packets.constants.CommandOptions import CommandOption


def change_pin(xbee_local, xbee_remote, pin, to_value):
    """
    :type xbee_local: Xbee
    :type xbee_remote: Xbee
    :type pin: Pin
    :type to_value: AtCommand
    :param xbee_local: the local xbee that is used with the serial port.
    :param xbee_remote: the remote xbee that receives the packets and does the deed.
    :param pin: The pin to change.
    :param to_value: what value should the pin have after this method? ATcommand.digital_output_high or _low?
    :rtype: RemoteAtResponse
    :return: the response packet.
    """
    frame_id = 0x01
    command_option = CommandOption.apply_changes.value
    at_command = pin.value.get_command

    request = RemoteAtCommand(frame_id, xbee_remote.address, command_option, at_command, to_value)

    xbee_local.send_request(request)
    response = xbee_local.listen_for_response(RemoteAtResponse())

    return response