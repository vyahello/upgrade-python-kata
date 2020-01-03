"""
remove(text, what)

that takes in a string str(text in Python) and an object/hash/dict/Dictionary what and returns a string with the chars
removed in what. For example:

remove('this is a string',{'t':1, 'i':2}) == 'hs s a string'
# remove from 'this is a string' the first 1 't' and the first 2 i's.
remove('hello world',{'x':5, 'i':2}) == 'hello world'
# there are no x's or i's, so nothing gets removed
remove('apples and bananas',{'a':50, 'n':1}) == 'pples d bnns'
# we don't have 50 a's, so just remove it till we hit end of string.

-----------------------------------
For doctests run following command:
python -m xdoctest -v remove.py
or
python3 -m xdoctest -v remove.py

For manual testing run:
python remove.py
"""
from typing import Dict
import re


def remove_regex(text: str, what: Dict[str, int]) -> str:
    """Removes values in a dictionary from given text (with regex)

    Examples:
        >>> assert remove_regex("this is a string", {"t": 1, "i": 2}) == "hs s a string"
        >>> assert remove_regex("hello world", {"x": 1, "i": 2}) == "hello world"
    """
    for char, count in what.items():  # type: str, int
        text = re.sub(char, "", text, count=count)
    return text


def remove_pythonic(text: str, what: Dict[str, int]) -> str:
    """Removes values in a dictionary from given text (pythonic)

    Examples:
        >>> assert remove_pythonic("this is a string", {"t": 1, "i": 2}) == "hs s a string"
        >>> assert remove_pythonic("hello world", {"x": 1, "i": 2}) == "hello world"
    """
    for char in what:  # type: str
        text = text.replace(char, "", what[char])
    return text


if __name__ == "__main__":
    print(remove_regex("this is a string", {"t": 1, "i": 2}))
    print(remove_regex("hello world", {"x": 1, "i": 2}))

    print(remove_pythonic("this is a string", {"t": 1, "i": 2}))
    print(remove_pythonic("hello world", {"x": 1, "i": 2}))
