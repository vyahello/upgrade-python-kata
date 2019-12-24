"""
Your task it to swap keys and values of a dictionary

-----------------------------------
For doctests run following command:
python -m xdoctest -v reversed_dict.py
or
python3 -m xdoctest -v reversed_dict.py

For manual testing run:
python reversed_dict.py
"""
from typing import Dict, Any


def swap_dict_keys_to_values(dictionary: Dict[Any, Any]) -> Dict[Any, Any]:
    """Swaps key and values in a dictionary

    Args:
        dictionary: a dictionary object e.g {"a": 1, "b": 2}
    
    Examples:
        >>> assert swap_dict_keys_to_values({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    """
    for swapped_key in dictionary.values():  # type: Any
        if isinstance(swapped_key, (list, dict, bytearray)):
            raise TypeError(f"Dict key '{swapped_key}' should not be mutable object!")
    return {value: key for key, value in dictionary.items()}


if __name__ == "__main__":
    print(swap_dict_keys_to_values({"a": 1, "b": 2}))  # -> {1: "a", 2: "b"}
    print(swap_dict_keys_to_values({"a": 1, "b": 2, "v": [1, 2]}))  # -> raise TypeError
