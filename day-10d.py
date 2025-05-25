from datetime import datetime, timedelta
from time import time

dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
print(dt1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print(duration.days)
print(duration.seconds)
print(duration.total_seconds())
