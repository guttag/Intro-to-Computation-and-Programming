# -*- coding: utf-8 -*-

# # Code from page 148
def is_smaller(x, y):
     """Assumes x and y are ints
        Returns True if x is less than y and False otherwise."""

# # Code from page 150
def sqrt(x, epsilon):
    """Assumes x, epsilon floats
               x >= 0
               epsilon > 0
       Returns result such that
               x-epsilon <= result*result <= x+epsilon"""
               
# # Code from page 151               
def copy(L1, L2):
    """Assumes L1, L2 are lists
       Mutates L2 to be a copy of L1"""
    while len(L2) > 0: #remove all elements from L2
        L2.pop() #remove last element of L2
    for e in L1: #append L1's elements to initially empty L2
        L2.append(e)

# # Code to test copy (not in book)
# L1 = [1,2,3]
# L2 = [4,5,6]
# copy(L1, L2)
# print(L2)
# copy(L1, L1)
# print(L1)

# # Code from page 152        
def is_prime(x):
    """Assumes x is a nonnegative int
       Returns True if x is prime; False otherwise"""
    if x <= 2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

# # Code from page 153    
def abs(x):
    """Assumes x is an int
       Returns x if x>=0 and –x otherwise"""
    if x < -1:
        return -x
    else:
        return x

# # Figure 8-3 from page page 161
def is_pal(x):
    """Assumes x is a list
       Returns True if the list is a palindrome; False otherwise"""
    temp = x
    temp.reverse
    return temp == x

def silly(n):
    """Assumes n is an int > 0
       Gets n inputs from user
       Prints 'Yes' if the sequence of inputs forms a palindrome;
           'No' otherwise"""
    for i in range(n):
        result = []
        elem = input('Enter element: ')
        result.append(elem)
    if is_pal(result):
        print('Yes')
    else:
        print('No')

# # Code from page 162
# silly(2)

# # Code from page 163
def silly(n):
    """Assumes n is an int > 0
    Gets n inputs from user
    Prints 'Yes' if the sequence of inputs forms a palindrome;
    'No' otherwise"""
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    print(result)
    if is_pal(result):
        print('Yes')
    else:
        print('No')

# silly(2)

# # Code from page 164
# def is_pal(x):
#     """Assumes x is a list
#         Returns True if the list is a palindrome; False otherwise"""
#     temp = x[:]
#     temp.reverse()
#     return temp == x
        
# def silly(n):
#     """Assumes n is an int > 0
#         Gets n inputs from user
#         Prints 'Yes' if the sequence of inputs forms a palindrome;
#             'No' otherwise"""
#     result = []
#     for i in range(n):
#         elem = input('Enter element: ')
#         result.append(elem)
#     print(result)
#     if is_pal(result):
#         print('Yes')
#     else:
#         print('No')

# silly(2)


