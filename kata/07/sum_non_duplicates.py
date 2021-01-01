"""
Please write a function that sums a list, but ignores any duplicate items
in the list.

For instance, for the list [3, 4, 3, 6] , the function should return 10.
"""
from typing import List


def sum_no_duplicates(items: List[int]) -> int:
    """Sums no duplicated items in a list.

    Args:
        items: list of numbers

    Examples:
        >>> sum_no_duplicates([3, 4, 3, 6]) == 10
    """
    return sum(number for number in items if items.count(number) == 1)


def sum_no_duplicates_filter(items: List[int]) -> int:
    """Sums no duplicated items in a list.

    Args:
        items: list of numbers

    Examples:
        >>> sum_no_duplicates_filter([3, 4, 3, 6]) == 10
    """
    return sum(filter(lambda number: items.count(number) == 1, items))


if __name__ == "__main__":
    print(sum_no_duplicates([3, 4, 3, 6]))
    print(sum_no_duplicates_filter([3, 4, 3, 6]))
