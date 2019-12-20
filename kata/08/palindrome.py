"""
Palindrome could be any number, string or sequence.
It's main focus is that it is the same item if you read it backward e.g

"abccba" string is a palindrome

Your task is to write a function that will check if given string is palindrome

-----------------------------------
For doctests run following command:
python -m xdoctest -v palindrome.py
or
python3 -m xdoctest -v palindrome.py

For manual testing run:
python palindrome.py
"""


def is_palindrome(string: str) -> bool:
    """Checks is given string is palindrome.

    Examples:
        >>> assert is_palindrome("abccba")
        >>>
        >>> assert is_palindrome("123321")
        >>>
        >>> assert not is_palindrome("abccbX")
    """
    if not isinstance(string, str):
        raise TypeError("Input value should be string.")
    return string.lower() == string[::-1].lower()


if __name__ == "__main__":
    print(is_palindrome("abccba"))
    print(is_palindrome("123321"))
    print(is_palindrome("abccbX"))
