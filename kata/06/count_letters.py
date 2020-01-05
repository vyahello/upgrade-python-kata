"""
In this kata, you've to count lowercase letters in a given string and return the letter count in a hash with 'letter'
as key and count as 'value'. The key must be 'symbol' instead of string in Ruby and 'char' instead of string in Crystal.
"""
from typing import Dict
from collections import Counter


def letter_count(letter: str) -> Dict[str, int]:
    """Counts letters in a string.

    Examples:
        >>> assert letter_count("codewars") == {"a": 1, "c": 1, "d": 1, "e": 1, "o": 1, "r": 1, "s": 1, "w": 1}
    """
    count: Dict[str, int] = dict()
    for item in letter:  # type: str
        if item not in count:
            count[item] = 0
        count[item] += 1
    return count


def letter_count_collection(letter: str) -> Dict[str, int]:
    """Counts letters in a string (collection approach).

    Examples:
        >>> assert letter_count_collection("codewars")
        >>> {"a": 1, "c": 1, "d": 1, "e": 1, "o": 1, "r": 1, "s": 1, "w": 1}
    """
    return Counter(letter)


def letter_count_pythonic(letter: str) -> Dict[str, int]:
    """Counts letters in a string (pythonic approach).

    Examples:
        >>> assert letter_count_collection("codewars")
        >>> {"a": 1, "c": 1, "d": 1, "e": 1, "o": 1, "r": 1, "s": 1, "w": 1}
    """
    return {item: letter.count(item) for item in letter}


if __name__ == "__main__":
    print(letter_count("codewars"))
    print(letter_count_collection("codewars"))
    print(letter_count_pythonic("codewars"))
