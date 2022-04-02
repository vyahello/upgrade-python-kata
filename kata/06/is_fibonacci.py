"""
I would like for you to write me a function that when given a number
(n) returns the n-th number in the Fibonacci Sequence.
"""


def is_fibonacci(number: int) -> int:
    """Check if a given number if a fibonacci number.

    Examples:
        >>> assert is_fibonacci(8)
        >>> assert not is_fibonacci(10)
    """
    counter, value = 0, 1
    while number > counter:
        counter, value = value, counter + value
    return counter == number


if __name__ == '__main__':
    print(is_fibonacci(5))
    print(is_fibonacci(10))
