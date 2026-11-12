"""CS 1001 - Lab Programming 7, Day 1 (Monday, November 16, 2026).

Input, output, and string processing. NO FILE I/O ON DAY 1.

Complete the four TODO functions below without changing their signatures.
Add your own tests to test_1.py. Assume the supplied strings are valid:
- parse_pair and sum_pair receive exactly two whitespace-separated numbers.
- command_line_sum receives exactly two numeric argument strings.

Run: python -m unittest test_1.py

Manual demos AFTER implementation:
    python day1.py               # prompts with input()
    python day1.py 3.0 4.0       # uses command-line arguments
"""


def parse_pair(text: str) -> tuple[float, float]:
    """Convert two whitespace-separated numbers in text into floats.

    Examples:
        parse_pair("3.0 4.0") -> (3.0, 4.0)
        parse_pair("  -2.5   7 ") -> (-2.5, 7.0)

    Use str.split() and float(). Do not use input() or files here.
    """
    # TODO (Day 1, Task 1): Parse both values and return a tuple.
    raise NotImplementedError


def sum_pair(text: str) -> float:
    """Return the sum of a pair of numbers encoded in one string.

    Example: sum_pair("3 4") -> 7.0
    Reuse parse_pair rather than duplicating its parsing logic.
    """
    # TODO (Day 1, Task 2): Call parse_pair and compute the sum.
    raise NotImplementedError


def keyboard_sum() -> None:
    """Prompt once using input(), then print the sum on one line.

    Prompt exactly: Enter two numbers: 
    Output exactly: Sum: <result>
    Example: with input "3 4", print "Sum: 7.0".
    Return None. Reuse sum_pair.
    """
    # TODO (Day 1, Task 3): Read from keyboard; print formatted result.
    raise NotImplementedError


def command_line_sum(args: list[str]) -> None:
    """Print the sum of two command-line argument strings.

    args holds the values after the program name (sys.argv[1:]).
    Assume it contains exactly two valid numbers.
    Example: command_line_sum(["1.5", "2.5"]) prints "Sum: 4.0".
    Return None. Reuse sum_pair or parse_pair.
    """
    # TODO (Day 1, Task 4): Convert args and print formatted result.
    raise NotImplementedError


if __name__ == "__main__":
    # Provided driver. Tests import this module without running the driver.
    import sys

    if len(sys.argv) > 1:
        command_line_sum(sys.argv[1:])
    else:
        keyboard_sum()
