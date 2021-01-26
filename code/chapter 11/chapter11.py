# -*- coding: utf-8 -*-

# # Cdoe from page 214
def f(i):
    """Assumes i is an int and i >= 0"""
    answer = 1
    while i >= 1:
        answer *= i
        i -= 1
    return answer

# # Code from page 215
def linear_search(L, x):
    for e in L:
        if e == x:
            return True
    return False

# # Code from page 216
def fact(n):
   """Assumes n is a positive int
      Returns n!"""
   answer = 1
   while n > 1:
      answer *=  n
      n -= 1
   return answer

# # Figure 11-1 from page 217
def square_root_exhaustive(x, epsilon):
   """Assumes x and epsilon are positive floats & epsilon < 1
      Returns a y such that y*y is within epsilon of x"""
   step = epsilon**2
   ans = 0.0
   while abs(ans**2 - x) >= epsilon and ans*ans <= x:
       ans += step
   if ans*ans > x:
      raise ValueError
   return ans

# # Figure 11-2 from page 217
def square_root_bi(x, epsilon):
   """Assumes x and epsilon are positive floats & epsilon < 1
      Returns a y such that y*y is within epsilon of x"""
   low = 0.0
   high = max(1.0, x)
   ans = (high + low)/2.0
   while abs(ans**2 - x) >= epsilon:
      if ans**2 < x:
         low = ans
      else:
         high = ans
      ans = (high + low)/2.0
   return ans

# # Figure 11-3 from page 218
def f(x):
   """Assume x is an int > 0"""
   ans = 0
   #Loop that takes constant time
   for i in range(1000):
      ans += 1
   print('Number of additions so far', ans)
   #Loop that takes time x
   for i in range(x):
      ans += 1
   print('Number of additions so far', ans)
   #Nested loops take time x**2
   for i in range(x):
      for j in range(x):
         ans += 1
         ans += 1
   print('Number of additions so far', ans)
   return ans

# Code from page 219
f(10)
f(1000)

# Finger exercise on page 220
def g(L, e):
    """L a list of ints, e is an int"""
    for i in range(100):
        for e1 in L:
            if e1 == e:
                return True
    return False

def h(L, e):
    """L a list of ints, e is an int"""
    for i in range(e):
        for e1 in L:
            if e1 == e:
                return True
    return False

# # Code from page 222
def int_to_str(i):
   """Assumes i is a nonnegative int
      Returns a decimal string representation of i"""
   digits = '0123456789'
   if i == 0:
      return '0'
   result = ''
   while i > 0:
      result = digits[i%10] + result
      i = i//10
   return result


#print(int_to_str(23))
   
def add_digits(n):
   """Assumes n is a nonnegative int
      Returns the sum of the digits in n"""
   string_rep = int_to_str(n)
   val = 0
   for c in string_rep:
       val += int(c)
   return val

#print(add_digits(23))

# # Code from page 223
def add_digits(s):
   """Assumes s is a string of digits
      Returns the sum of the digits in s"""
   val = 0
   for c in s:
       val += int(c)
   return val

# print(add_digits('23'))

def factorial(x):
   """Assumes that x is a positive int
      Returns x!"""
   if x == 1:
      return 1
   else:
      return x*factorial(x-1)

# # Figure 11-4 from page 225
def is_subset(L1, L2):
   """Assumes L1 and L2 are lists.
      Returns True if each element in L1 is also in L2
      and False otherwise."""
   for e1 in L1:
      matched = False
      for e2 in L2:
         if e1 == e2:
            matched = True
            break
      if not matched:
         return False
   return True

# # Figure 11-5 from page 226
def intersect(L1, L2):
   """Assumes: L1 and L2 are lists
      Returns a list without duplicates that is the intersection of
      L1 and L2"""
   #Build a list containing common elements
   tmp = []
   for e1 in L1:
      for e2 in L2:
         if e1 == e2:
            tmp.append(e1)
            break
   #Build a list without duplicates
   result = []
   for e in tmp:
      if e not in result:
         result.append(e)
   return result

