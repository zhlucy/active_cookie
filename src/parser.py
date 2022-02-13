import argparse
import csv
import re

class Parser:

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("log_file")
        parser.add_argument("-d")
        args = parser.parse_args()
        self.file = args.log_file
        self.date = args.d
        self.structured_content = {}
        self.structure_content()

    def structure_content(self):
        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    cookie, timestamp = row[0], row[1]
                    date = self.extractDate(timestamp)
                    self.updateCookies(date, cookie)
                    line_count += 1


    def extractDate(self, timestamp):
        match = re.search("[0-9]{4}-[0-9]{2}-[0-9]{2}", timestamp)
        if not match:
            raise SystemExit("Timestamp is incorrectly formatted.")
        else:
            return match.group()

    def updateCookies(self, date, cookie):
        if date in self.structured_content.keys():
            cookies = self.structured_content[date]
            cookies[cookie] = cookies.get(cookie, 0) + 1
        else:
            self.structured_content[date] = {cookie : 1}

    def getFile(self):
        return self.file

    def getDate(self):
        return self.date

    def getStructuredContent(self):
        return self.structured_content