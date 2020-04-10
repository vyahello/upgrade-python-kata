"""
I would like for you to write me a function that when given a number
(n) returns the n-th number in the Fibonacci Sequence.
"""


def nth_fibonacci(number: int) -> int:
    """Returns value of nth fibonacci sequence.

    Args:
        number (int): sequential number

    Examples:
        >>> assert nth_fibonacci(4) == 2
    """
    number -= 1
    counter, helper = 0, 1
    while number:
        counter, helper = helper, counter + helper
        number -= 1
    return counter


def nth_fibonacci_alt(number: int) -> int:
    """Returns value of nth fibonacci sequence (alternative).

    Args:
        number (int): sequential number

    Examples:
        >>> assert nth_fibonacci_alt(4) == 2
    """
    counter, helper = 0, 1
    for _ in range(number - 1):  # type: int
        counter, helper = helper, counter + helper
    return counter


if __name__ == "__main__":
    print(nth_fibonacci(4))
    print(nth_fibonacci_alt(4))
