"""
You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"

"""


def get_middle(string: str) -> str:
    """Get middle value of a string.

    Examples:
        >>> assert get_middle('middle') == 'dd'
    """
    if len(string) > 2:
        index: int = int(len(string) / 2)
        if len(string) % 2:
            return string[index]
        return f'{string[index-1]}{string[index]}'
    return string


def get_middle_opt(string: str) -> str:
    """Get middle value of a string (efficient).

    Examples:
        >>> assert get_middle_opt('middle') == 'dd'
    """
    return (
        string[int(len(string) // 2) - 1 : int(len(string) // 2) + 1]
        if not len(string) % 2
        else string[int(len(string) // 2)]
    )


if __name__ == '__main__':
    print(get_middle('middle'))
    print(get_middle_opt('middle'))
