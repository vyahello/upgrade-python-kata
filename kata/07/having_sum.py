"""
Task

Given a positive integer n, calculate the following sum:
n + n/2 + n/4 + n/8 + ...
"""


def having_sum(number: int) -> int:
    """Returns all elements of the sum are the results of integer division.

    Args:
        number (int): a number to get divisible from

    Examples:
        >>> assert having_sum(25) == 47
    """
    count: int = number
    while number:
        number //= 2
        count += number
    return count


def having_sum_recursive(number: int) -> int:
    """Returns all elements of the sum are the results of integer division.

    Args:
        number (int): a number to get divisible from

    Examples:
        >>> assert having_sum_recursive(25) == 47
    """
    if number == 1:
        return 1
    return number + having_sum_recursive(number // 2)


def having_sum_pythonic(number: int) -> int:
    """Returns all elements of the sum are the results of integer division.

    Args:
        number (int): a number to get divisible from

    Examples:
        >>> assert having_sum_pythonic(25) == 47
    """
    count: int = 0
    while number:
        count += number
        number >>= 1
    return count


if __name__ == "__main__":
    print(having_sum_pythonic(25))
    print(having_sum_recursive(25))
    print(having_sum_pythonic(25))
