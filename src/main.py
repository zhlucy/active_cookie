#!/usr/bin/env python
import argparse
from inputparser import InputParser
from cookiefinder import CookieFinder

class Main:
    def main():
        parser = Main.getParser()
        parser.readFile()
        cookieFinder = CookieFinder(parser.getContent())
        cookieFinder.printMostActiveCookies(parser.getDate())

    def getParser():
        parser = argparse.ArgumentParser()
        parser.add_argument("log_file")
        parser.add_argument("-d")
        args = parser.parse_args()
        return InputParser(args.log_file, args.d)

if __name__ == '__main__':
    Main.main()