from datetime import date, datetime

today = date.today()
now = datetime.now()

print("Today is",today)
print("The date and time is", now)

print()

print("Date's components: ",today.day,today.month,today.year)
print("Current time's components: ",now.hour,now.minute,now.second)
