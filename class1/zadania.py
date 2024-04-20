from typing import Optional

SQUARE_ROOT_OF_2: float = 1.41421356237


def art(a, b, operation: str) -> float | str:
    if operation == "+":
        return a + b
    elif operation== "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        # No specification for DivisionByZeroError so
        # nothing gets caught
        return a/b
    return "Nieznana operacja"


def kwadrat(bok) -> tuple[float, float, float]:
    return (4*bok, bok*bok, bok*SQUARE_ROOT_OF_2)

def pora_roku(miesiac: int) -> Optional[str]:
    if miesiac in (12, 1, 2, 3):
        return "zima"
    elif miesiac in (4, 5, 6):
        return "wiosna"
    elif miesiac in (7, 8, 9):
        return "lato"
    elif miesiac in (10, 11):
        return "jesien"
    return None # Out of range, but no bad input return spec given


