"""
Task
Test whether or not the string contains all of the letters which spell a given name, in order.

The format
A function passing two strings, searching for one (the name) within the other. ``function nameInStr(str, name){ return true || false }``

nameInStr("Across the rivers", "chris") --> true
            ^      ^  ^^   ^
            c      h  ri   s

Contains all of the letters in "chris", in order.

nameInStr("Next to a lake", "chris") --> false

Contains none of the letters in "chris".
"""
import re


def name_in_string(string: str, name: str) -> bool:
    """Checks if string contains name.

    Args:
        string (str): input searchable string
        name (str): input name

    Examples:
        >>> assert name_in_string("Across the rivers", "chris")
        >>> assert not name_in_string("Next to a lake", "chris")
        >>> assert not name_in_string("A crew that boards the ship", "chris")
        >>> assert name_in_string("thomas", "Thomas")
    """
    return bool(re.compile(f'(?i){".*".join(name)}').search(string))


def name_in_string_pythonic(string: str, name: str) -> bool:
    """Checks if string contains name (pythonic).

    Args:
        string (str): input searchable string
        name (str): input name

    Examples:
        >>> assert name_in_string_pythonic("Across the rivers", "chris")
        >>> assert not name_in_string_pythonic("Next to a lake", "chris")
        >>> assert not name_in_string_pythonic("A crew that boards the ship", "chris")
        >>> assert name_in_string_pythonic("thomas", "Thomas")
    """
    iter_string: iter = iter(string.lower())
    return all(char in iter_string for char in name.lower())


if __name__ == "__main__":
    print(name_in_string("Across the rivers", "chris"))
    print(name_in_string_pythonic("Across the rivers", "chris"))
