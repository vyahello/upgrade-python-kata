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


def sum_of_minimums_non_efficient(numbers: _ListOfLists) -> int:
    """Returns a sum of minimums in an array of arrays (less efficient)

    Args:
        numbers: a list of numbers lists

    Examples:
        >>> assert sum_of_minimums_non_efficient([[0, 1, 2], [3, 4, 5], [6, 7, 8]]) == 9
    """
    minimum_numbers: List[int] = []
    for array in numbers:  # type: List[int]
        first_number: int = array[0]
        for number in array:  # type: int
            if number < first_number:
                first_number = number
        minimum_numbers.append(first_number)
    return sum(minimum_numbers)


def sum_of_minimums_good(numbers: _ListOfLists) -> int:
    """Returns a sum of minimums in an array of arrays (good way to operate)

    Args:
        numbers: a list of numbers lists

    Examples:
        >>> assert sum_of_minimums_good([[0, 1, 2], [3, 4, 5], [6, 7, 8]]) == 9
    """
    return sum(min(array) for array in numbers)


def sum_of_minimums_efficient(numbers: _ListOfLists) -> int:
    """Returns a sum of minimums in an array of arrays (pythonic)

    Args:
        numbers: a list of numbers lists

    Examples:
        >>> assert sum_of_minimums_efficient([[0, 1, 2], [3, 4, 5], [6, 7, 8]]) == 9
    """
    return sum(map(min, numbers))


if __name__ == "__main__":
    print(sum_of_minimums_non_efficient([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
    print(sum_of_minimums_efficient([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
    print(sum_of_minimums_good([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
