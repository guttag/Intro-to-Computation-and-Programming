# -*- coding: utf-8 -*-

# # Figure 3-1
# # Find the cube root of a perfect cube
# x = int(input('Enter an integer: '))
# ans = 0
# while ans**3 < abs(x):
#     ans = ans + 1
# if ans**3 != abs(x):
#     print(x, 'is not a perfect cube')
# else:
#     if x < 0:
#         ans = -ans
#     print('Cube root of', x,'is', ans)

# #Code fragment on page 47
# max_val = int(input('Enter a postive integer: '))
# i = 0
# while i < max_val:
#     i = i + 1
# print(i)

# # Figure 3-2
# # Test if an int > 2 is prime. If not, print smallest divisor
# x = int(input('Enter an integer greater than 2: '))
# smallest_divisor = None
# for guess in range(2, x):
#     if x%guess == 0:
#         smallest_divisor = guess
#         break
# if smallest_divisor != None:
#     print('Smallest divisor of', x, 'is', smallest_divisor)
# else:
#     print(x, 'is a prime number')

# # Figure 3-3
# # Test if an int > 2 is prime. If not, print smallest divisor
# x = int(input('Enter an integer greater than 2: '))    
# smallest_divisor = None
# if x%2 == 0:
#     smallest_divisor = 2
# else:
#     for guess in range(3, x, 2):
#         if x%guess == 0:
#             smallest_divisor = guess
#             break
# if smallest_divisor != None:
#     print('Smallest divisor of', x, 'is', smallest_divisor)
# else:
#     print(x, 'is a prime number')
#    
## Test if an int > 2 is prime. If not, return smallest divisor
#x = int(input('Enter an integer greater than 2: '))    
#smallest_divisor = None
#if x%2 == 0:
#    smallest_divisor = 2
#else:
#    for guess in range(3, x, 2):
#        if x%guess == 0:
#            smallest_divisor = guess
#            break
#if smallest_divisor != None:
#    print('Smallest divisor of', x, 'is', smallest_divisor)
#else:
#    print(x, 'is a prime number')

# x = 25 # A test case for code in Figure 3-4
# # Figure 3-4 
# epsilon = 0.01
# step = epsilon**2
# num_guesses = 0
# ans = 0.0
# while abs(ans**2 - x) >= epsilon and ans <= x:
#     ans += step
#     num_guesses += 1
# print('number of guesses =', num_guesses)
# if abs(ans**2 - x) >= epsilon:
#     print('Failed on square root of', x)
# else:
#     print(ans, 'is close to square root of', x)

# x = 123456 # Another test case for code in Figure 3-4
# epsilon = 0.01
# step = epsilon**2
# num_guesses = 0
# ans = 0.0
# while abs(ans**2 - x) >= epsilon and ans*ans <= x:
#     ans += step
#     num_guesses += 1
# print('number of guesses =', num_guesses)
# if abs(ans**2 - x) >= epsilon:
#     print('Failed on square root of', x)
# else:
#     print(ans, 'is close to square root of', x)

# x = 123456789 # A test case for code in Figure 3-5
# # Figure 3-5
# epsilon = 0.01
# num_guesses, low = 0, 0
# high = max(1, x)
# ans = (high + low)/2
# while abs(ans**2 - x) >= epsilon:
#     print('low =', low, 'high =', high, 'ans =', ans)
#     num_guesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2
# print('number of guesses =', num_guesses)
# print(ans, 'is close to square root of', x)

# epsilon = 0.01
# x = 65
# # Figure 3-6
# Find lower bound on ans
# lower_bound = 0
# while 2**lower_bound < x:
#     lower_bound += 1
# low = lower_bound - 1
# high = lower_bound + 1
# #perform bisection search
# ans = (high + low)/2
# while abs(2**ans - x) >= epsilon:
#     if 2**ans < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2
# print(ans, 'is close to the log base 2 of', x)

# # Code fragment on page 56 and page 59
# x = 0.0
# for i in range(10):
#     x = x + 0.1
# if x == 1.0:
#     print(x, '= 1.0')
# else:
#     print(x, 'is not 1.0')

# k = 24 # Test case for Figure 3-7
# # Figure 3-7
# #Newton-Raphson for square root
# #Find x such that x**2 - 24 is within epsilon of 0
# epsilon = 0.01
# guess = k/2
# while abs(guess**2 - k) >= epsilon:
#     guess = guess - (((guess**2) - k)/(2*guess))
# print('Square root of', k, 'is about', guess)
