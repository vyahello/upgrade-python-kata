"""
Create a factorial function.
"""
from functools import reduce


def factorial_reduce(number: int) -> int:
    """Factorial with reduce function.

    Examples:
        >>> assert factorial_reduce(0) == 1
        >>> assert factorial_reduce(1) == 1
        >>> assert factorial_reduce(2) == 2
        >>> assert factorial_reduce(3) == 6
    """
    return (
        1
        if number in (0, 1)
        else reduce(lambda x, y: x * y, range(1, number + 1))
    )


def factorial_pythonic(number: int) -> int:
    """Factorial with reduce function (pythonic approach).

    Examples:
        >>> assert factorial_pythonic(0) == 1
        >>> assert factorial_pythonic(1) == 1
        >>> assert factorial_pythonic(2) == 2
        >>> assert factorial_pythonic(3) == 6
    """
    return 1 if number in (0, 1) else number * factorial_pythonic(number - 1)


if __name__ == "__main__":
    print(factorial_reduce(3))
    print(factorial_pythonic(3))
