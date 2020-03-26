"""
Determine the total number of digits in the integer (n>=0) given as input to the function.
For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. Be careful to avoid overflows/underflows.

All inputs will be valid.
"""


def digits(number: int) -> int:
    """Counts number of digits.

    Args:
        number (int): given input number

    Examples:
        >>> assert digits(66) == 2
    """
    return len(str(number))


if __name__ == "__main__":
    print(digits(66))
