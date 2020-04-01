"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1)
"""


def row_sum_odd_numbers(number: int) -> int:
    """Returns the row sums.

    Args:
        number (int): input number to evaluate

    Examples:
        >>> assert row_sum_odd_numbers(1) == 1
        >>> assert row_sum_odd_numbers(2) == 8
        >>> assert row_sum_odd_numbers(13) == 2197
        >>> assert row_sum_odd_numbers(19) == 6859
        >>> assert row_sum_odd_numbers(41) == 68921
    """
    return number ** 3


if __name__ == "__main__":
    print(row_sum_odd_numbers(19))
