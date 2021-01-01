"""
An array is given with palindromic and non-palindromic numbers.
A palindromic number is a number that is the same from a reversed order.
For example 122 is not a palindromic number, but 202 is one.

Your task is to write a function that returns an array with only 1s and 0s,
where all palindromic numbers are replaced with a 1 and all non-palindromic numbers are replaced with a 0.
"""
from typing import List


def convert_palindromes(numbers: List[int]) -> List[int]:
    """Converts numbers into palindromes values.

    Args:
        numbers (List[int]): a list of numbers

    Examples:
        >>> assert convert_palindromes([10, 11, 12, 121]) == [0, 1, 0, 1]
    """
    return list(
        map(
            lambda number_as_str: int(number_as_str == number_as_str[::-1]),
            map(str, numbers),
        )
    )


if __name__ == "__main__":
    print(convert_palindromes([10, 11, 12, 121]))
