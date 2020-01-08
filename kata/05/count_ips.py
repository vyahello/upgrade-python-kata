"""
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including
 the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.


# ips_between("10.0.0.0", "10.0.0.50")  ==   50
# ips_between("10.0.0.0", "10.0.1.0")   ==  256
# ips_between("20.0.0.10", "20.0.1.0")  ==  246
"""
import ipaddress


def ips_between(start: str, end: str) -> int:
    """
    Examples:
        >>> assert ips_between("10.0.0.0", "10.0.0.50") == 50
        >>> assert ips_between("20.0.0.10", "20.0.1.0") == 246
    """
    return int(ipaddress.IPv4Address(end)) - int(ipaddress.IPv4Address(start))


if __name__ == "__main__":
    print(ips_between("10.0.0.0", "10.0.0.50"))
    print(ips_between("20.0.0.10", "20.0.1.0"))
