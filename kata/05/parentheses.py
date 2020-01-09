"""
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""


def is_valid_parentheses(string: str) -> bool:
    """Checks if string has valid parentheses.
    Examples:
        >>> assert is_valid_parentheses("()")
        >>> assert not is_valid_parentheses(")test")
        >>> assert not is_valid_parentheses(")(")
    """
    count: int = 0
    for item in string:  # type: str
        if item == "(":
            count += 1
        elif item == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0


if __name__ == "__main__":
    print(is_valid_parentheses("()"))
    print(is_valid_parentheses(")("))