# # Figure 11-6 from page 227
def get_binary_rep(n, num_digits):
   """Assumes n and numDigits are non-negative ints
      Returns a str of length numDigits that is a binary
      representation of n"""
   result = ''
   while n > 0:
      result = str(n%2) + result
      n = n//2
   if len(result) > num_digits:
      raise ValueError('not enough digits')
   for i in range(num_digits - len(result)):
      result = '0' + result
   return result

def gen_powerset(L):
   """Assumes L is a list
      Returns a list of lists that contains all possible
      combinations of the elements of L. E.g., if
      L is [1, 2] it will return a list with elements
      [], [1], [2], and [1,2]."""
   powerset = []
   for i in range(0, 2**len(L)):
      bin_str = get_binary_rep(i, len(L))
      subset = []
      for j in range(len(L)):
         if bin_str[j] == '1':
            subset.append(L[j])
      powerset.append(subset)
   return powerset


# letters = 'abcdefghijklmnopqrstuvwxyz'
# print(len(gen_powerset(letters[0:10])))
# print(len(gen_powerset(letters[0:20])))
   
# Code to produce plots in this chapter. Code is not in book
# Don't expect to understand it until after you read chapter on plotting

import matplotlib.pyplot as plt
import math

# x_vals = range(1, 100000, 1)
# y_const, y_log = [], []
# for x in x_vals:
#     y_const.append(15)
#     y_log.append(math.log2(x))
# plt.plot(x_vals, y_const, 'r--', label = 'constant')
# plt.plot(x_vals, y_log, 'k-', label = 'log')
# plt.xlabel('Input Size')
# plt.ylabel('Time')
# plt.title('Constant (15) vs. Log (base 2)')
# plt.legend()

# plt.figure()
# x_vals = range(1, 100000, 1)
# y_log, y_linear = [], []
# for x in x_vals:
#     y_linear.append(x)
#     y_log.append(math.log2(x))
# plt.plot(x_vals, y_linear, 'r--', label = 'linear')
# plt.plot(x_vals, y_log, 'k-', label = 'log')
# plt.xlabel('Input Size')
# plt.ylabel('Time')
# plt.title('Log (base 2) vs. Linear')
# plt.legend()

# plt.figure()
# x_vals = range(1, 1000, 1)
# y_log_linear, y_linear = [], []
# for x in x_vals:
#     y_linear.append(x)
#     y_log_linear.append(x*math.log2(x))
# plt.plot(x_vals, y_linear, 'r--', label = 'linear')
# plt.plot(x_vals, y_log_linear, 'k-', label = 'log-linear')
# plt.xlabel('Input Size')
# plt.ylabel('Time')
# plt.title('Linear vs. Log-linear')
# plt.legend()

# plt.figure()
# x_vals = range(1, 1000, 1)
# y_log_linear, y_quadratic = [], []
# for x in x_vals:
#     y_quadratic.append(x**2)
#     y_log_linear.append(x*math.log2(x))
# plt.plot(x_vals, y_quadratic, 'r--', label = 'quadratioc')
# plt.plot(x_vals, y_log_linear, 'k-', label = 'log-linear')
# plt.xlabel('Input Size')
# plt.ylabel('Time')
# plt.title('Log-linear vs. Quadratic')
# plt.legend()

# plt.figure()
# x_vals = range(1, 100, 1)
# y_quad, y_exp = [], []
# for x in x_vals:
#     y_quad.append(x**2)
#     y_exp.append(2**x)
# plt.plot(x_vals, y_quad, 'r--', label = 'quadratic')
# plt.plot(x_vals, y_exp, 'k-', label = 'exponential')
# plt.xlabel('Input Size')
# plt.ylabel('Time')
# plt.title('Quadratic vs. Exponential')
# plt.legend()

# plt.semilogy()
    