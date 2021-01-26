# -*- coding: utf-8 -*-

# Code from page 168
# success_failure_ratio = num_successes/num_failures
# print('The success/failure ratio is', success_failure_ratio)

# Code from page 169
# try:
#     success_failure_ratio = num_successes/num_failures
#     print('The success/failure ratio is', success_failure_ratio)
# except ZeroDivisionError:
#     print('No failures, so the success/failure ratio is undefined.')

# # Figure 9-1 from page 170
def get_ratios(vect1, vect2):
    """Assumes: vect1 and vect2 are equal length lists of numbers
       Returns: a list containing the meaningful values of 
             vect1[i]/vect2[i]"""
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('get_ratios called with bad arguments')
    return ratios

# # Code from page 171
# try:
#     print(get_ratios([1, 2, 7, 6], [1, 2, 0, 3]))
#     print(get_ratios([], []))
#     print(get_ratios([1, 2], [3]))
# except ValueError as msg:
#     print(msg)

# val = int(input('Enter an integer: '))
# print('The square of the number you entered is', val**2)

# # Figure 9-1 from page 172
def get_ratios(vect1, vect2): 
    """Assumes: vect1 and vect2 are lists of equal length of numbers
       Returns: a list containing the meaningful values of 
             vect1[i]/vect2[i]"""
    ratios = []
    if len(vect1) != len(vect2):
        raise ValueError('get_ratios called with bad arguments')
    for index in range(len(vect1)):
        vect1_elem = vect1[index]
        vect2_elem = vect2[index]
        if (type(vect1_elem) not in (int, float))\
           or (type(vect2_elem) not in (int, float)):
            raise ValueError('get_ratios called with bad arguments')
        if vect2_elem == 0:
            ratios.append(float('NaN')) #NaN = Not a Number
        else:
            ratios.append(vect1_elem/vect2_elem)
    return ratios

# # Code from page 172
# while True:
#     val = input('Enter an integer: ')
#     try:
#         val = int(val)
#         print('The square of the number you entered is', val**2)
#         break #to exit the while loop
#     except ValueError:
#         print(val, 'is not an integer')

# # Code from page 173
def read_int():
    while True:
        val = input('Enter an integer: ')
        try:
            return(int(val)) #convert str to int before returning
        except ValueError:
            print(val, 'is not an integer')

def read_val(val_type, request_msg, error_msg):
  while True:
      val = input(request_msg + ' ')
      try:
          return(val_type(val)) #convert str to val_typex
      except ValueError:
          print(val, error_msg)

# val = read_val(int, 'Enter an integer:', 'is not an integer')

# # Header from finger exercise on page 175
def find_an_even(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number"""

# # Figure 9-1 from page 175
def get_grades(fname):
    grades = []
    try:
        with open(fname, 'r') as grades_file:
            for line in grades_file:
                try:
                    grades.append(float(line))
                except:
                    raise ValueError('Cannot convert line to float')     
    except IOError:
        raise ValueError('get_grades could not open ' + fname)
    return grades

# try:
#     grades = get_grades('quiz1grades.txt')
#     grades.sort()
#     median = grades[len(grades)//2]
#     print('Median grade is', median)
# except ValueError as error_msg:
#     print('Whoops.', error_msg)

