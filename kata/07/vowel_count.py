"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


def get_count(input_str: str) -> int:
    """Count vowel from input string.

    Args:
        input_str: <str> inout string.

    Returns: <int> total amount of vowels.

    Examples:
        >>> assert get_count('abracadabra') == 5

    """
    return sum(map(lambda letter: letter in 'aeiou', input_str))


def get_count_opt(input_str: str) -> int:
    """Count vowel from input string (efficient).

    Args:
        input_str: <str> inout string.

    Returns: <int> total amount of vowels.

    Examples:
        >>> assert get_count_opt('abracadabra') == 5

    """
    return sum(letter in 'aeiou' for letter in input_str)


if __name__ == '__main__':
    print(get_count('abracadabra'))
    print(get_count_opt('abracadabra'))
