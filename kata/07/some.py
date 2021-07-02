"""
Your task is to create a function that given a sequence and a predicate,
returns True if only some (but not all) elements in the sequence are True
after applying the predicate
"""
from typing import Callable


def some_basic(string: str, function: Callable) -> bool:
    """Check if some elements in a string match the function (basic).

    Args:
        string: <str> string to verify.
        function: <callable> function to call.

    Returns:
        True if some of elements are in the sequence are True.

    Examples:
        >>> assert some_basic('abcdefg&%$', str.isalpha)
        >>> assert not some_basic('&%$=', str.isalpha)
    """
    match: int = 0
    for next_string in string:  # type: str
        if function(next_string):
            match += 1
    return len(string) > match > 0


def some_func(string: str, function: Callable) -> bool:
    """Check if some elements in a string match the function (functional).

    Args:
        string: <str> string to verify.
        function: <callable> function to call.

    Returns:
        True if some of elements are in the sequence are True.

    Examples:
        >>> assert some_func('abcdefg&%$', str.isalpha)
        >>> assert not some_func('&%$=', str.isalpha)
    """
    return any(map(function, string)) and not all(map(function, string))


if __name__ == '__main__':
    print(some_basic('abcdefg', str.isalpha))
    print(some_func('abcdefg', str.isalpha))
