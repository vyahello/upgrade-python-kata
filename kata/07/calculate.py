"""
For doctests run following command:
python -m xdoctest -v calculate.py
or
python3 -m xdoctest -v calculate.py

For manual testing run:
python calculate.py
"""


def calculate(string: str) -> str:
    """Calculates value from a string.

    Examples:
        >>> assert calculate("1plus1") == "2"
    """
    return str(eval(string.replace("plus", "+").replace("minus", "-")))


if __name__ == "__main__":
    print(calculate("1plus1"))
