from datetime import datetime
from time import time

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()
dt3 = datetime.strptime("2018/10/11", "%Y/%m/%d")
dt4 = datetime.fromtimestamp(time())

print(f"{dt4.year}/{dt4.month}")
print(dt4.strftime("%Y/%m"))

print(dt1)
print(dt2)
print(dt3)
print(dt4)
