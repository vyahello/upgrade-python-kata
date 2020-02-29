"""
Given a 2D list of size m * n. Your task is to find the sum of minimum value in each row.

For Example:

[
  [1,2,3,4,5], # minimum value of row is 1
  [5,6,7,8,9], # minimum value of row is 5
  [20,21,34,56,100] # minimum value of row is 20
]
"""

from typing import List

_ListOfLists = List[List[int]]


def sum_of_minimums(numbers: _ListOfLists) -> int:
    """Returns sum of minimums in an array of arrays

    Args:
        numbers:

    Examples:
        >>> assert sum_of_minimums([[0, 1, 2], [3, 4, 5], [6, 7, 8]]) == 9
    """
    return sum(map(min, numbers))


if __name__ == "__main__":
    print(sum_of_minimums([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
