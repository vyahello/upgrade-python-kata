"""
An IP address contains four numbers(0-255) and separated by dots. It can be converted to a number by this way:

Given a string s represents a number or an IP address.
Your task is to convert it to another representation(number to IP address or IP address to number).

You can assume that all inputs are valid.

For s = "10.0.3.193", the output should be "167773121".

For s = "167969729", the output should be "10.3.3.193".
"""

import ipaddress


def number_and_ip_address(string: str) -> str:
    """
    Examples:
        >>> assert number_and_ip_address("10.0.3.193") == "167773121"
        >>> assert number_and_ip_address("167969729") == "10.3.3.193"
    """
    return (
        str(int(ipaddress.IPv4Address(string)))
        if "." in string
        else str(ipaddress.IPv4Address(int(string)))
    )


if __name__ == "__main__":
    print(number_and_ip_address("10.0.3.193"))
