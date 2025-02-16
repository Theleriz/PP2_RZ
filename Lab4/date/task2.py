import datetime as dt
print(f"To day is: {dt.datetime.now()}")
print(f"tomorow {dt.datetime.now() + dt.timedelta(days=1)}")
print(f"yesterday: {dt.datetime.now() - dt.timedelta(days=1)}")
