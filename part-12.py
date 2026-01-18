#Modules

from datetime import date
import math


#help(math)

print(math.sqrt(4))

print(math.log10(100))
print(math.pi)
print(math.sin(math.radians(90)))

print(date.today())
today = date.today()
print(today)

print(today.day, today.month, today.year)

from datetime import datetime
print(datetime.now())


print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))