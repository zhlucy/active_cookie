class CookieFinder:
    """
    A class responsible for finding the most active cookies.
    Attributes:
        content (dictionary): Cookie activties on different dates ex: (date : (cookie : count))
    """

    def __init__(self, content):
        """
        Creates a CookieFinder object.
        Args:
            content (dictionary)
        """
        self.content = content

    def getActiveCookies(self, day):
        """
        Returns a list of most active cookies on the given day. If no active cookies, then return None.
        """
        if day in self.content.keys():
            cookies = self.content[day]
            max_active_count = max(cookies.values())
            return [cookie for cookie in cookies if cookies[cookie] == max_active_count]
        else:
            return None

    def printMostActiveCookies(self, day):
        """
        Prints all of the most active cookies on the given day, one per line. 
        If no active cookies, then print "No active cookies."
        """
        cookies = self.getActiveCookies(day)
        if cookies == None:
            print("No active cookie.")
        else:
            for cookie in cookies:
                print(cookie)