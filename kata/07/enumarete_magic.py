"""
Create a function called one that accepts two params:

a sequence
a function
and returns true only if the function in the params returns true for exactly one item in the sequence.
"""
from typing import Sequence, Callable


def one(sequence: Sequence[int], function: Callable[[int], bool]) -> bool:
    """"Returns true for exactly one item in the sequence.

    Args:
        sequence (Sequence[int]): a sequence of numbers
        function (Callable[[int], bool]): a function to call

    Examples:
        >>> assert one([1, 3, 5, 6, 99, 1, 3], lambda number: number > 10)
        >>> assert not one([1, 3, 5, 6, 99, 88, 3], lambda number: number > 10)
        >>> assert not one([1, 3, 5, 6, 5, 1, 3], lambda number: number > 10)
    """
    return len(tuple(filter(function, sequence))) == 1


def one_pythonic(sequence: Sequence[int], function: Callable[[int], bool]) -> bool:
    """"Returns true for exactly one item in the sequence (pythonic).

    Args:
        sequence (Sequence[int]): a sequence of numbers
        function (Callable[[int], bool]): a function to call

    Examples:
        >>> assert one_pythonic([1, 3, 5, 6, 99, 1, 3], lambda number: number > 10)
        >>> assert not one_pythonic([1, 3, 5, 6, 99, 88, 3], lambda number: number > 10)
        >>> assert not one_pythonic([1, 3, 5, 6, 5, 1, 3], lambda number: number > 10)
    """
    return sum(map(function, sequence)) == 1


if __name__ == "__main__":
    print(one([1, 3, 5, 6, 99, 1, 3], lambda number: number > 10))
    print(one_pythonic([1, 3, 5, 6, 99, 1, 3], lambda number: number > 10))
