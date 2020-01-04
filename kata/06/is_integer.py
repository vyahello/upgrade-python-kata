"""
Write a function with the signature shown below:

def is_int_array(arr):
    return True
returns true / True if every element in an array is an integer or a float with no decimals.
returns true / True if array is empty.
returns false / False for every other input.

-----------------------------------
For doctests run following command:
python -m xdoctest -v is_integer.py
or
python3 -m xdoctest -v is_integer.py

For manual testing run:
python is_integer.py
"""
from typing import List, Any


def is_int_array(array: List[Any]) -> bool:
    """Returns `True` is array contains integers or floats otherwise `False`.

    Examples:
        >>> assert not is_int_array("")
        >>> assert not is_int_array(None)
        >>> assert not is_int_array("-1")
        >>> assert not is_int_array([1, 2, None])
        >>> assert is_int_array([])
        >>> assert is_int_array([1, 2, 3, 4])
        >>> assert is_int_array([-11, -12, -13, -14])
        >>> assert is_int_array([1.0, 2.0, 3.0])
    """
    if array is None or isinstance(array, str):
        return False
    for item in array:
        if not isinstance(item, (int, float)):
            return False
        if isinstance(item, float):
            if not item.is_integer():  # e.g 3.001 is decimal
                return False
    return True


def is_int_array_pythonic(array: List[Any]) -> bool:
    """Returns `True` is array contains integers or floats otherwise `False` (pythonic).

    Examples:
        >>> assert not is_int_array_pythonic("")
        >>> assert not is_int_array_pythonic(None)
        >>> assert not is_int_array_pythonic("-1")
        >>> assert not is_int_array_pythonic([1, 2, None])
        >>> assert is_int_array_pythonic([])
        >>> assert is_int_array_pythonic([1, 2, 3, 4])
        >>> assert is_int_array_pythonic([-11, -12, -13, -14])
        >>> assert is_int_array_pythonic([1.0, 2.0, 3.0])
    """
    return isinstance(array, list) and all(isinstance(value, (int, float)) and value == int(value) for value in array)


if __name__ == "__main__":
    print(is_int_array([1, 2, None]))  # -> False
    print(is_int_array([1, 2, 3, 4]))  # -> True

    print(is_int_array_pythonic([1, 2, None]))  # -> False
    print(is_int_array_pythonic([1, 2, 3, 4]))  # -> True
