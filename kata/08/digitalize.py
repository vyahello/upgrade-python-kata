"""
Your task is to convert number to reversed array of digits.

51037 -> [7, 3, 0, 1, 5]

-----------------------------------
For doctests run following command:
python -m xdoctest -v digitalize.py
or
python3 -m xdoctest -v digitalize.py

For manual testing run:
python digitalize.py
"""

from typing import List


def digitalize(number: int) -> List[int]:
    """Convert number to reversed array of digits.

    Examples:
        >>> assert digitalize(4567) == [7, 6, 5, 4]
        >>>
        >>> assert digitalize(4321) == [1, 2, 3, 4]
    """
    return list(map(int, str(number)))[::-1]


if __name__ == "__main__":
    print(digitalize(4567))  # -> [7, 6, 5, 4]
    print(digitalize(4321))  # -> [1, 2, 3, 4]
