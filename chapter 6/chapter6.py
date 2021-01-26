# -*- coding: utf-8 -*-

# # Code from Figure 6-1 on page 124
def fact_iter(n):
    """Assumes n an int > 0
      Returns n!"""
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def fact_rec(n):
    """Assumes n an int > 0
      Returns n!"""
    if n == 1:
        return n
    else:
        return n*fact_rec(n - 1)

# # Figure 6-3 on page 127      
# def fib(n):
#     """Assumes n int >= 0
#     Returns Fibonacci of n"""
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# def test_fib(n):
#     for i in range(n+1):
#         print('fib of', i, '=', fib(i))

# test_fib(4)

# # Figure 6-4 on page 119
def is_palindrome(s):
    """Assumes s is a str
    Returns True if letters in s form a palindrome; False
    otherwise. Non-letters and capitalization are ignored."""
    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
        
    return is_pal(to_chars(s))

# print(is_palindrome('Able was I ere I saw Elba'))
# print(is_palindrome('Able was I ere I saw Atlanta'))

# # Figure 6-5 on page 131
def is_palindrome(s):
   """Assumes s is a str
      Returns True if s is a palindrome; False otherwise.
       Punctuation marks, blanks, and capitalization are ignored."""
   
   def to_chars(s):
      s = s.lower()
      letters = ''
      for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            letters = letters + c
      return letters

   def is_pal(s):
      print('  is_pal called with', s)
      if len(s) <= 1:
         print('  About to return True from base case')
         return True
      else:
         answer = s[0] == s[-1] and is_pal(s[1:-1])
         print('  About to return', answer, 'for', s)
         return answer
         
   return is_pal(to_chars(s))

# print('Try dogGod')
# print(is_palindrome('dogGod'))
# print('Try doGood')
# print(is_palindrome('doGood'))

# # Figure 6-6 on page 133
def fib(x):
    """Assumes x an int >= 0
       Returns Fibonacci of x"""
    global num_fib_calls
    num_fib_calls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def test_fib(n):
    for i in range(n+1):
        global num_fib_calls
        num_fib_calls = 0
        print('fib of', i, '=', fib(i))
        print('fib called', num_fib_calls, 'times.')

# test_fib(6)