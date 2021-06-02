# Hello, the correct definition for leap year is: "The year has to be divisible by 4 and not exactly divisible by 100, unless it is divisible by 400".
# 1600 is a leap year, but 1700, 1800 and 1900 aren't leap years
import calendar
print(calendar.calendar(2020))
print(calendar.isleap(2020))
