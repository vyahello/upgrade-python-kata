"""
Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses

# balanced_parens(0) => [""]
# balanced_parens(1) => ["()"]
# balanced_parens(2) => ["()()","(())"]
# balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
"""
from itertools import permutations as options
from typing import List


def only_balanced(count: int) -> list:
    """

    Examples:
        >>> assert only_balanced(0) == [""]
        >>> assert only_balanced(1) == ["()"]
    """
    balanced = list()
    for item in set("".join(option) for option in iter(options(count * "()"))):  # type: str
        counter: int = 0
        for inner in item:
            if inner == "(":
                counter += 1
            elif inner == ")":
                counter -= 1
            if counter < 0:
                break
        if counter == 0:
            balanced.append(item)
    return balanced


def only_balanced_pythonic(number: int) -> List:
    """Most efficient way

    Examples:
        >>> assert only_balanced_pythonic(0) == [""]
        >>> assert only_balanced_pythonic(1) == ["()"]
    """
    if number == 0:
        return [""]
    balanced = []
    for next_number in range(number):  # type: int
        for left in only_balanced_pythonic(next_number):
            for right in only_balanced_pythonic(number - 1 - next_number):
                balanced.append(f"({left}){right}")
    return balanced


if __name__ == "__main__":
    print(only_balanced(3))
    print(only_balanced_pythonic(3))
