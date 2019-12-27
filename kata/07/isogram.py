"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case

-----------------------------------
For doctests run following command:
python -m xdoctest -v is_isogram.py
or
python3 -m xdoctest -v is_isogram.py

For manual testing run:
python is_isogram.py
"""


def is_isogram(string: str) -> bool:
    """Checks if string is isogram.

    Args:
        string: given string value

    Examples:
        >>> assert is_isogram("Dermatoglyphics")
        >>> assert not is_isogram("aba")
    """
    return len(string) == len(set(string.lower()))


if __name__ == "__main__":
    print(is_isogram("Dermatoglyphics"))
    print(is_isogram("aba"))
