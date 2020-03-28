from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

"""
.get(data) function available arguments:
    • deaths          - Deaths
    • cases           - Total Cases
    • curr_infected   - Currently Infected
    • mild_infected   - Mild conditions
    • crit_infected   - Critical conditions
    • recoveries      - Total Recoveries

.get_by_country(country, data) function available arguments
    • country - Any country affected with COVID-19
    • data    - cases, recovered, deaths
"""


class Initialize:
    def __init__(self):
        self.web = Request('https://www.worldometers.info/coronavirus/', headers={'User-Agent': 'Mozilla/5.0'})
        self.web2 = Request('https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic_by_country_and_territory', headers = {'User-Agent': 'Mozilla/5.0'})
        self.cases = re.findall(r'[\d]{1,3},[\d]{3}', str(urlopen(self.web).read()))
        self.soup = BeautifulSoup(urlopen(self.web2).read(), 'html.parser')
    
    def get(self, g):
        info = {"deaths": self.cases[1], "cases": self.cases[0], "curr_infected": self.cases[5], "mild_infected": self.cases[6], "crit_infected": self.cases[7], "recoveries": self.cases[4]}
        return info[g]

    def get_by_country(self, country, d):
        table_temp = self.soup.get_text().strip()
        table = table_temp[table_temp.index("China (mainland)[d]"):table_temp.index("[201]\n\n\nAs of ")].split("\n\n\n\n\n")
        t = {}
        for i in table:
            data = i.split("\n\n")[1:4]
            c = i.split("\n\n")[0].split(r"\[.\]")[0]
            try:
                t[c[0:c.index('[')]] = data
            except:
                t[c] = data
        if d == "cases":
            return t[country][0]
        elif d == "deaths":
            return t[country][1]
        elif d == "recoveries":
            return t[country][2]
        else:
            raise ValueError("Invalid parameter for data...")

if __name__ == "__main__":
    print("This code is not designed to be run directly")
    print("See wiki: https://github.com/marshaaall/corona/blob/master/README.md")
