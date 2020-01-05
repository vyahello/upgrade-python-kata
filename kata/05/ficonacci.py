"""
You're going to provide a needy programmer a utility method that generates an infinite sized, sequential IntStream
(in TypeScript Iterator<number>, in Python generator) which contains all the numbers in a fibonacci sequence.

A fibonacci sequence starts with two 1s. Every element afterwards is the sum of the two previous elements. See:

1, 1, 2, 3, 5, 8, 13, ..., 89, 144, 233, 377, ...
"""
from itertools import islice
from typing import Generator


def fibonacci() -> Generator[int, None, None]:
    """Returns fibonacci generator.

    Examples:
        >>> assert tuple(islice(fibonacci(), 5)) == (1, 1, 2, 3, 5)
    """
    counter, helper = 1, 1
    while True:
        yield counter
        counter, helper = helper, counter + helper


if __name__ == "__main__":
    print(tuple(islice(fibonacci(), 5)))
