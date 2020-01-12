"""
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8.
It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

perimeter(5)  should return 80
perimeter(7)  should return 216
"""
from typing import Generator


def fibonacci(number: int) -> Generator[int, None, None]:
    counter, handler = 0, 1
    while number >= 0:
        counter, handler = handler, counter + handler
        yield counter
        number -= 1


def perimeter(number: int) -> int:
    """Calculates perimeter of squares.

    Examples:
        >>> assert perimeter(5) == 80
        >>> assert perimeter(30) == 14098308
    """
    return 4 * sum(fibonacci(number))


def perimeter_pythonic(number: int) -> int:
    """Calculates perimeter of squares (pythonic).

    Examples:
        >>> assert perimeter_pythonic(5) == 80
        >>> assert perimeter_pythonic(30) == 14098308
    """
    counter, handler = 1, 2
    while number:
        counter, handler, number = handler, counter + handler, number - 1
    return 4 * (handler - 1)


if __name__ == "__main__":
    print(perimeter(5))
    print(perimeter_pythonic(5))
