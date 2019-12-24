"""
Your task it to swap keys and values of a dictionary.

# {"a": 1, "b": 2} -> {1: "a", 2: "b"}

-----------------------------------
For doctests run following command:
python -m xdoctest -v reversed_dict.py
or
python3 -m xdoctest -v reversed_dict.py

For manual testing run:
python reversed_dict.py
"""
from typing import Dict, Any

_AnyDict = Dict[Any, Any]


def swap_dict_keys_to_values_naive(dictionary: _AnyDict) -> _AnyDict:
    """Swaps key and values in a dictionary (naive)

    Args:
        dictionary: a dictionary object e.g {"a": 1, "b": 2}
    
    Examples:
        >>> assert swap_dict_keys_to_values_naive({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    """
    for swapped_key in dictionary.values():  # type: Any
        if isinstance(swapped_key, (list, dict, bytearray)):
            raise TypeError(f"Dict key '{swapped_key}' should not be mutable object!")
    return {value: key for key, value in dictionary.items()}


def swap_dict_keys_to_values_pythonic(dictionary: _AnyDict) -> _AnyDict:
    """Swaps key and values in a dictionary (pythonic)

    Args:
        dictionary: a dictionary object e.g {"a": 1, "b": 2}

    Examples:
        >>> assert swap_dict_keys_to_values_pythonic({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    """
    if any(filter(lambda swapped_key: isinstance(swapped_key, (list, dict, bytearray)), dictionary.values())):
        raise TypeError("Dict key should not be mutable object!")
    return {value: key for key, value in dictionary.items()}


def swap_dict_keys_to_values_object(dictionary: _AnyDict) -> _AnyDict:
    """Swaps key and values in a dictionary (OOP)

    Args:
        dictionary: a dictionary object e.g {"a": 1, "b": 2}

    Examples:
        >>> assert swap_dict_keys_to_values_object({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    """

    class SwappedDict(dict):
        """The class represents custom dictionary."""

        def __call__(self) -> _AnyDict:
            """Returns swapped dictionary.

            Examples:
                >>> assert SwappedDict({"a": 1, "b": 2})() == {1: "a", 2: "b"}
            """
            return {value: key for key, value in self.items()}

    if any(filter(lambda swapped_key: isinstance(swapped_key, (list, dict, bytearray)), dictionary.values())):
        raise TypeError("Dict key should not be mutable object!")
    return SwappedDict(dictionary)()


if __name__ == "__main__":
    print(swap_dict_keys_to_values_naive({"a": 1, "b": 2}))  # -> {1: "a", 2: "b"}
    print(swap_dict_keys_to_values_naive({"a": 1, "b": 2, "v": [1, 2]}))  # -> raise TypeError

    print(swap_dict_keys_to_values_pythonic({"a": 1, "b": 2}))  # -> {1: "a", 2: "b"}
    print(swap_dict_keys_to_values_pythonic({"a": 1, "b": 2, "v": [1, 2]}))  # -> raise TypeError

    print(swap_dict_keys_to_values_object({"a": 1, "b": 2}))  # -> {1: "a", 2: "b"}
    print(swap_dict_keys_to_values_object({"a": 1, "b": 2, "v": [1, 2]}))  # -> raise TypeError
