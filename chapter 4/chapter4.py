# -*- coding: utf-8 -*-

# x = 25
# epsilon = 0.01

# # Figure 4-1
# #Find approximation to square root of x
# if x < 0:
#     print('Does not exist')
# else:
#     low = 0
#     high = max(1, x)
#     ans = (high + low)/2
#     while abs(ans**2 - x) >= epsilon:
#         if ans**2 < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low)/2
#     print(ans, 'is close to square root of', x)

# x1 = 25
# epsilon = 0.01

# # Figure 4-2
# # Find square root of x1
# if x1 < 0:
#     print('Does not exist')
# else:
#     low = 0
#     high = max(1, x1)
#     ans = (high + low)/2
#     while abs(ans**2 - x1) >= epsilon:
#         if ans**2 < x1:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low)/2
# x1_root = ans
# x2 = -8
# #find cube root of x2
# if x2 < 0:
#     is_pos = False
#     x2 = -x2
# else:
#     is_pos = True
# low = 0
# high = max(1, x2)
# ans = (high + low)/2
# while abs(ans**3 - x2) >= epsilon:
#     if ans**3 < x2:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2
# if is_pos:
#     x2_root = ans
# else:
#     x2_root = -ans
#     x2 = -x2
# print('Sum of square root of', x1, 'and cube root of', x2,
#       'is close to', x1_root + x2_root)

# Function definition on page 66
def max_val(x, y):
    if x > y:
        return x
    else:
        return y

# # Code fragment on page 67
max_val(3, 4)

# # Figure 4-3
def find_root(x, power, epsilon):
    #find interval containing answer
    if x < 0 and power%2 == 0:
        return None #Negative number has no even-powered roots
    low = min(-1, x)
    high = max(1, x)
    #use bisection search
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans

# Figure 4-4
def test_find_root(x_vals, powers, epsilons):
    for x in x_vals:
        for p in powers:
            for e in epsilons:
                result = find_root(x, p, e)
                if result == None:
                    val = 'No root exists'
                else:
                    val = 'Okay'
                    if abs(result**p - x) > e:
                        val = 'Bad'
                print(f'x = {x}, power = {p}, epsilon = {e}: {val}')

# # Code to test Figure 4-4                       
x_vals = (0.25, 8, -8)
powers = (1, 2, 3)
epsilons = (0.1, 0.001, 1)
test_find_root(x_vals, powers, epsilons)

# # Code on page 70
# def print_name(first_name, last_name, reverse): 
#    if reverse:
#       print(last_name + ', ' + first_name)
#    else:
#       print(first_name, last_name)

# # Code on page 71     
# print_name('Olga', 'Puchmajerova', False)
# print_name('Olga', 'Puchmajerova', reverse = False)
# print_name('Olga', last_name = 'Puchmajerova', reverse = False)
# print_name(last_name = 'Puchmajerova', first_name = 'Olga',
#           reverse = False)

#print_name('Olga', last_name = 'Puchmajerova', False)

# def print_name(first_name, last_name, reverse = False):
#    if reverse:
#       print(last_name + ', ' + first_name)
#    else:
#       print(first_name, last_name)

# print_name('Olga', 'Puchmajerova')
# print_name('Olga', 'Puchmajerova', True)
# print_name('Olga', 'Puchmajerova', reverse = True)

# print_name(last_name = 'Puchmajerova', first_name = 'Olga')

# # Function definition on page 72
def mean(*args):
    # Assumes at least one argument and all arguments are numbers
    # Returns the mean of the arguments
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

# # Code on page 73
# def f(x): #name x used as formal parameter
#     y = 1
#     x = x + y
#     print('x =', x)
#     return x

# x = 3
# y = 2
# z = f(x) #value of x used as actual parameter
# print('z =', z)
# print('x =', x)
# print('y =', y)


# # Figure 4-5
def f(x):
    def g():
      x = 'abc'
      print('x =', x)
    def h():
      z = x
      print('z =', z)
    x = x + 1
    print('x =', x)
    h()
    g()
    print('x =', x)
    return g

