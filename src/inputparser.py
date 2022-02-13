import csv, re
import os.path

class InputParser:

    def __init__(self, file, date):
        self.file = file
        self.date = date
        self.content = {}

    def readFile(self):
        if not os.path.isfile(self.file):
            raise SystemExit("File not found.")
        if os.path.getsize(self.file == 0):
            raise SystemExit("Empty file.")
        self.structureContent()

    def structureContent(self):
        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    if (row != ["cookie", "timestamp"]):
                        raise SystemExit("Incorrect columns.")
                else:
                    self.readRow(row)
                line_count += 1
                
    def readRow(self, row):
        if len(row) != 2:
            raise SystemExit("One row is incorrectly formatted.")
        cookie, timestamp = row[0], row[1]
        #Consider short circuiting
        self.updateCookies(timestamp, cookie)

    def extractDate(self, timestamp):
        match = re.search("[0-9]{4}-[0-9]{2}-[0-9]{2}", timestamp)
        if not match:
            raise SystemExit("Timestamp is incorrectly formatted.")
        else:
            return match.group()

    def updateCookies(self, timestamp, cookie):
        date = self.extractDate(timestamp)
        if date in self.content.keys():
            cookies = self.content[date]
            cookies[cookie] = cookies.get(cookie, 0) + 1
        else:
            self.content[date] = {cookie : 1}

    def getFile(self):
        return self.file

    def getDate(self):
        return self.date

    def getContent(self):
        return self.content