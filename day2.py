"""CS 1001 - Lab Programming 7, Day 2 (Wednesday, November 18, 2026).

File input and output. Complete these four functions and test_2.py.
Unlike Day 1, this file READS and WRITES ordinary text files.

Assumptions for this lab: all requested input files exist, each nonempty
input line contains exactly two valid numbers, and paths are writable.
Error handling for invalid files/input is outside the scope of this lab.

Run: python -m unittest test_2.py
"""

from day1 import sum_pair


def count_lines(filename: str) -> int:
    """Return the number of lines in a text file.

    An empty file contains 0 lines. Use open(..., 'r') and a with-block.
    Example: three newline-terminated lines -> 3.
    """
    # TODO (Day 2, Task 5): Read the file and count its lines.
    raise NotImplementedError


def sum_pairs(filename: str) -> list[float]:
    """Read lines each containing two floats; return their sums in order.

    Example file contents: '3.0 4.0\n1.5 2.5\n'
    Expected result: [7.0, 4.0]. An empty file returns [].
    Reuse day1.sum_pair(line) for each line.
    """
    # TODO (Day 2, Task 6): Open/read lines; reuse sum_pair.
    raise NotImplementedError


def write_numbers(filename: str, values: list[float]) -> None:
    """Overwrite/create a file, writing one float per line.

    Example: [4.5, 2.0] creates a file with '4.5\n2.0\n'.
    An empty list creates an empty file. Return None.
    Use open(..., 'w'), str(value), and '\n'.
    """
    # TODO (Day 2, Task 7): Open in write mode, then write each value.
    raise NotImplementedError


def sum_file(input_filename: str, output_filename: str) -> None:
    """Read number pairs and write one sum per line to an output file.

    Example input:  '3.0 4.0\n1.5 2.5\n'
    Example output: '7.0\n4.0\n'
    Return None. Reuse sum_pairs() and write_numbers(); do not duplicate.
    """
    # TODO (Day 2, Task 8): Compose your existing functions.
    raise NotImplementedError
