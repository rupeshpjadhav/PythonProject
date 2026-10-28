# datetime module
# The datetime module works with dates, times, and time differences.
# It has several classes:
#   date      - only the day, month, and year
#   time      - only the time of day
#   datetime  - both date and time together
#   timedelta - a length of time, such as "7 days"

from datetime import date, time, datetime, timedelta

# Current date and time
# date.today() returns today's date, with no time part.
today = date.today()
print("Today:", today)

# datetime.now() returns the current date and time together.
now = datetime.now()
print("Now:", now)
# Each part is available as an attribute, so you can read them one at a time.
print("Year:", now.year, "| Month:", now.month, "| Day:", now.day)

# Creating specific dates and times
# You pass the values in order: year, month, day (for date) or hour, minute (for time).
birthday = date(2000, 5, 20)
meeting = time(14, 30)     # 24-hour clock, so 14 means 2 PM
print(birthday)     # 2000-05-20
print(meeting)      # 14:30:00

# Formatting dates as text with strftime
# strftime() ("string format time") turns a date into text using format codes.
# Common codes:
#   %Y = 4-digit year, %m = month (01-12), %d = day (01-31)
#   %H = hour (00-23), %M = minute, %S = second
#   %B = full month name, %A = full weekday name
print(now.strftime("%Y-%m-%d %H:%M:%S"))   # 2026-10-28 09:15:00 (your output will show the current time)
print(now.strftime("%d %B %Y"))            # 28 October 2026
print(now.strftime("%A"))                  # weekday name, e.g. Wednesday

# Parsing text into a datetime with strptime
# strptime() ("string parse time") does the reverse: it reads text and builds a datetime.
# The second argument must describe the layout of the text, using the same format codes.
parsed = datetime.strptime("2025-01-15 08:30", "%Y-%m-%d %H:%M")
print(parsed)

# Date arithmetic with timedelta
# Adding a timedelta moves a date forward or backward by that amount of time.
one_week_later = today + timedelta(days=7)
print("One week from today:", one_week_later)

# Difference between two dates
# Subtracting two dates gives a timedelta. Its .days attribute holds the number of whole days.
days_between = date(2026, 12, 25) - today
print("Days until Christmas:", days_between.days)

# Comparing dates
# Dates can be compared with < > == just like numbers. Earlier dates are "smaller".
print(birthday < today)     # True

# Getting the day of the week (Monday = 0, Sunday = 6)
# weekday() uses 0 for Monday. isoweekday() uses 1 for Monday instead.
print(today.weekday())
# isoformat() returns the standard YYYY-MM-DD format, which is good for storing dates.
print(today.isoformat())    # standard format, e.g. 2026-10-28
