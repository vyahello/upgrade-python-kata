"""
Write a function insertDash(num)/InsertDash(int num) that will insert dashes ('-') between each two odd numbers in num
For example: if num is 454793 the output should be 4547-9-3. Don't count zero as an odd number.

Note that the number will always be non-negative (>= 0).
"""
from re import sub


def insert_dash_between_odds_common(number: int) -> int:
    "Inserts dash between two odd numbers."
    index: int = 0
    result: str = str()
    while index != len(str(number)):
        result += str(number)[index]
        if not index + 1 >= len(str(number)):
            if int(str(number)[index]) % 2 and int(str(number)[index + 1]) % 2:
                result += "-"
        index += 1
    return result


def insert_dash_between_odds_pythonic(number: int) -> str:
    """Inserts dash between two odd numbers.

    Uses pythonic approach.
    """
    return sub(r"([13579])(?=13579)", r"\1-", str(number))



if __name__ == "__main__":
    print(insert_dash_between_odds_common(113345566))  # -> "1-1-3-345-566"
    print(insert_dash_between_odds_common(113345566))  # -> "1-1-3-345-566"

