# time module
# The time module works with timestamps and measures how long code takes to run.
# A "timestamp" is the number of seconds since January 1, 1970 at midnight UTC, called the epoch.
# For calendar dates, the datetime module is usually more convenient.

import time

# Current timestamp
# time() returns the current time as a float: seconds since the epoch.
now_seconds = time.time()
print("Seconds since epoch:", now_seconds)

# Converting a timestamp into a readable time
# localtime() turns a timestamp into a struct_time with fields like tm_year, tm_mon, and tm_hour.
local = time.localtime(now_seconds)
print("Year:", local.tm_year, "| Month:", local.tm_mon, "| Day:", local.tm_mday)

# strftime() formats a struct_time as text, using the same % codes as datetime.
print(time.strftime("%Y-%m-%d %H:%M:%S", local))

# gmtime() is like localtime(), but it returns UTC time instead of your local time zone.
print("UTC:", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(now_seconds)))

# Pausing the program
# sleep() stops the program for the given number of seconds. Decimals are allowed, such as 0.5.
print("Waiting half a second...")
time.sleep(0.5)
print("Done waiting.")

# Measuring how long code takes
# perf_counter() is a high-resolution timer meant for measuring short durations.
# Use it for timing code, not for telling the time of day.
start = time.perf_counter()
total = sum(range(1_000_000))     # the work we want to measure
end = time.perf_counter()
print(f"Sum: {total}, took {end - start:.6f} seconds")   # :.6f shows 6 digits after the decimal point

# monotonic() always moves forward, even if the system clock is changed.
# It is the best choice for timeouts and elapsed-time checks.
deadline = time.monotonic() + 2   # 2 seconds from now
count = 0
while time.monotonic() < deadline:
    count += 1
print("Loop ran", count, "times in about 2 seconds")

# Converting a time string back into a timestamp
# mktime() takes a struct_time in local time and returns a timestamp.
parsed = time.strptime("2025-01-15 08:30:00", "%Y-%m-%d %H:%M:%S")
print("Timestamp for 2025-01-15 08:30:", time.mktime(parsed))
