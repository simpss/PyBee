from enum import Enum


class DiscoveryStatus(Enum):
    no_discovery_overhead = 0x00
    address_discovery = 0x01
    route_discovery = 0x02
    address_and_route = 0x03
    extended_timeout_discovery = 0x40