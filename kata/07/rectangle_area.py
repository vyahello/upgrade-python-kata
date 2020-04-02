"""
Find the area of a rectangle when provided with one diagonal and one side of the rectangle.

If the input diagonal is less than or equal to the length of the side, return "Not a rectangle".
If the resultant area has decimals round it to two places.
"""
import math
from typing import Union


def area(diagonal: int, side: int) -> Union[int, float, str]:
    """Returns rectangle area by given diagonal and side numbers

    Args:
        diagonal (int): rectangle diagonal e.g 5
        side (int): rectangle diagonal e.f 3

    Examples:
        >>> assert area(5, 4) == 12
        >>> assert area(10, 6) == 48
    """
    return "Not a rectangle" if diagonal <= side else round(side * math.sqrt(diagonal ** 2 - side ** 2), 2)


if __name__ == "__main__":
    print(area(5, 4))
