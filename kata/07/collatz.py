"""
The Collatz Conjecture states that for any natural number n, if n is even, divide it by 2.
If n is odd, multiply it by 3 and add 1. If you repeat the process continously for n, n will eventually reach 1.

For example, if n = 20, the resulting sequence will be:

[20, 10, 5, 16, 8, 4, 2, 1]

Write a program that will output the length of the Collatz Conjecture for any given n.
In the example above, the output would be 8

-----------------------------------
For doctests run following command:
python -m xdoctest -v collatz.py
or
python3 -m xdoctest -v collatz.py

For manual testing run:
python collatz.py
"""


def collatz_conjecture_length(number: int) -> int:
    """Returns length of collatz conjecture sequence.

    Examples:
        >>> assert collatz_conjecture_length(20) == 8
    """
    counter: int = 1
    while number > 1:
        counter += 1
        if not number % 2:
            number /= 2
        else:
            number = number * 3 + 1
    return counter


if __name__ == "__main__":
    print(collatz_conjecture_length(20))  # returns 8
