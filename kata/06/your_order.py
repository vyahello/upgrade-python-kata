"""
Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""

-----------------------------------
For doctests run following command:
python -m xdoctest -v your_order.py
or
python3 -m xdoctest -v your_order.py

For manual testing run:
python your_order.py
"""


def order(sentence: str) -> str:
    """Returns ordered sentence.

    Examples:
        >>> assert order("") == ""
        >>> assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
    """
    return " ".join(
        map(
            lambda item: item[1],
            sorted(
                map(
                    lambda word: (
                        [index for index in word if index.isdigit()][0],
                        word,
                    ),
                    sentence.split(),
                )
            ),
        )
    )


def order_pythonic(sentence: str) -> str:
    """Returns ordered sentence (pythonic).

    Examples:
        >>> assert order_pythonic("") == ""
        >>> assert order_pythonic("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
    """
    return " ".join(
        sorted(sentence.split(), key=lambda x: "".join(filter(str.isdigit, x)))
    )


def order_pythonic_min(sentence: str) -> str:
    """Returns ordered sentence (pythonic).

    Examples:
        >>> assert order_pythonic_min("") == ""
        >>> assert order_pythonic_min("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
    """
    return " ".join(sorted(sentence.split(), key=min))


if __name__ == "__main__":
    print(order("Thi1s is2 3a T4est"))
    print(order_pythonic("Thi1s is2 3a T4est"))
    print(order_pythonic_min("Thi1s is2 3a T4est"))
