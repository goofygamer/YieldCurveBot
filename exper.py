from datetime import date, timedelta, datetime

recessionList = [[datetime.strptime("1990-07-01", "%Y-%m-%d").date(), datetime.strptime("1991-03-31", "%Y-%M-%d").date()],
[datetime.strptime("2001-03-01", "%Y-%m-%d").date(), datetime.strptime("2001-11-31", "%Y-%M-%d").date()],
[datetime.strptime("2007-12-01", "%Y-%m-%d").date(), datetime.strptime("2009-06-30", "%Y-%M-%d").date()],
[datetime.strptime("2020-02-01", "%Y-%m-%d").date(), datetime.strptime("2020-04-30", "%Y-%M-%d").date()]]

print(recessionList)