"""
Given the parameters day, month and year, return whether that date is a valid date.

is_valid_date(35, 2, 2020) ➞ False
# February doesn't have 35 days.

is_valid_date(8, 3, 2020) ➞ True
# 8th March 2020 is a real date.

is_valid_date(31, 6, 1980) ➞ False
# June only has 30 days.
"""
import datetime

inputDate=input("Enter the date in DD/MM/YYYY format ")
day,month,year=inputDate.split('/')
is_valid_date=True
try:
    datetime.datetime(int(year),int(month),int(day))
except ValueError:
    is_valid_date=False
if(is_valid_date):
    print(inputDate," is a valid date.")
else:
    print(inputDate," is not a valid date.")
