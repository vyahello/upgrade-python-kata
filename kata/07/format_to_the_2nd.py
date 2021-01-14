"""
Given some positive integers, I wish to print the integers such that all
take up the same width by adding a minimum number of leading zeroes.
No leading zeroes shall be added to the largest integer.

For example, given 1, 23, 2, 17, 102, I wish to print out
these numbers as follows:

001
023
002
017
102
Write a function that takes a variable number of integers and returns
the string to be printed out.
"""


def print_nums(*numbers: int) -> str:
    """Fill numbers with zeros.

    Args:
        *numbers: <int> sequence of numbers

    Returns: zero filled string.

    Examples:
        >>> assert print_nums(1, 12, 23) == '01 12 23'
    """
    if not len(numbers):
        return ''
    largest_number = max(len(str(next_num)) for next_num in numbers)
    return ' '.join(map(lambda item: str(item).zfill(largest_number), numbers))


def print_nums_opt(*numbers: int) -> str:
    """Fill numbers with zeros (optimizible).

    Args:
        *numbers: <int> sequence of numbers

    Returns: zero filled string.

    Examples:
        >>> assert print_nums_opt(1, 12, 23) == '01 12 23'
    """
    return ' '.join(str(num).zfill(len(max(str(num)))) for num in numbers)


if __name__ == '__main__':
    print(print_nums(1, 12, 23))
    print(print_nums_opt(1, 12, 23))
