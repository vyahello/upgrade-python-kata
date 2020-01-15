"""
You've just discovered a square (NxN) field and you notice a warning sign.
The sign states that there's a single bomb in the 2D grid-like field in front of you.

Write a function mineLocation/MineLocation that accepts a 2D array, and returns the location of the mine.
The mine is represented as the integer 1 in the 2D array.
Areas in the 2D array that are not the mine will be represented as 0s.

The location returned should be an array (Tuple<int, int> in C#) where the first element is the row index,
and the second element is the column index of the bomb location (both should be 0 based).
All 2D arrays passed into your function will be square (NxN), and there will only be one mine in the array.
"""
from typing import List


def find_mine(field: List) -> List[int]:
    """Finds mine location.

    Examples:
        >>> assert find_mine([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [1, 1]
    """
    return [
        [top_index, inner_index]
        for top_index, top_value in enumerate(field)
        for inner_index, inner_value in enumerate(top_value)
        if inner_value != 0
    ][0]


def find_mine_pythonic(field: List) -> List[int]:
    """Finds mine location (pythonic).

    Examples:
        >>> assert find_mine([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [1, 1]
    """
    for sub_field in field:  # type: List
        if 1 in sub_field:
            return [field.index(sub_field), sub_field.index(1)]


def find_mine_pythonic_alt(field: List) -> List[int]:
    """Finds mine location (pythonic alternative).

    Examples:
        >>> assert find_mine([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [1, 1]
    """
    return next([field.index(sub_field), sub_field.index(1)] for sub_field in field if 1 in sub_field)


if __name__ == "__main__":
    print(find_mine([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(find_mine_pythonic([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(find_mine_pythonic_alt([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
