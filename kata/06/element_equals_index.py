"""
Given a sorted array of distinct integers, write a function index_equals_value that returns the lowest index for which
array[index] == index. Return -1 if there is no such index.

Your algorithm should be very performant.

[input] array of integers ( with 0-based nonnegative indexing )
[output] integer
"""
import math
from typing import Sequence


def index_search(array: Sequence[int], low: int, high: int) -> int:
    """Searches index of an array by given low and high values."""
    if low > high:
        return -1
    median: int = math.floor(high + low / 2)
    if array[median] == median:
        left_value: int = index_search(array, low, median - 1)
        if left_value != -1 and left_value < median:
            return left_value
        return median
    if array[median] > median:
        return index_search(array, low, median - 1)
    return index_search(array, median + 1, high)


def index_equals_value(array: Sequence[int]) -> int:
    """Returns the lowest index for which array[index] == index.

    Args:
        array (Iterable[int]): a list of numbers

    Examples:
        >>> assert index_equals_value((-3, 0, 1, 3, 10)) == 3
        >>> assert index_equals_value((9,10,11,12,13,14)) == -1
    """
    return index_search(array, 0, len(array) - 1)


if __name__ == "__main__":
    print(index_equals_value((-3, 0, 1, 3, 10)))
    print(index_equals_value((9, 10, 11, 12, 13, 14)))
