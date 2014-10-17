__author__ = 'siim'

from enum import Enum


class DeliveryStatus(Enum):

    success = 0x00
    MAC_acknowledgment_failure = 0x01
    CCA_failure = 0x02
    destination_endpoint_invalid = 0x15
    network_ACK_failure = 0x21
    network_not_joined = 0x22
    self_addressed = 0x23
    address_not_found = 0x24
    route_not_found = 0x25
    broadcast_source_failed_hearing_relay_message = 0x26
    invalid_binding_index_table = 0x2B
    attempted_broadcast_with_APS_transmission = 0x2D
    attempted_unicast_with_APS_transmission_but_EE_is_0 = 0x2E
    data_payload_too_large = 0x74
    indirect_message_unrequested = 0x75

    resource_error_1 = 0x2C
    resource_error_2 = 0x32
    """Lack of free buffers, timers, or something similar."""