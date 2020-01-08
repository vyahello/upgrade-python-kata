"""
Write a function ip_to_int32(ip) ( JS: ipToInt32(ip) ) that takes an IPv4 address and returns a 32 bit number.
"""


import ipaddress


def ip_to_int32(ip: str) -> int:
    """
    Examples:
        >>> assert ip_to_int32("128.114.17.104") == 2154959208
    """
    return int(ipaddress.IPv4Address(ip))


if __name__ == "__main__":
    print(ip_to_int32("128.114.17.104"))
