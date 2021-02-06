#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:05:53 2020

@author: johnguttag
"""
# # # Code fragment from page 15
# print('Yankees rule!')
# print('But not in Boston!')
# print('Yankees rule,', 'but not in Boston!')

# # # Code fragment from page 19
# pi = 3
# radius = 11
# area = pi * (radius**2)
# radius = 14

# # # Code fragment from page 20
# a = 3.14159
# b = 11.2
# c = a*(b**2)
# diameter = 11.2
# pi = 3.14159
# area = pi*(diameter**2)

# # # Code fragments from page 21
# side = 1 # length of sides of a unit square
# radius = 1 # radius of a unit circle
# # subtract area of unit circle from area of unit square
# area_circle = pi*radius**2
# area_square = side*side
# difference = area_square - area_circle

# x, y = 2, 3
# x, y = y, x
# print('x =', x)
# print('y =', y)

# # # Code fragments from page 23
# if x%2 == 0:
#     print('Even')
# else:
#     print('Odd')
# print('Done with conditional')

# x = 1111111111111111111111111111111 + 222222222222333222222222 +\
#     3333333333333333333333333333333

# # # Code fragments from page 24
# # x = 1111111111111111111111111111111 + 222222222222333222222222 +
# #     3333333333333333333333333333333
    
# x = (1111111111111111111111111111111 + 222222222222333222222222 +
#     3333333333333333333333333333333)

# if x%2 == 0:
#     if x%3 == 0:
#         print('Divisible by 2 and 3')
#     else:
#         print('Divisible by 2 and not by 3')
# elif x%3 == 0:
#     print('Divisible by 3 and not by 2')

# # # Test setup for following code
# x = 1
# y = 2
# z = 3

# if x < y and x < z:
#     print('x is least')
# elif y < z:
#     print('y is least')
# else:
#     print('z is least')

# # # Code fragments from page 25   
# if x%2 != 0 and y%2 != 0 and z%2 != 0:
#     print(max(x, y, z))
# if x%2 != 0 and y%2 != 0 and z%2 == 0:
#     print(max(x, y))
# if x%2 != 0 and y%2 == 0 and z%2 != 0:
#     print(max(x, z))
# if x%2 == 0 and y%2 != 0 and z%2 != 0:
#     print(max(y, z))
# if x%2 != 0 and y%2 == 0 and z%2 == 0:
#     print(x)
# if x%2 == 0 and y%2 != 0 and z%2 == 0:
#     print(y)
# if x%2 == 0 and y%2 == 0 and z%2 != 0:
#     print(z)
# if x%2 == 0 and y%2 == 0 and z%2 == 0:
#     print(min(x, y, z))
    
# answer = min(x, y, z)
# if x%2 != 0:
#     answer = x
# if y%2 != 0 and y > answer:
#     answer = y
# if z%2 != 0 and z > answer:
#     answer = z
# print(answer)

# # # Code fragment from page 26
# print((x if x > z else z) if x > y else (y if y > z else z))

# # # Code fragment from page 29
# num = 30000000
# fraction = 1/2
# print(num*fraction, 'is', fraction*100, '%', 'of', num)
# print(num*fraction, 'is', str(fraction*100) + '%', 'of', num)

# # # Code fragments from page 30
# print(int(num*fraction), 'is', str(fraction*100) + '%', 'of', num)

# print(f'{int(num*fraction)} is {fraction*100}% of {num}')

# print(f'{{{3*5}}}')

# print(f'{3.14159:.2f}')
# print(f'{num*fraction:,.0f} is {fraction*100}% of {num:,}')

# # # Code fragments from page 31
# name = input('Enter your name: ')

# print('Are you really ' + name + '?')
# print(f'Are you really {name}?')

# n = input('Enter an int: ')
# print(type(n))

# # # Code fragment from page 32
# print('Mluvíš anglicky?')
# print('क्या आप अंग्रेज़ी बोलते ह�?')

# # # Code fragments from page 33
# num_x = int(input('How many times should I print the letter X? '))
# to_print = ''
# if num_x == 1:
#     to_print = 'X'
# elif num_x == 2:
#     to_print = 'XX'
# elif num_x == 3:
#     to_print = 'XXX'
# #...
# print(to_print)

# # Figure 2-7
x = 0
ans = 0
num_iterations = 0
while (num_iterations != x):
    ans = ans + x
    num_iterations = num_iterations + 1
print(f'{x}*{x} = {ans}')

# # # Code fragment from page 36
# #Find a positive integer that is divisible by both 11 and 12
# x = 1
# while True:
#     if x%11 == 0 and x%12 == 0:
#         break
#     x = x + 1
# print(x, 'is divisible by 11 and 12')

# # # Code fragment from page 37
# total = 0
# for num in (77, 11, 3):
#     total = total + num
# print(total)

# # # Code fragment from page 38
# x = 4
# for i in range(x):
#     print(i)

# # # Figure 2-9
# x = 3
# ans = 0
# for num_iterations in range(abs(x)):
#     ans = ans + abs(x)
# print(f'{x}*{x} = {ans}')

# # # Code fragment from page 38
# for i in range(2):
#     print(i)
#     i = 0
#     print(i)

# # # Code fragments from page 39
# index = 0
# last_index = 1
# while index <= last_index:
#     i = index
#     print(i)
#     i = 0
#     print(i)
#     index = index + 1

# x=1
# for i in range(x):
#     print(i)
#     x=4

# x = 4
# for j in range(x):
#     for i in range(x):
#         x = 2

# # # Code fragments from page 40
# x = 3
# for j in range(x):
#     print('Iteration of outer loop')
#     for i in range(x):
#         print('    Iteration of inner loop')
#         x = 2

# total = 0
# for c in '12345678':
#     total = total + int(c)
# print(total)
