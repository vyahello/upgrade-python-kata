"""
In this kata you will have to calculate fib(n) where:

fib(0) := 0
fib(1) := 1
fin(n + 2) := fib(n + 1) + fib(n)
"""
from typing import Generator
from itertools import islice


def generator(number: int) -> Generator[int, None, None]:
    counter, handler = 0, 1
    while True:
        yield counter
        counter, handler = handler, counter + handler
        number -= 1


def fib(number: int) -> int:
    """Calculates the nth Fibonacci number"""
    return next(islice(generator(number), number, number + 1))
