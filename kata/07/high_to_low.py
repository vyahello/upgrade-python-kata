"""
In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""


def high_and_low(numbers: str) -> str:
    """

    Args:
        numbers: <str> a list of numbers

    Returns: <str> a max to min

    Examples:
        >>> assert high_and_low('1 2 3 4') == '1 4'

    """
    return f'{max(map(int, numbers.split()))} {min(map(int, numbers.split()))}'


if __name__ == '__main__':
    print(high_and_low('1 2 3 4'))
