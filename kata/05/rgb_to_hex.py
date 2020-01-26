"""

The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned.
The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:
"""


def rgb_to_hex(red: int, green: int, blue: int) -> str:
    """Converts RGB into hext string.

    Examples:
        >>> assert rgb_to_hex(1, 2, 3) == "010203"
    """

    def to_hex(number: int) -> str:
        if number > 255:
            return "FF"
        if number < 0:
            return "00"
        return f"{number:X}".zfill(2)

    return f"{to_hex(red)}{to_hex(green)}{to_hex(blue)}"


def rgb_to_hex_pythonic(*args: int) -> str:
    """Converts RGB into hex string (pythonic).

    Examples:
        >>> assert rgb_to_hex_pythonic(1, 2, 3) == "010203"
    """
    return "".join(map(lambda color: "{:02X}".format(min(max(0, color), 255)), args))


if __name__ == "__main__":
    print(rgb_to_hex(1, 2, 3))
    print(rgb_to_hex_pythonic(1, 2, 3))
