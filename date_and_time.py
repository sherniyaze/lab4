import datetime
time_now = datetime.datetime.now()
subtract = datetime.timedelta(days=5)
final_result = time_now - subtract
print(final_result)
date_now = datetime.date.today()
subtract_days = datetime.timedelta(days=5)
day = date_now-subtract_days
print(day)

today = datetime.date.today()
def yesterday_today_tomorrow(current):
    x = datetime.timedelta(days=1)
    print(current-x)
    print(current)
    print(current+x)
yesterday_today_tomorrow(today)

without_micro = datetime.datetime.now()
micro = without_micro.replace(microsecond=0)
print(micro)

date_in_string = input("Your date and time: ")
your_date = datetime.datetime.strptime(date_in_string, "%Y-%m-%d %H:%M:%S")
print(your_date)
date_number_2 = input("Your second date: ")
date_number_2 = datetime.datetime.strptime(date_number_2, "%Y-%m-%d %H:%M:%S")
print(date_number_2)
delta_of_two = abs(date_number_2-your_date)
print(delta_of_two)
print(delta_of_two.total_seconds())
