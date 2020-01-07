"""
For doctests run following command:
python -m xdoctest -v most_frequent.py
or
python3 -m xdoctest -v most_frequent.py

For manual testing run:
python most_frequent.py
"""
from typing import List, Set


def find_most_frequent(array: List[int]) -> Set[int]:
    """Finds most frequent values in array.

    Examples:
        >>> assert find_most_frequent([1, 1, 1, 2, 2, 3]) == {1, 2}
    """
    return set(number for number in array if array.count(number) > 1)


if __name__ == "__main__":
    print(find_most_frequent([1, 1, 1, 2, 2, 3]))
