import datetime
time_now = datetime.datetime.now()
subtract = datetime.timedelta(days=5)
final_result = time_now - subtract
print(final_result)
date_now = datetime.date.today()
subtract_days = datetime.timedelta(days=5)
day = date_now-subtract_days
print(day)