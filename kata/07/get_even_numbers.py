"""
In Python, there is a built-in filter function that operates similarly to JS's filter.
For more information on how to use this function, visit https://docs.python.org/3/library/functions.html#filter

The solution would work like the following:

get_even_numbers([2,4,5,6]) => [2,4,6]
"""


def get_even_numbers(array: list) -> list:
    """Returns the row sums.

    Args:
        array (list): input array of numbers.

    Returns:
        array (list): sorted array of numbers.

    Examples:
        >>> assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    """
    return list(filter(lambda number: not number % 2, array))


if __name__ == "__main__":
    print(get_even_numbers([1, 2, 3, 4, 5, 6]))
