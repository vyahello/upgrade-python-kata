"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
"""


def solution(string: str, ending: str) -> bool:
    """Checks if given string ends with specific string.

    Examples:
        >>> assert solution("abcb", "cb")
        >>> assert not solution("abcb", "d")
    """
    return string.endswith(ending)


if __name__ == "__main__":
    print(solution("abcb", "cb"))
