from pybee.packets.request import RemoteAtCommand
from pybee.packets.response import IODataResponse, RemoteAtResponse
from pybee.xbee import AtCommand, AtCommands

from pybee.xbee.Pins import Pin
from pybee.packets.constants.CommandOptions import CommandOption


def _calculate_temperature_tmp36(voltage):
    mV = voltage * 1000
    temp = (mV - 500) / 10
    return temp


def read_pin(xbee_local, xbee_remote):

    #create the needed information for the packets to be created.
    configure_command_option = CommandOption.apply_changes.value
    configure_frame_id = 0x01
    configure_at_command = Pin.DIO_2.value.get_command

    sample_command_option = CommandOption.apply_changes.value
    sample_frame_id = 0x02
    sample_at_command = AtCommands.sample_force.value.get_command

    #create the needed packets.
    configure_request = RemoteAtCommand(configure_frame_id, xbee_remote.address, configure_command_option, configure_at_command, AtCommand.analog_input_single_ended)
    sample_request = RemoteAtCommand(sample_frame_id, xbee_remote.address, sample_command_option, sample_at_command)

    xbee_local.send_request(configure_request)
    configure_response = xbee_local.listen_for_response(RemoteAtResponse())

    xbee_local.send_request(sample_request)
    sample_request_response = xbee_local.listen_for_response(IODataResponse())

    print(configure_response)
    print(sample_request_response)
    print("digital channel mask: {}, analog channel mask: {}"
          .format(sample_request_response.samples.digital_channel_mask, sample_request_response.samples.analog_channel_mask))

    voltage = sample_request_response.samples.analog_samples_voltage[Pin.DIO_2]

    temperature = _calculate_temperature_tmp36(voltage)

    print("voltage: {}, temperature: {}".format(voltage, temperature))

    return sample_request_response.samples.analog_samples_voltage