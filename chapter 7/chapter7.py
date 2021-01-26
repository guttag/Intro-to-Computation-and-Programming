# -*- coding: utf-8 -*-

# # Code from page 136
# import circle

# # pi = 3
# # print(pi)
# # print(circle.pi)
# # print(circle.area(3))
# # print(circle.circumference(3))
# # print(circle.sphere_surface(3))

# Code from page 137
from circle import * # Note that this will fail if path not set
print(pi)
print(circle.pi)

# # Code from page 138
# import math

# x = 8
# print(math.log(x, 2))

# # Code from page 139
# import calendar as cal

# cal_english = cal.TextCalendar()
# print(cal_english.formatmonth(1949, 3))

# print(cal.LocaleTextCalendar(locale='fr_FR').formatmonth(2049, 3))
# print(cal.LocaleTextCalendar(locale='pl_PL').formatmonth(2049, 3))
# print(cal.LocaleTextCalendar(locale='da_dk').formatmonth(2049, 3))

# print(cal.day_name[cal.weekday(2033, 12, 25)])

# # Code from page 141
# def find_thanksgiving(year):
#     month = cal.monthcalendar(year, 11)
#     if month[0][cal.THURSDAY] != 0:
#         thanksgiving = month[3][cal.THURSDAY]
#     else:
#         thanksgiving = month[4][cal.THURSDAY]
#     return thanksgiving

# print('In 2011', 'U.S. Thanksgiving was on November',
#       find_thanksgiving(2011))

# # Header for finger exercise on page 141
def shopping_days(year):
    """year a number >= 1941
    returns the number of days between U.S. Thanksgiving and
    Christmas in year"""

# # Code on page 142
# name_handle = open('kids', 'w')
# for i in range(2):
#     name = input('Enter name: ')
#     name_handle.write(name + '\n')
# name_handle.close()

# with open('kids', 'r') as name_handle:
#     for line in name_handle:
#         print(line)

# name_handle = open('kids', 'w')
# name_handle.write('Michael')
# name_handle.write('Mark')
# name_handle.close()
# name_handle = open('kids', 'r')
# for line in name_handle:
#     print(line)

# name_handle = open('kids', 'a')
# name_handle = open('kids', 'a')
# name_handle.write('David')
# name_handle.write('Andrea')
# name_handle.close()
# name_handle = open('kids', 'r')
# for line in name_handle:
#     print(line)

