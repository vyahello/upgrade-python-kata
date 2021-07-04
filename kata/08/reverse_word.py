"""
Complete the solution so that it reverses all of the words within
the string passed in.

Example:
"The greatest victory is that which requires no battle" -->
"battle no requires which that is victory greatest The"
"""


def reverse_words(string: str) -> str:
    """Sort words in reverse order.

    Examples:
        >>> assert reverse_words('hello world!') == 'world! hello'
    """
    return ' '.join(string.split()[::-1])


if __name__ == '__main__':
    print(reverse_words('hello world!'))
