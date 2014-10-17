__author__ = 'siim'

from enum import Enum
from xbee.AtCommand import AtCommand


class AtCommands(Enum):
    """
    An Enum to keep the different AT commands.
    """
    # DIO_0 = AtCommand((0x44, 0x30))
    # DIO_1 = AtCommand((0x44, 0x31))
    # DIO_2 = AtCommand((0x44, 0x32))
    # DIO_3 = AtCommand((0x44, 0x33))
    # DIO_4 = AtCommand((0x44, 0x34))
    # DIO_6 = AtCommand((0x44, 0x36))
    # DIO_7 = AtCommand((0x44, 0x37))
    # DIO_8 = AtCommand((0x44, 0x38))
    # PWM_0 = AtCommand((0x50, 0x30))
    # DIO_11 = AtCommand((0x50, 0x31))
    # DIO_12 = AtCommand((0x50, 0x32))
    # DIO_13 = AtCommand((0x50, 0x33))

    destination_address_high = AtCommand((0x44, 0x48))
    destination_address_low = AtCommand((0x44, 0x4C))
    network_address_16_bit = AtCommand((0x4D, 0x59))
    parent_network_address_16_bit = AtCommand((0x4D, 0x50))
    remaining_children_number = AtCommand((0x4E, 0x43))
    address_high = AtCommand((0x53, 0x48))
    address_low = AtCommand((0x53, 0x4C))
    node_identifier = AtCommand((0x4E, 0x49))
    source_endpoint = AtCommand((0x53, 0x45))
    destination_endpoint = AtCommand((0x44, 0x45))
    cluster_identifier = AtCommand((0x43, 0x49))
    maximum_RF_payload_bytes = AtCommand((0x4E, 0x50))
    device_type_identifier = AtCommand((0x44, 0x44))
    operating_channel = AtCommand((0x43, 0x48))
    extended_pan_id = AtCommand((0x49, 0x44))
    extended_operating_pan_id = AtCommand((0x4F, 0x50))
    maximum_unicast_hops = AtCommand((0x4E, 0x48))
    maximum_broadcast_hops = AtCommand((0x42, 0x48))
    pan_id_16_bit = AtCommand((0x4F, 0x49))
    node_discovery_timeout = AtCommand((0x4E, 0x54))
    network_discovery_options = AtCommand((0x4E, 0x4F))
    scan_channels = AtCommand((0x53, 0x43))
    scan_duration = AtCommand((0x53, 0x44))
    zigbee_stack_profile = AtCommand((0x5A, 0x53))
    node_join_time = AtCommand((0x4E, 0x4A))
    channel_verification = AtCommand((0x4A, 0x56))
    network_watchdog_timeout = AtCommand((0x4E, 0x57))
    join_notification = AtCommand((0x4A, 0x4E))
    aggregate_routing_notification = AtCommand((0x41, 0x52))
    encryption_enable = AtCommand((0x45, 0x45))
    encryption_options = AtCommand((0x45, 0x4F))
    network_encryption_key = AtCommand((0x4E, 0x4B))
    link_key = AtCommand((0x4B, 0x59))
    power_level = AtCommand((0x50, 0x4C))
    power_mode = AtCommand((0x50, 0x4D))
    received_signal_strength = AtCommand((0x44, 0x42))
    peak_power = AtCommand((0x50, 0x50))
    API_enable = AtCommand((0x41, 0x50))
    API_options = AtCommand((0x42, 0x4F))
    interface_data_rate = AtCommand((0x42, 0x44))
    serial_parity = AtCommand((0x4E, 0x42))
    stop_bits = AtCommand((0x53, 0x42))
    packetization_timeout = AtCommand((0x52, 0x4F))
    IO_sample_rate = AtCommand((0x49, 0x52))
    IO_digital_change_detection = AtCommand((0x49, 0x43))
    association_led_blink_time = AtCommand((0x4c, 0x54))
    pull_up_resistor = AtCommand((0x50, 0x52))
    RSSI_PWM_timer = AtCommand((0x52, 0x50))
    supply_voltage = AtCommand((0x25, 0x56))
    supply_voltage_monitoring = AtCommand((0x56, 0x2b))
    module_temperature = AtCommand((0x54, 0x50))
    firmware_version = AtCommand((0x56, 0x52))
    hardware_version = AtCommand((0x48, 0x56))
    association_indication = AtCommand((0x41, 0x49))
    command_mode_timeout = AtCommand((0x43, 0x54))
    command_mode_exit = AtCommand((0x43, 0x4E))
    guard_times = AtCommand((0x47, 0x54))
    command_sequence_character = AtCommand((0x43, 0x43))
    sleep_mode = AtCommand((0x53, 0x4D))
    sleep_number_of_periods = AtCommand((0x53, 0x4E))
    sleep_period = AtCommand((0x53, 0x50))
    sleep_time_before = AtCommand((0x53, 0x54))
    sleep_options = AtCommand((0x53, 0x4F))
    wake_host = AtCommand((0x57, 0x48))
    sleep_immediately = AtCommand((0x53, 0x49))
    polling_rate = AtCommand((0x50, 0x4F))
    apply_changes = AtCommand((0x41, 0x43))
    write = AtCommand((0x57, 0x52))
    restore_defaults = AtCommand((0x52, 0x45))
    software_reset = AtCommand((0x46, 0x52))
    network_reset = AtCommand((0x4E, 0x52))
    commission = AtCommand((0x43, 0x42))
    node_discover = AtCommand((0x4E, 0x44))
    destination_node = AtCommand((0x44, 0x4E))
    sample_force = AtCommand((0x49, 0x53))
    sample_sensor = AtCommand((0x31, 0x53))