# x = 3
# z = f(x)
# print('x =', x)
# print('z =', z)
# z()

# # Code on page 77
# def f():
#     print(x)

# def g():
#     print(x)
#     x = 1

# x = 3
# f()
# x = 3
# g()
 
# # Figure 4-7     
# def find_root(x, power, epsilon): 
#     """Assumes x and epsilon int or float, power an int,
#            epsilon > 0 & power >= 1
#        Returns float y such that y**power is within epsilon of x.
#            If such a float does not exist, it returns None"""
#     #find interval containing answer
#     if x < 0 and power%2 == 0:
#         return None
#     low = min(-1, x)
#     high = max(1, x)
#     #use bisection search
#     ans = (high + low)/2
#     while abs(ans**power - x) >= epsilon:
#         if ans**power < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low)/2
#     return ans

# # Code to test function in Figure 4-7
# e = 0.001
# print(find_root(25, 2, e), find_root(-8, 3, 3), find_root(14, 4, e))

# # Header from finger exericise on page 82
def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
    x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon of x."""

# # Figure 4-8
def find_root_bounds(x, power):
    """x a float, power a positive int
       return low, high such that low**power <=x and high**power >= x"""
    low = min(-1, x)
    high = max(1, x)
    return low, high

def bisection_solve(x, power, epsilon, low, high):
    """x, epsilon, low, high are floats
        epsilon > 0
        low <= high and there is an ans between low and high s.t.
            ans**power is within epsilon of x
        returns ans s.t. ans**power within epsilon of x"""
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans

def find_root(x, power, epsilon):
    """Assumes x and epsilon int or float, power an int,
           epsilon > 0 & power >= 1
       Returns float y such that y**power is within epsilon of x.
           If such a float does not exist, it returns None"""
    if x < 0 and power%2 == 0:
        return None #Negative number has no even-powered roots
    low, high = find_root_bounds(x, power)
    return bisection_solve(x, power, epsilon, low, high)

# # Code to test Figure 4-8
# x_vals = (0.25, 8, -8)
# powers = (1, 2, 3)
# epsilons = (0.1, 0.001, 1)
# test_find_root(x_vals, powers, epsilons)

# # Figure 4-9    
def bisection_solve(x, eval_ans, epsilon, low, high):
    """x, epsilon, low, high are floats
       epsilon > 0
       eval_ans a function mapping a float to a float
       low <= high and there is an ans between low and high s.t.
           eval(ans) is within epsilon of x
       returns ans s.t. eval(ans) within epsilon of x"""
    ans = (high + low)/2
    while abs(eval_ans(ans) - x) >= epsilon:
        if eval_ans(ans) < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans

# # Code from page 85
def square(ans):
    return ans**2

# low, high = find_root_bounds(99, 2)
# print(bisection_solve(99, square, 0.01, low, high))

# print(bisection_solve(99, lambda ans: ans**2, 0.01, low, high))

# def create_eval_ans():
#     power = input('Enter a positive integer: ')
#     return lambda ans: ans**int(power)

# eval_ans = create_eval_ans()
# print(bisection_solve(99, eval_ans, 0.01, low, high))

# # Figure 4-10
def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
           x > 1, epsilon > 0 & power >= 1
       Returns float y such that base**y is within epsilon of x."""
    def find_log_bounds(x, base):
        upper_bound = 0
        while base**upper_bound < x:
            upper_bound += 1
        return upper_bound - 1, upper_bound
    low, high = find_log_bounds(x, base)
    return bisection_solve(x, lambda ans: base**ans, epsilon, low, high)

# # Code to test figure 4-10
import math

def test_log():
    epsilon = 0.001
    for b in range(2, 6):
        for x in range(1, 100):
            if abs(math.log(x, b) - log(x, b, epsilon)) > epsilon:
                print('Failed on', x, b)
    print('Finished test_log')

test_log()
    
# # Header from Finger exercise on page 87
def find_last(s, sub):
    """s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s"""