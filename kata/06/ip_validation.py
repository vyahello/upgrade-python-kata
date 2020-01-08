"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Input to the function is guaranteed to be a single string.

Examples
Valid inputs:

1.2.3.4
123.45.67.89
Invalid inputs:

1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
"""
import re


def is_valid_ip(ip: str) -> bool:
    """Checks if ip address is valid

    Examples:
        >>> assert is_valid_ip('12.255.56.1')
        >>> assert not is_valid_ip('1.1.1')
    """
    octets = ip.split(".")
    if not octets or len(octets) != 4:
        return False
    return all(map(lambda octet: octet in map(str, range(256)), octets))


def is_valid_ip_re(ip: str) -> bool:
    """Checks if ip address is valid

    Examples:
        >>> assert is_valid_ip('12.255.56.1')
        >>> assert not is_valid_ip('1.1.1')
    """
    return bool(re.compile(r"[0-256]\.[0-256]\.[0-256]\.[0-256]").search(ip))


if __name__ == "__main__":
    print(is_valid_ip("12.255.56.1"))
    print(is_valid_ip_re("12.255.56.1"))
