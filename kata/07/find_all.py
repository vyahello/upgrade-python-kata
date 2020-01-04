"""
Given an array (a list in Python) of integers and an integer n, find all occurrences of n in the given array and return
another array containing all the index positions of n in the given array.

If n is not in the given array, return an empty array [].

Assume that n and all values in the given array will always be integers.

Example:

find_all([6, 9, 3, 4, 3, 82, 11], 3)
> [2, 4]
"""
from typing import List


def find_all(array: List[int], number: int) -> List[int]:
    """Returns position number in an array.

    Examples:
        >>> assert find_all([6, 9, 3, 4, 3, 82, 11], 3) == [2, 4]
        >>> assert find_all([10, 16, 20, 6, 14, 11, 20, 2, 17, 16, 14], 16) == [1, 9]
    """
    return [index for index, value in enumerate(array) if value == number]


if __name__ == "__main__":
    print(find_all([6, 9, 3, 4, 3, 82, 11], 3))  # -> [2, 4]
