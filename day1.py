"""CS 1001 - Lab Programming 8: Raising and Handling Exceptions.

Friday, November 20, 2026 - ONE 50-minute lab.
Implement only the THREE TODO functions below. Do not rename them.

Run tests:  python -m unittest test_1.py
Run demo:   python day1.py

NO file reading, parsing pairs, or extra Python modules are required.
"""


def parse_price(text: str) -> float:
    """Return a nonnegative price as a float.

    Convert with float(text). Non-numeric input should naturally raise
    ValueError. If the converted price is negative, MANUALLY raise
    ValueError("Price cannot be negative"). Do NOT return None.
    """
    # TODO 1: convert, validate, and raise ValueError for negative prices.
    raise NotImplementedError


def split_bill(total_text: str, people_text: str) -> float:
    """Return the amount owed by each person.

    Reuse parse_price(total_text), then convert people_text with int().
    If count is negative: raise ValueError("People must be positive").
    If count is zero: raise ZeroDivisionError(
        "Cannot split among zero people").
    Otherwise, return the total divided by the count.

    Do NOT catch the exceptions here; allow them to reach the caller.
    """
    # TODO 2: reuse Task 1, validate count, raise on errors, divide.
    raise NotImplementedError


def bill_message(total_text: str, people_text: str) -> str:
    """Return a readable message instead of allowing exceptions to escape.

    Call split_bill() inside a try block.
    - On ValueError as exc, return "Invalid input: " + str(exc).
    - On ZeroDivisionError as exc, return "Cannot split bill: " + str(exc).
    - On success, return "Each person pays $X.XX" (two decimals).

    Use TWO specific except clauses (and 'as exc'). Do NOT use
    'except:' or a generic 'except Exception:' in this function.
    """
    # TODO 3: try / except ValueError / except ZeroDivisionError.
    raise NotImplementedError


def main() -> None:
    """Provided demonstration driver - do not change."""
    examples = [
        ("18.00", "3"),
        ("-5", "2"),
        ("12", "0"),
    ]
    for total, people in examples:
        print(bill_message(total, people))


if __name__ == "__main__":
    main()
