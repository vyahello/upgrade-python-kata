"""
Write a function that doubles every second integer in a list starting from the left.

double_every_other([1,2,3,4]) # -> [1, 4, 3, 8]
"""
from typing import List


def double_every_other_basic(items: List[int]) -> List[int]:
    """Doubles every second integer in a list starting

    Returns: a list of doubled items.

    Examples:
        >>> double_every_other_basic([1, 2, 3, 4]) == [1, 4, 3, 8]
    """
    for index, item in enumerate(items):  # type: int, int
        if index % 2:
            items[index] = item * 2
    return items


def double_every_other_func(items: List[int]) -> List[int]:
    """Doubles every second integer in a list starting

    Returns: a list of doubled items.

    Examples:
        >>> double_every_other_func([1, 2, 3, 4]) == [1, 4, 3, 8]
    """
    return list(
        map(
            lambda pair: pair[1] * 2 if pair[0] % 2 else pair[1],
            enumerate(items),
        )
    )


def double_every_other_main(items: List[int]) -> List[int]:
    """Doubles every second integer in a list starting

    Returns: a list of doubled items.

    Examples:
        >>> double_every_other_main([1, 2, 3, 4]) == [1, 4, 3, 8]
    """
    return [item * 2 if index % 2 else item for index, item in enumerate(items)]


double_every_other_lambda = lambda items: [
    item * 2 if index % 2 else item for index, item in enumerate(items)
]


if __name__ == "__main__":
    print(double_every_other_basic([1, 2, 3, 4]))
    print(double_every_other_func([1, 2, 3, 4]))
    print(double_every_other_main([1, 2, 3, 4]))
    print(double_every_other_lambda([1, 2, 3, 4]))
