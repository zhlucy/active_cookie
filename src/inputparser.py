import csv, re
import os.path

class InputParser:
    """
    A class that is responsible for parsing the CSV file.

    Attributes:
        file (string): Filepath of the csv file
        date (string): Date of the most active cookies
        content (dictionary): Cookie activties on different dates ex: (date : (cookie : count))
    """

    def __init__(self, file, date):
        """
        Creates an InputParser object.

        Args:
            file (string): Filepath of the csv file
            date (string): Date of the most active cookies
        """
        self.file = file
        self.date = self.extractDate(date)
        self.content = {}

    def readFile(self):
        """
        Check if the file is valid. If it is, then reads the csv file and 
        updates content with cookie activity information.
        """
        if not os.path.isfile(self.file):
            raise SystemExit("File not found.")
        if os.path.getsize(self.file == 0):
            raise SystemExit("Empty file.")
        self.structureContent()

    def structureContent(self):
        """
        Reads the csv file and update content with cookie activity information.
        """
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
        """
        Reads the row of the csv file and update cookie counts stored in content.
        """
        if len(row) != 2:
            raise SystemExit("One row is incorrectly formatted.")
        cookie, timestamp = row[0], row[1]
        self.updateCookies(timestamp, cookie)

    def extractDate(self, timestamp):
        """
        Extracts and returns the date from timestamp.
        """
        match = re.search("[0-9]{4}-[0-9]{2}-[0-9]{2}", timestamp)
        if not match:
            raise SystemExit("Timestamp is incorrectly formatted.")
        else:
            return match.group()

    def updateCookies(self, timestamp, cookie):
        """
        Increment cookie count in content if the cookie had been active on the given date.
        Else, add cookie to the given date with value 1 in content.
        """
        date = self.extractDate(timestamp)
        if date in self.content.keys():
            cookies = self.content[date]
            cookies[cookie] = cookies.get(cookie, 0) + 1
        else:
            self.content[date] = {cookie : 1}

    def getFile(self):
        """
        Returns csv filepath.
        """
        return self.file

    def getDate(self):
        """
        Returns date of the most active cookies.
        """
        return self.date

    def getContent(self):
        """
        Returns content, the mapping of cookie activities.
        """
        return self.content
