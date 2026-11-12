"""CS 1001 - Lab Programming 7: Day 2 starter unit tests.

Each task initially fails with NotImplementedError until implemented.
Add MULTIPLE more unittest methods for each required function.
The provided tests use temporary files to avoid changing repository files.
Use self.assertEqual(...), not bare assert.

Run: python -m unittest test_2.py
Run both days: python -m unittest test_1.py test_2.py
"""

import tempfile
import unittest
from pathlib import Path

from day2 import count_lines, sum_pairs, write_numbers, sum_file


class TempFilesTestCase(unittest.TestCase):
    """Small helper that creates a fresh temporary directory for each test."""

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.folder = Path(temporary.name)

    def create_file(self, name: str, contents: str) -> str:
        path = self.folder / name
        path.write_text(contents, encoding="utf-8")
        return str(path)


class TestCountLines(TempFilesTestCase):
    def test_three_lines(self):
        filename = self.create_file("lines.txt", "apple\nbanana\npear\n")
        self.assertEqual(3, count_lines(filename))

    def test_empty_file(self):
        filename = self.create_file("empty.txt", "")
        self.assertEqual(0, count_lines(filename))

    # TODO: Add a one-line test and a line with no trailing newline.


class TestSumPairs(TempFilesTestCase):
    def test_multiple_pairs(self):
        filename = self.create_file("pairs.txt", "3.0 4.0\n1.5 2.5\n-2.0 7.0\n")
        self.assertEqual([7.0, 4.0, 5.0], sum_pairs(filename))

    def test_empty_file(self):
        filename = self.create_file("empty.txt", "")
        self.assertEqual([], sum_pairs(filename))

    # TODO: Add a one-line and zero-sum or negative-number test.


class TestWriteNumbers(TempFilesTestCase):
    def test_several_values(self):
        filename = str(self.folder / "out.txt")
        result = write_numbers(filename, [4.5, 2.0, -3.0])
        self.assertEqual("4.5\n2.0\n-3.0\n", Path(filename).read_text(encoding="utf-8"))
        self.assertEqual(None, result)

    def test_empty_list(self):
        filename = self.create_file("existing.txt", "OLD CONTENT\n")
        write_numbers(filename, [])
        self.assertEqual("", Path(filename).read_text(encoding="utf-8"))

    # TODO: Add one value, zero, and overwrite-existing-file tests.


class TestSumFile(TempFilesTestCase):
    def test_multiple_pairs(self):
        source = self.create_file("input.txt", "3.0 4.0\n1.5 2.5\n-2.0 7.0\n")
        destination = str(self.folder / "totals.txt")
        result = sum_file(source, destination)
        self.assertEqual("7.0\n4.0\n5.0\n", Path(destination).read_text(encoding="utf-8"))
        self.assertEqual(None, result)

    def test_empty_input_file(self):
        source = self.create_file("empty.txt", "")
        destination = str(self.folder / "totals.txt")
        sum_file(source, destination)
        self.assertEqual("", Path(destination).read_text(encoding="utf-8"))

    # TODO: Add a one-line input and a zero-sum input test.


if __name__ == "__main__":
    unittest.main()
