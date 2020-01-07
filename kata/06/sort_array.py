"""
Sort the given strings in alphabetical order, case insensitive. For example:

["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]

-----------------------------------
For doctests run following command:
python -m xdoctest -v sort_array.py
or
python3 -m xdoctest -v sort_array.py

For manual testing run:
python sort_array.py
"""
from typing import List


def sort_array(words: List[str]) -> List[str]:
    """Sort array words ignoring case.

    Examples:
        >>> assert sort_array(["C", "d", "a", "B"]) == ["a", "B", "C", "d"]
        >>> assert sort_array(["Hello", "there", "I'm", "fine"]) == ["fine", "Hello", "I'm", "there"]
        >>> assert sort_array(["CodeWars"]) == ["CodeWars"]
    """
    return sorted(words, key=str.casefold)


if __name__ == "__main__":
    print(sort_array(["C", "d", "a", "B"]))
