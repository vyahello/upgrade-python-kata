"""
Task

Given a number, Return `The Maximum number` could be formed from the digits of the number given .
"""


def max_number(number: int) -> int:
    """Returns number starting from the largest item.

    Args:
        number (int): input number

    Examples:
        >>> assert max_number(132) == 321
    """
    return int("".join(sorted(tuple(str(number)), reverse=True)))


if __name__ == "__main__":
    print(max_number(132))
