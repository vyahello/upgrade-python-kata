"""
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""


def square_digits(number: int) -> int:
    """Calculates square of a digit.

    Examples:
        >>> assert square_digits(9119) == 811181
    """
    return int("".join(map(lambda item: str(int(item) ** 2), str(number))))


if __name__ == "__main__":
    print(square_digits(9119))
