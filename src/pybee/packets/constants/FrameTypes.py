from enum import Enum


class FrameType(Enum):
    at_command_immediate = 0x08
    at_command_queued = 0x09
    remote_command_request = 0x17
    at_command_response = 0x88
    modem_status = 0x8a
    tx_request = 0x10
    tx_response = 0x8b
    rx_received = 0x90
    rx_io_data_received = 0x92
    node_identification_indicator = 0x95
    remote_command_response = 0x97