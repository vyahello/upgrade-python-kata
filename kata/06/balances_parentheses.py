"""
Given an expression string, write a python program to find whether a given string has balanced parentheses or not.

Input : {[]{()}}
Output : Balanced

Input : [{}{}(]
Output : Unbalanced

-----------------------------------
For doctests run following command:
python -m xdoctest -v balances_parentheses.py
or
python3 -m xdoctest -v balances_parentheses.py

For manual testing run:
python balances_parentheses.py
"""
from typing import List, Sequence, Dict


def parentheses_status_stack(string: str) -> str:
    """Check is expression string has balanced parentheses (using stack method).

    One approach to check balanced parentheses is to use stack.
    Each time, when an open parentheses is encountered push it in the stack, and when closed parenthesis is encountered,
    match it with the top of stack and pop it.

    If stack is empty at the end, return Balanced otherwise, Unbalanced.

    Examples:
        >>> assert parentheses_status_stack("{[]{()}}") == "Balanced"
        >>> assert parentheses_status_stack("[{}{})(]") == "Unbalanced"
    """
    # match indexes
    opened: Sequence[str] = tuple("[{(")
    closed: Sequence[str] = tuple("]})")
    stack: List[str] = list()

    for item in string:  # type: str
        if item in opened:
            stack.append(item)
        elif item in closed:
            position: int = closed.index(item)
            if len(stack) and opened[position] == stack[len(stack) - 1]:
                stack.pop()
    if not len(stack):
        return "Balanced"
    return "Unbalanced"


def parentheses_status_queue(string: str) -> str:
    """Check is expression string has balanced parentheses (using stack queue).

    First Map opening parentheses to respective closing parentheses.
    Iterate through the given expression using ‘i’, if ‘i’ is an open parentheses,
    append in queue, if ‘i’ is close parentheses,
    Check whether queue is empty or ‘i’ is the top element of queue, if yes, return “Unbalanced”, otherwise “Balanced”.

    Examples:
        >>> assert parentheses_status_queue("{[]{()}}") == "Balanced"
        >>> assert parentheses_status_queue("[{}{})(]") == "Unbalanced"
    """
    opened: Sequence[str] = tuple("({[")
    closed: Sequence[str] = tuple(")}]")
    zipped: Dict[str, str] = dict(zip(opened, closed))
    queue: List[str] = list()

    for item in string:  # type: str
        if item in opened:
            queue.append(zipped[item])
        elif item in closed:
            if not queue or item != queue.pop():
                return "Unbalanced"
    return "Balanced"


def parentheses_status_eliminate(string: str) -> str:
    """Check is expression string has balanced parentheses (using stack elimination).

    In every iteration, the innermost brackets get eliminated (replaced with empty string).
    If we end up with an empty string, our initial one was balanced; otherwise, not.

    Examples:
        >>> assert parentheses_status_eliminate("{[]{()}}") == "Balanced"
        >>> assert parentheses_status_eliminate("[{}{})(]") == "Unbalanced"
    """
    brackets: List[str] = ["()", "{}", "[]"]
    while any(item in string for item in brackets):
        for bracket in brackets:
            string = string.replace(bracket, "")
    if not string:
        return "Balanced"
    return "Unbalanced"


def parentheses_status_eliminate_recursion(string: str) -> str:
    """Check is expression string has balanced parentheses (using stack elimination via resursion).

    In every iteration, the innermost brackets get eliminated (replaced with empty string).
    If we end up with an empty string, our initial one was balanced; otherwise, not.

    Examples:
        >>> assert parentheses_status_eliminate_recursion("{[]{()}}") == "Balanced"
        >>> assert parentheses_status_eliminate_recursion("[{}{})(]") == "Unbalanced"
    """
    brackets = '()', '[]', '{}'
    if any(br in string for br in brackets):
        for br in brackets:  # type: str
            string = string.replace(br, '')
        if not string:
            return 'Balanced'
        return parentheses_status_eliminate_recursion(string)
    return 'Unbalanced'


if __name__ == "__main__":
    print(parentheses_status_stack("{[]{()}}"))  # -> "Balanced"
    print(parentheses_status_stack("[{}{})(]"))  # -> "Unbalanced"

    print(parentheses_status_queue("{[]{()}}"))  # -> "Balanced"
    print(parentheses_status_queue("[{}{})(]"))  # -> "Unbalanced"

    print(parentheses_status_eliminate("{[]{()}}"))  # -> "Balanced"
    print(parentheses_status_eliminate("[{}{})(]"))  # -> "Unbalanced"

    print(parentheses_status_eliminate_recursion("{[]{()}}"))  # -> "Balanced"
    print(parentheses_status_eliminate_recursion("[{}{})(]"))  # -> "Unbalanced"
