"""
In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""


def high_and_low(numbers: str) -> str:
    """Return min and max values.

    Args:
        numbers: <str> a list of numbers

    Returns: <str> a max to min

    Examples:
        >>> assert high_and_low('1 2 3 4') == '1 4'

    """
    return f'{min(map(int, numbers.split()))} {max(map(int, numbers.split()))}'


def high_and_low_classic(numbers: str) -> str:
    """Return min and max values.

    Examples:
        >>> assert high_and_low_classic('1 2 3 4') == '1 4'

    """
    min_num = max_num = int(numbers[0])
    for number in map(int, numbers.split()):  # type: int
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number
    return f'{min_num} {max_num}'


if __name__ == '__main__':
    print(high_and_low('1 2 3 4'))
    print(high_and_low_classic('1 2 3 4'))
