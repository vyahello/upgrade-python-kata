"""
Given a number, return the maximum value by rearranging its digits.

(123) => 321 (786) => 876 ("001") => 100 (999) => 999 (10543) => 54310
"""
from typing import Union


def rotate_to_max(number: Union[str, int]) -> int:
    """Sort number from the highest value to the lowest.

    Args:
        number: (str) given input string

    Returns: (int) sorted a number

    Examples:
        >>> assert rotate_to_max('19801') == 98110
    """

    return int(''.join(sorted(str(number), reverse=True)))


if __name__ == '__main__':
    print(rotate_to_max('19801'))
