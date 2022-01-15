"""
You will be given an array and a limit value.
You must check that all values in the array are below or equal to the limit value.
If they are, return true. Else, return false.

You can assume all values in the array are numbers.
"""


def small_enough(array: list, limit: int) -> bool:
    """Check if all values in the array are below or equal to the limit.

    Args:
        array: <list> list of integers.
        limit: <int> limit integer.

    Returns:

    Examples:
        >>> assert small_enough([1, 2, 3], 4)
    """
    return all(v <= limit for v in array)


if __name__ == '__main__':
    small_enough([1, 2, 3], 4)
