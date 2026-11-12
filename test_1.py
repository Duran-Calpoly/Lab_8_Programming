"""CS 1001 - Lab Programming 7: Day 1 starter unit tests.

Required functions start with NotImplementedError: initial failures are expected.
For EACH task, add multiple NEW test cases beyond these examples.
Use self.assertEqual(...), not bare assert. Test typical and boundary cases.

Run: python -m unittest test_1.py
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from day1 import parse_pair, sum_pair, keyboard_sum, command_line_sum


class TestParsePair(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual((3.0, 4.0), parse_pair("3.0 4.0"))

    def test_whitespace_negative_decimal(self):
        self.assertEqual((-2.5, 7.0), parse_pair("  -2.5   7  "))

    # TODO: Add tests for zero, negative values, and decimals.


class TestSumPair(unittest.TestCase):
    def test_integer_looking_inputs(self):
        self.assertEqual(7.0, sum_pair("3 4"))

    def test_negative_numbers(self):
        self.assertEqual(-1.5, sum_pair("-2 0.5"))

    # TODO: Add zero-sum, extra-whitespace, and decimal tests.


class TestKeyboardSum(unittest.TestCase):
    def test_reads_and_prints(self):
        output = io.StringIO()
        with patch("builtins.input", return_value="3 4"):
            with redirect_stdout(output):
                result = keyboard_sum()
        self.assertEqual("Sum: 7.0\n", output.getvalue())
        self.assertEqual(None, result)

    def test_negative_input(self):
        output = io.StringIO()
        with patch("builtins.input", return_value="-2 0.5"):
            with redirect_stdout(output):
                keyboard_sum()
        self.assertEqual("Sum: -1.5\n", output.getvalue())

    # TODO: Add decimal and zero tests; no live keyboard input in tests.


class TestCommandLineSum(unittest.TestCase):
    def test_two_argument_strings(self):
        output = io.StringIO()
        with redirect_stdout(output):
            result = command_line_sum(["1.5", "2.5"])
        self.assertEqual("Sum: 4.0\n", output.getvalue())
        self.assertEqual(None, result)

    def test_negative_argument(self):
        output = io.StringIO()
        with redirect_stdout(output):
            command_line_sum(["-3", "1"])
        self.assertEqual("Sum: -2.0\n", output.getvalue())

    # TODO: Add tests for zero and whitespace-free numeric arguments.


if __name__ == "__main__":
    unittest.main()
