#!/usr/bin/env python

from parser import Parser
from cookiefinder import CookieFinder

def main():
    parser = Parser()
    cookieFinder = CookieFinder(parser.getStructuredContent())
    cookies = cookieFinder.getActiveCookies(parser.getDate())
    printCookies(cookies)

def printCookies(cookies):
    if cookies == None:
        print("No active cookie.")
    else:
        for cookie in cookies:
            print(cookie)

if __name__ == '__main__':
    main()