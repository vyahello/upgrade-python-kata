"""
Write a program that outputs the top n elements from a list.

Example:

largest(2, [7,6,5,4,3,2,1])
# => [6,7]
"""
from typing import List


def find_largest(number: int, from_list: List[int]) -> List[int]:
    """Find `n` largest elements from the list.

    Example:
        >>> assert find_largest(2, [1, 10, 8, 11]) == [10, 11]
    """

    return sorted(from_list)[-number:]


if __name__ == '__main__':
    print(find_largest(2, [1, 10, 8, 11])) == [10, 11]
