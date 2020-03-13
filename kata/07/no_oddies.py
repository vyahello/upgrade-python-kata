"""
Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given.

def no_odds(values):
"""

from typing import List


def no_odds(values: List[int]) -> List[int]:
    """Returns no odd numbers from a list if numbers.

    Args:
        values (List[int]): a list of numbers

    Examples:
        >>> assert no_odds([1, 2, 10, 8]) == [2, 10, 8]
    """
    return list(filter(lambda number: not number % 2, values))


if __name__ == "__main__":
    print(no_odds([1, 2, 10, 8]))
