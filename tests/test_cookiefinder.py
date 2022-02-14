import unittest
from src.cookiefinder import CookieFinder

class TestCookieFinder(unittest.TestCase):
    """
    Tests the functions in CookieFinder.
    """
    nineth = {"AtY0laUfhglK3lC7" : 2, "SAZuXPGUrfbcn5UA" : 1, "5UAVanZf6UtGyKVS" : 1}
    eighth = {"SAZuXPGUrfbcn5UA" : 1, "4sMM2LxV07bPJzwf" : 1, "fbcn5UAVanZf6UtG" : 1}
    content = {"2018-12-09" : nineth, "2018-12-08" : eighth}

    def test_noActiveCookies(self):
        cookiefinder = CookieFinder(self.content)
        self.assertEqual(None, cookiefinder.getActiveCookies("2018-12-07"))

    def test_oneActiveCookie(self):
        cookiefinder = CookieFinder(self.content)
        expected = ["AtY0laUfhglK3lC7"]
        self.assertEqual(expected, cookiefinder.getActiveCookies("2018-12-09"))

    def test_moreActiveCookies(self):
        cookiefinder = CookieFinder(self.content)
        expected = ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
        self.assertEqual(expected, cookiefinder.getActiveCookies("2018-12-08"))
