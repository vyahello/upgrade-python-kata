"""
In this simple exercise, you will build a program that takes a value, integer, and returns
a list of its multiples up to another value, limit.

If limit is a multiple of integer, it should be included as well.
There will only ever be positive integers passed into the function, not consisting of 0.
The limit will always be higher than the base.

For example, if the parameters passed are (2, 6), the function should return
[2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.

If you can, try writing it in only one line of code.

-----------------------------------
For doctests run following command:
python -m xdoctest -v find_multiples.py
or
python3 -m xdoctest -v find_multiples.py

For manual testing run:
python find_multiples.py
"""

from typing import List


def find_multiples(integer: int, range_: int) -> List[int]:
    """Returns a list of multiplies of given integer range.

    Examples:
        >>> assert find_multiples(3, 15) == [3, 6, 9, 12, 15]
        >>>
        >>> assert find_multiples(2, 6) == [2, 4, 6]
    """
    return list(filter(lambda number: number % integer == 0, range(1, range_ + 1)))


if __name__ == "__main__":
    print(find_multiples(integer=3, range_=15))  # -> [3, 6, 9, 12, 15]
