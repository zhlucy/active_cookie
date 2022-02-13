import unittest
from unittest import mock
import os.path, sys, io
sys.path.append('src')
from src.most_active_cookie import Main

class Test(unittest.TestCase):
    def path(filename):
        return os.path.join("tests", "test_inputs", filename)

    def toString(self, lst):
        string = ""
        for cookie in lst:
            string = string + cookie + "\n"
        return string

    def check_stdout(self, string, function, *args):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        function(*args)
        sys.stdout = old_stdout
        self.assertEqual(string, buffer.getvalue())

    @mock.patch('sys.argv', ["main", path("cookie_log.csv"), "-d", "2018-12-09"])
    def test_example_one(self):
        self.check_stdout("AtY0laUfhglK3lC7\n", Main.main)

    @mock.patch('sys.argv', ["main", path("cookie_log.csv"), "-d", "2018-12-08"])
    def test_example_two(self):
        expected = ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
        self.check_stdout(self.toString(expected), Main.main)

    @mock.patch('sys.argv', ["main", path("long_cookie_log.csv"), "-d", "2012-12-20"])
    def test_long_one(self):
        self.check_stdout("h34d\n", Main.main)

    @mock.patch('sys.argv', ["main", path("long_cookie_log.csv"), "-d", "2012-12-10"])
    def test_long_two(self):
        expected = ["qr2d", "hua8d"]
        self.check_stdout(self.toString(expected), Main.main)

    @mock.patch('sys.argv', ["main", path("skip_days_log.csv"), "-d", "2011-08-05"])
    def test_skip_days(self):
        self.check_stdout("qr2d\n", Main.main)

    @mock.patch('sys.argv', ["main", path("skip_days_log.csv"), "-d", "2012-08-05"])
    def test_skip_days_no_active(self):
        self.check_stdout("No active cookie.\n", Main.main)