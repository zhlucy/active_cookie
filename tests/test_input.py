import unittest
from src.inputparser import InputParser
import os.path, sys, io

class TestInput(unittest.TestCase):
    """
    Tests for bad inputs.
    """
    def path(self, filename):
        return os.path.join("test_inputs", filename)

    def test_no_file(self):
        parser = InputParser("somefakefile", "2018-12-09")
        self.assertRaises(SystemExit, parser.readFile)

    def test_empty_file(self):
        parser = InputParser(self.path("empty.csv"), "2018-12-09")
        self.assertRaises(SystemExit, parser.readFile)

    def test_bad_column(self):
        parser = InputParser(self.path("bad_column.csv"), "2018-12-09")
        self.assertRaises(SystemExit, parser.readFile)

    def test_no_column(self):
        parser = InputParser(self.path("no_column.csv"), "2018-12-09")
        self.assertRaises(SystemExit, parser.readFile)

    def test_bad_timestamp(self):
        parser = InputParser(self.path("bad_timestamp.csv"), "2018-12-09")
        self.assertRaises(SystemExit, parser.readFile)

    def test_no_comma(self):
        parser = InputParser(self.path("no_comma.csv"), "2018-12-09")
        self.assertRaises(SystemExit, parser.readFile)

    def test_skip_line(self):
        parser = InputParser(self.path("skip_line.csv"), "2018-12-09")
        self.assertRaises(SystemExit, parser.readFile)
