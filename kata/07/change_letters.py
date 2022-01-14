"""
When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"

Note: Y is not a vowel in this kata.
"""


def swap_basic(value: str) -> str:
    """Capitalize all vowels in a string (basic).

    Args:
        value: <str> input string value.

    Returns: <str> swapped string.

    Examples:
        >>> assert swap_basic('HelloWorld') == 'HEllOWOrld'

    """
    new_val = ''
    for next_val in value:  # type: str
        if next_val in 'aeiou':
            next_val = next_val.upper()
        new_val += next_val
    return new_val


def swap_eff(value: str) -> str:
    """Capitalize all vowels in a string (efficient).

    Args:
        value: <str> input string value.

    Returns: <str> swapped string.

    Examples:
        >>> assert swap_eff('HelloWorld') == 'HEllOWOrld'

    """
    return ''.join(val.upper() if val in 'aeiou' else val for val in value)


if __name__ == '__main__':
    print(swap_basic('HelloWorld'))
    print(swap_eff('HelloWorld'))
