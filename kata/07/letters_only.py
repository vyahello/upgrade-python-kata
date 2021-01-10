"""
Let's assume we need "clean" strings.
Clean means a string should only contain letters a-z, A-Z and spaces.
We assume that there are no double spaces or line breaks.

Write a function that takes a string and returns a string without the unnecessary characters.
"""
import re


def remove_chars(string: str) -> str:
    """Remove all characters but strings.

    Args:
        string: <str> input string sequence.

    Returns:
        string: <str> sorted only letters string.

    Examples:
        >>> assert remove_chars('.tree1') == 'tree'
    """

    return ''.join(
        filter(lambda letter: letter.isalpha() or letter.isspace(), string)
    )


def remove_chars_re(string: str) -> str:
    """Remove all charactes but strings (with regex support).

    Args:
        string: <str> input string.

    Returns:
        string: <str> sorted only letters.

    Examples:
        >>> assert remove_chars_re('.tree1') == 'tree'
    """

    return re.sub(pattern='[^a-zA-Z ]', repl='', string=string)


remove_chars_lambda = lambda string: ''.join(
    filter(lambda letter: letter.isalpha() or letter.isspace(), string)
)


if __name__ == '__main__':
    print(remove_chars('.tree1'))
    print(remove_chars_re('.tree1'))
    print(remove_chars_lambda('.tree1'))
