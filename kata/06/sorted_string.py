"""
You will receive a string consisting of lowercase letters, uppercase letters and digits as input.
Your task is to return this string as blocks separated by dashes ("-").
The elements of a block should be sorted with respect to the hierarchy listed below,
and each block cannot contain multiple instances of the same character.

The hierarchy is:

lowercase letters (a - z), in alphabetic order
uppercase letters (A - Z), in alphabetic order
digits (0 - 9), in ascending order
Examples
"21AxBz" -> "xzAB12" - since input does not contain repeating characters, you only need 1 block
"abacad" -> "abcd-a-a" - character "a" repeats 3 times, thus 3 blocks are needed
"" -> "" - an empty input should result in an empty output

-----------------------------------
For doctests run following command:
python -m xdoctest -v sort_array.py
or
python3 -m xdoctest -v sort_array.py

For manual testing run:
python sort_array.py
"""


def sorted_string(string: str) -> str:
    """Returns string as sorted block.

    Examples:
        >>> assert sorted_string("21AxBz") == "xzAB12"
        >>> assert sorted_string("abacad") == "abcd-a-a"
        >>> assert sorted_string("") == ""
    """
    blocks = [f"-{item}" for item in string if list(string).count(item) > 1]
    sorted_array = sorted(sorted(set(string), key=str.swapcase), key=str.isdigit)
    if blocks:
        sorted_array.extend(blocks[1:])
    return "".join(sorted_array)


if __name__ == "__main__":
    print(sorted_string("21AxBz"))
