"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.
"""
from typing import List


def count_sequence(lines: List[str], start_from: int = 1) -> List[str]:
    """Returns line prepended by the correct number.

    Args:
        lines: a list of lines combined in a list
        start_from: counter value to start from

    Examples:
        >>> assert not count_sequence([])
        >>> assert count_sequence(["a", "b", "c"]) == ["1: a", "2: b", "3: c"]
    """
    return [
        f"{index}: {value}" for index, value in enumerate(lines, start_from)
    ]


if __name__ == "__main__":
    print(count_sequence(["a", "b", "c"]))
