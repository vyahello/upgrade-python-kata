"""
A zero-indexed array arr consisting of n integers is given.

The dominator of array arr is the value that occurs in more than half of the elements of arr.
For example, consider array arr such that arr = [3,4,3,2,3,1,3,3]
The dominator of arr is 3 because it occurs in 5 out of 8 elements of arr and 5 is more than a half of 8.
"""
from typing import List


def dominator(array: List[int]) -> int:
    """Returns most occurred number (dominator) in an array.

    Args:
        array (List[int]): an array

    Examples:
        >>> assert dominator([3,4,3,2,3,1,3,3]) == 3
    """
    for value in array:  # type: int
        if array.count(value) > len(array) / 2:
            return value
    return -1


if __name__ == "__main__":
    print(dominator([3, 4, 3, 2, 3, 1, 3, 3]))
