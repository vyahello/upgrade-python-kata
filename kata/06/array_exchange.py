"""
Array Exchange and Reversing

It's time for some array exchange!
The objective is simple: exchange the elements of two arrays in-place in a way that their new content is also reversed.
"""

from typing import Any, List


def exchange_with(first: List[Any], second: List[Any]) -> None:
    """Returns reversed arrays with exchanged values.

    Args:
        first (List[Any]): an array
        second (List[Any]): an array

    Examples:
        >>> first: List[Any] = [1, 2, 3]
        >>> second: List[Any] = ["a", "b", "c"]
        >>> exchange_with(first, second)
        >>> assert first == ["c", "b", "a"]
        >>> assert second == [3, 2, 1]
    """
    from_first: List[Any] = list(first)
    first.clear()
    first.extend(second[::-1])
    second.clear()
    second.extend(from_first[::-1])


def exchange_with_pythonic(first: List[Any], second: List[Any]) -> None:
    """Returns reversed arrays with exchanged values (pythonic).

    Args:
        first (List[Any]): an array
        second (List[Any]): an array

    first[:] is a slice of all array

    Examples:
        >>> first: List[Any] = [1, 2, 3]
        >>> second: List[Any] = ["a", "b", "c"]
        >>> exchange_with_pythonic(first, second)
        >>> assert first == ["c", "b", "a"]
        >>> assert second == [3, 2, 1]
    """
    first[:], second[:] = second[::-1], first[::-1]


if __name__ == "__main__":
    first: List[int] = [1, 2, 3]
    second: List[str] = ["a", "b", "c"]
    exchange_with(first, second)
    print(first, second)
