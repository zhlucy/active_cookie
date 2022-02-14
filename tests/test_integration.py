import unittest
from unittest import mock
import os.path, sys, io, imp
sys.path.append('src')
most_active_cookie = imp.load_source("most_active_cookie", os.path.join("src", "most_active_cookie"))

class Test(unittest.TestCase):
    """
    Test the whole program with sample csv files.
    """
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
        self.check_stdout("AtY0laUfhglK3lC7\n", most_active_cookie.Main.main)

    @mock.patch('sys.argv', ["main", path("cookie_log.csv"), "-d", "2018-12-08"])
    def test_example_two(self):
        expected = ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
        self.check_stdout(self.toString(expected), most_active_cookie.Main.main)

    @mock.patch('sys.argv', ["main", path("long_cookie_log.csv"), "-d", "2012-12-20"])
    def test_long_one(self):
        self.check_stdout("h34d\n", most_active_cookie.Main.main)

    @mock.patch('sys.argv', ["main", path("long_cookie_log.csv"), "-d", "2012-12-10"])
    def test_long_two(self):
        expected = ["qr2d", "hua8d"]
        self.check_stdout(self.toString(expected), most_active_cookie.Main.main)

    @mock.patch('sys.argv', ["main", path("skip_days_log.csv"), "-d", "2011-08-05"])
    def test_skip_days(self):
        self.check_stdout("qr2d\n", most_active_cookie.Main.main)

    @mock.patch('sys.argv', ["main", path("skip_days_log.csv"), "-d", "2012-08-05"])
    def test_skip_days_no_active(self):
        self.check_stdout("No active cookie.\n", most_active_cookie.Main.main)

    @mock.patch('sys.argv', ["main", path("cookie_log.csv"), "-d", "20181209"])
    def test_bad_timestamp(self):
        self.assertRaises(SystemExit, most_active_cookie.Main.main)

    @mock.patch('sys.argv', ["main", path("fakefile"), "-d", "20181209"])
    def test_bad_file(self):
        self.assertRaises(SystemExit, most_active_cookie.Main.main)