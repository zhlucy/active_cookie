import unittest
import os.path
from src.inputparser import InputParser

class TestParser(unittest.TestCase):
    testfile = os.path.join("tests", "test_inputs", "cookie_log.csv")

    def test_extractDate(self):
        parser = InputParser(TestParser.testfile, "2018-12-09")
        self.assertEqual("1010-83-21", parser.extractDate("something1010-83-21some"))

    def test_updateCookies(self):
        parser = InputParser(TestParser.testfile, "2018-12-09")
        parser.updateCookies("2018-12-09T14:19:00+00:00", "c1")
        nineth = {"c1" : 1}
        expected = {"2018-12-09" : nineth}
        self.assertDictEqual(expected, parser.getContent())

        parser.updateCookies("2018-12-09T14:19:00+00:00", "c1")
        nineth["c1"] += 1
        self.assertDictEqual(expected, parser.getContent())

        parser.updateCookies("2018-12-08T14:19:00+00:00", "c1")
        eighth = {"c1" : 1}
        expected["2018-12-08"] = eighth
        self.assertDictEqual(expected, parser.getContent())

    def test_readRow(self):
        parser = InputParser(TestParser.testfile, "2018-12-09")
        parser.readRow(["c1", "2018-12-09"])
        nineth = {"c1" : 1}
        expected = {"2018-12-09" : nineth}
        self.assertDictEqual(expected, parser.getContent())

    def test_structureContent(self):
        parser = InputParser(TestParser.testfile, "2018-12-09")
        parser.structureContent()
        nineth = {"AtY0laUfhglK3lC7" : 2, "SAZuXPGUrfbcn5UA" : 1, "5UAVanZf6UtGyKVS" : 1}
        eighth = {"SAZuXPGUrfbcn5UA" : 1, "4sMM2LxV07bPJzwf" : 1, "fbcn5UAVanZf6UtG" : 1}
        seventh = {"4sMM2LxV07bPJzwf" : 1}
        expected = {"2018-12-09" : nineth, "2018-12-08" : eighth, "2018-12-07" : seventh}
        self.assertDictEqual(expected, parser.getContent())

    def test_readFile(self):
        parser = InputParser(TestParser.testfile, "2018-12-09")
        self.assertDictEqual({}, parser.getContent())