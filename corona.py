import urllib.request
import re

"""
.get() function available arguments:
    • deaths          - Deaths
    • cases           - Total Cases
    • curr_infected   - Currently Infected
    • mild_infected   - Mild conditions
    • crit_infected   - Critical conditions
    • recoveries      - Total Recoveries
"""

class Info():
    def __init__(self):
        self.web = urllib.request.urlopen('https://www.worldometers.info/coronavirus/')
        self.cases = re.findall(r'[\d]{1,3},[\d]{3}', str(self.web.read()))
    
    def get(self, g):
        info = {"deaths": self.cases[1], "cases": self.cases[0], "curr_infected": self.cases[5], "mild_infected": self.cases[6], "crit_infected": self.cases[7], "recoveries": self.cases[4]}
        return info[g]

if __name__ == "__main__":
    print("This code is not designed to be run directly")
    print("See wiki: https://github.com/marshaaall/corona/blob/master/README.md")