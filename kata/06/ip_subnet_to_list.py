"""
Generate a sorted list of all possible IP addresses in a network.

For a subnet that is not a valid IPv4 network return None.

Examples
#ipsubnet2list("192.168.1.0/31") == ["192.168.1.0", "192.168.1.1"]
#ipsubnet2list("213.256.46.160/28") == None
"""
from typing import List
import ipaddress


def ip_subnet_to_list(subnet: str) -> List[str]:
    """Generate list all possible ip addresses from a network.

    Examples:
        >>> assert ip_subnet_to_list("192.168.1.0/31") == ["192.168.1.0", "192.168.1.1"]
        >>> assert ip_subnet_to_list("213.256.46.160/28") is None
    """
    try:
        return list(map(str, ipaddress.IPv4Network(subnet)))
    except ipaddress.AddressValueError:
        return None


if __name__ == "__main__":
    print(ip_subnet_to_list("192.168.1.0/31"))
