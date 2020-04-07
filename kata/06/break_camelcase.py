"""
Complete the solution so that the function will break up camel casing, using a space between words.
"""
import re


def break_camelcase(string: str) -> str:
    """Breaks camelcase string.

    Args:
        string (str): as string

    Examples:
        >>> assert break_camelcase("helloWorld") == "hello World"
    """
    return "".join(map(lambda item: f" {item}" if item.isupper() else item, string))


def break_camelcase_re(string: str) -> str:
    """Breaks camelcase string (regex).

    Args:
        string (str): as string

    Examples:
        >>> assert break_camelcase_re("helloWorld") == "hello World"
    """
    return re.sub(pattern="([A-Z])", repl=r" \1", string=string)


def break_camelcase_pythonic(string: str) -> str:
    """Breaks camelcase string (pythonic).

    Args:
        string (str): as string

    Examples:
        >>> assert break_camelcase_pythonic("helloWorld") == "hello World"
    """
    return "".join(f" {item}" if item.isupper() else item for item in string)


if __name__ == "__main__":
    print(break_camelcase("helloWorld"))
    print(break_camelcase_re("helloWorld"))
    print(break_camelcase_pythonic("helloWorld"))
