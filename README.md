# corona
An external module to be used inside an application that scrapes data from (various) websites about the COVID-19

Returns details of COVID-19
According to: https://www.worldometers.info/coronavirus/

import corona

Create new instance:
s = corona.Info()


.get() Function usage:

print(s.get("cases"))  # returns Covid-19 cases
