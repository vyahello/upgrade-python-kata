"""
You have a positive number n consisting of digits. You can do at most one operation:
Choosing the index of a digit in the number, remove this digit at that index and insert it back to another or at the
same place in the number in order to find the smallest number you can get.

#Task: Return an array or a tuple or a string depending on the language (see "Sample Tests") with

1) the smallest number you got
2) the index i of the digit d you took, i as small as possible
3) the index j (as small as possible) where you insert this digit d to have the smallest number.
Example:

smallest(261235) --> [126235, 2, 0] or (126235, 2, 0) or "126235, 2, 0"
"""
from typing import List


def smallest(number: int) -> List[int]:
    """Finds smallest number.

    Examples:
        >>> assert smallest(261235) == [126235, 2, 0]
        >>> assert smallest(209917) == [29917, 0, 1]
        >>> assert smallest(285365) == [238565, 3, 1]
        >>> assert smallest(269045) == [26945, 3, 0]
    """
    numbers: List[int] = list(map(int, str(number)))
    min_: int = min(numbers[1:])
    current_index: int = numbers.index(min_)
    numbers.pop(current_index)
    if min_ < numbers[0]:
        numbers.insert(0, min_)
    else:
        numbers.insert(1, min_)

    min_index: int = numbers.index(min_)
    if current_index in numbers:
        if current_index < numbers.index(current_index):
            current_index, min_index = min_index, current_index
    return [int("".join(map(str, numbers))), current_index, min_index]


if __name__ == "__main__":
    print(smallest(261235))
    print(smallest(209917))
