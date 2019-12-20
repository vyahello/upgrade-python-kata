"""
3 friends go out together: A spends £20, B spends £15, and C spends £10.
The function should return an object/dict showing that A should receive £5, B should receive £0, and C should pay £5.

-----------------------------------
For doctests run following command:
python -m xdoctest -v split_the_bill.py
or
python3 -m xdoctest -v split_the_bill.py

For manual testing run:
python split_the_bill.py
"""
from typing import Dict


def split_the_bill(group: Dict[str, float]) -> Dict[str, float]:
    """Splits the bill between members.

    Examples:
        >>> assert split_the_bill({"A": 20, "B": 15, "C": 10}) == {'A': 5, 'B': 0, 'C': -5}
        >>>
        >>> assert split_the_bill(
        >>>      {'A': -17.200000000000003, 'B': -32.2, 'C': -47.2, 'D': 95.8, 'E': 0.7999999999999972}
        >>> ) == {'A': -17.2, 'B': -32.2, 'C': -47.2, 'D': 95.8, 'E': 0.8}
        >>>
    """
    average: float = sum(group.values()) / len(group)
    return {member: round(pounds - average, 2) for member, pounds in group.items()}


if __name__ == "__main__":
    print(split_the_bill({"A": 20, "B": 15, "C": 10}))  # -> {'A': 5, 'B': 0, 'C': -5}
    print(split_the_bill({"A": -17.200000000000003, "B": -32.2, "C": -47.2, "D": 95.8, "E": 0.7999999999999972}))
