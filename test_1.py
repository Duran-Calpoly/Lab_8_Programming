"""Lab 8 - starter unittest tests for exception behavior.

Run: python -m unittest test_1.py

Initially these tests fail with NotImplementedError; that is EXPECTED.
Add ONE more test to EACH class (three new tests total):
  1. Test nonnumeric parse_price with CALLABLE assertRaises form.
  2. Test negative people with CONTEXT MANAGER assertRaises form.
  3. Test bill_message on a nonnumeric people count.
"""

import unittest
from day1 import parse_price, split_bill, bill_message


class TestParsePrice(unittest.TestCase):
    def test_normal_price(self):
        self.assertEqual(12.5, parse_price("12.50"))

    def test_zero_is_valid(self):
        self.assertEqual(0.0, parse_price("0"))

    def test_negative_price_raises_with_context_form(self):
        # assertRaises syntax 1: context-manager form.
        with self.assertRaises(ValueError):
            parse_price("-2.00")

    # TODO TEST 1: nonnumeric price (e.g. "hello") must raise ValueError.
    # Use the other syntax: self.assertRaises(ValueError, parse_price, "hello")


class TestSplitBill(unittest.TestCase):
    def test_three_people(self):
        self.assertAlmostEqual(6.0, split_bill("18", "3"))

    def test_zero_people_raises_callable_form(self):
        # assertRaises syntax 2: callable form (NO parentheses on split_bill).
        self.assertRaises(ZeroDivisionError, split_bill, "12", "0")

    # TODO TEST 2: negative people (e.g. "-2") raises ValueError.
    # Use: with self.assertRaises(ValueError): ...


class TestBillMessage(unittest.TestCase):
    def test_success(self):
        self.assertEqual("Each person pays $6.00", bill_message("18", "3"))

    def test_negative_price_becomes_message(self):
        self.assertEqual(
            "Invalid input: Price cannot be negative",
            bill_message("-2", "2"),
        )

    def test_zero_people_becomes_message(self):
        self.assertEqual(
            "Cannot split bill: Cannot split among zero people",
            bill_message("12", "0"),
        )

    # TODO TEST 3: "abc" people count should return a string starting
    # with "Invalid input: ", not raise an uncaught ValueError.


if __name__ == "__main__":
    unittest.main()
