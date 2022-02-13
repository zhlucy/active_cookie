import csv

class CookieFinder:
    def __init__(self, content):
        self.content = content

    def getActiveCookies(self, day):
        if day in self.content.keys():
            cookies = self.content[day]
            max_active_count = max(cookies.values())
            return [cookie for cookie in cookies if cookies[cookie] == max_active_count]
        else:
            return None