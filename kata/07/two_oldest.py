"""
The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age, oldest age].

The order of the numbers passed in could be any order. The array will always include at least 2 items.

For example:
    two_oldest_ages([1, 3, 10, 0]) # should return [3, 10]
"""
from typing import List


def two_oldest_ages(ages: List[int]) -> List[int]:
    """Returns a list of highest ages from given list of ages.

    Args:
        ages (List[int]): given list of ages

    Examples:
        >>> assert two_oldest_ages([1, 3, 10, 0]) == [3, 10]
    """
    return sorted(ages)[len(ages) - 2 : len(ages)]


if __name__ == "__main__":
    print(two_oldest_ages([1, 3, 10, 0]))
