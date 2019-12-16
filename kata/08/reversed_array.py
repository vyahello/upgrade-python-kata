"""
Your task is to convert number to reversed array of digits.

51037 -> [7, 3, 0, 1, 5]
"""

from typing import List


def digitalize(number: int) -> List[int]:
    "Convert number to reversed array of digits."
    return list(map(int, str(number)))[::-1]


if __name__ == "__main__":
    print(digitalize(4567))  # -> [7, 6, 5, 4]
    print(digitalize(4321))  # -> [1, 2, 3, 4]

