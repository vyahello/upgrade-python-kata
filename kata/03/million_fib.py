"""
In this kata you will have to calculate fib(n) where:

fib(0) := 0
fib(1) := 1
fin(n + 2) := fib(n + 1) + fib(n)
"""
from typing import Generator, Sequence
from itertools import islice


def generator(number: int) -> Generator[int, None, None]:
    counter, handler = 0, 1
    while True:
        yield counter
        counter, handler = handler, counter + handler
        number -= 1


def fib(number: int) -> int:
    """Calculates the nth Fibonacci number.

    Examples:
        >>> assert fib(10) == 55
    """
    return next(islice(generator(number), number, number + 1))


def calculate(number: int) -> Sequence[int]:
    if number == 0:
        return 0, 1
    elif number == 1:
        return 1, 1
    else:
        first, second = calculate(number // 2)
        intermediate: int = first * (2 * second - first)
        quit_: int = second * second + first * first
        return (
            (intermediate, quit_)
            if not number % 2
            else (quit_, intermediate + quit_)
        )


def fib_efficient(number: int) -> int:
    """Calculates the nth Fibonacci number (efficient).

    Examples:
         >>> assert fib_efficient(10) == 55
    """
    if number >= 0:
        return calculate(number)[0]
    return -calculate(-number)[0] if not number % 2 else calculate(-number)[0]


if __name__ == "__main__":
    print(fib(10))
    print(fib_efficient(10))
