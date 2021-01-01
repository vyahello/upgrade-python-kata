"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans
at least 3 numbers. For example ("12, 13, 15-17")
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string
in the range format.
"""
from typing import List, Generator, Sequence


def extract_range(numbers: List[int]) -> Generator[Sequence[int], None, None]:
    """Extract range groups."""
    length: int = len(numbers)
    counter: int = 0
    while counter < length:
        low: int = numbers[counter]
        while (
            counter < length - 1
            and numbers[counter] + 1 == numbers[counter + 1]
        ):
            counter += 1
        high: int = numbers[counter]
        if high - low >= 2:
            yield low, high
        elif high - low == 1:
            yield low,
            yield high,
        else:
            yield low,
        counter += 1


def solution(numbers: List[int]) -> str:
    """Specify range of items.

    Examples:
        >>> assert solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]) == "-3--1,2,10,15,16,18-20"
    """
    return ",".join(
        f"{group[0]}-{group[1]}" if len(group) == 2 else f"{group[0]}"
        for group in extract_range(numbers)
    )


if __name__ == "__main__":
    print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
