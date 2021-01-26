# -*- coding: utf-8 -*-

import random
import numpy as np

# # Code from page 306
def fib(n):
    """Assumes n is an int >= 0
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# # Figure 15-2 from page 308
def fib_memo(n, memo = None):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if memo == None:
        memo = {}
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        memo[n] = result
        return result

def fib_tab(n):
    """Assumes n is an int >= 0
       Returns Fibonacci of n"""
    tab = [1]*(n+1) #only first two values matter
    for i in range(2, n + 1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[n]

# print(fib_memo(120))
# print(fib_tab(120))

# # Header for finger exercise on page 309
def make_change(coin_vals, change):
    """coin_vals is a list of positive ints and coin_vals[0] = 1
       change is a positive int
       return the minimum number of coins needed to have a set of
          coins the values of which sum to change. Coins may be used
          more than once. For example, make_change([1, 5, 8], 11)"""

# # Code from Figure 14-2
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    def get_name(self):
        return self.name
    def get_value(self):
        return self.value
    def get_weight(self):
        return self.weight
    def __str__(self):
        result = ('<' + self.name + ', ' + str(self.value)
                 + ', ' + str(self.weight) + '>')
        return result

def value(item):
    return item.get_value()

def weight_inverse(item):
    return 1.0/item.get_weight()

def density(item):
    return item.get_value()/item.get_weight()

# # Figure 15-5 on page 313  
def max_val(to_consider, avail):
    """Assumes to_consider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if to_consider == [] or avail == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > avail:
        #Explore right branch only
        result = max_val(to_consider[1:], avail)
    else:
        next_item = to_consider[0]
        #Explore left branch
        with_val, with_to_take = max_val(to_consider[1:],
                                     avail - next_item.get_weight())
        with_val += next_item.get_value()
        #Explore right branch
        without_val, without_to_take = max_val(to_consider[1:], avail)
        #Choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
    return result

# # Figure 15-6 on page 314
def small_test():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    val, taken = max_val(Items, 5)
    for item in taken:
        print(item)
    print('Total value of items taken =', val)

def build_many_items(num_items, max_val, max_weight):
    items = []
    for i in range(num_items):
        items.append(Item(str(i),
                          random.randint(1, max_val),
                          random.randint(1, max_weight)))
    return items

def big_test(num_items, avail_weight):
    items = build_many_items(num_items, 10, 10)
    val, taken = max_val(items, avail_weight)
    print('Items Taken')
    for item in taken:
        print(item)
    print('Total value of items taken =', val)

# small_test()    
# big_test(10, 40)
# big_test(40, 100)

# # Figure 15-7 on page 316
def fast_max_val(to_consider, avail, memo = {}):
    """Assumes to_consider a list of items, avail a weight
         memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if (len(to_consider), avail) in memo:
        result = memo[(len(to_consider), avail)]
    elif to_consider == [] or avail == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > avail:
        #Explore right branch only
        result = fast_max_val(to_consider[1:], avail, memo)
    else:
        next_item = to_consider[0]
        #Explore left branch
        with_val, with_to_take =\
                 fast_max_val(to_consider[1:],
                            avail - next_item.get_weight(), memo)
        with_val += next_item.get_value()
        #Explore right branch
        without_val, without_to_take = fast_max_val(to_consider[1:],
                                                avail, memo)
        #Choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
    memo[(len(to_consider), avail)] = result
    return result

# # Version for which dynamic programming will not help on page 319
# def build_many_items(num_items, max_val, max_weight):
#     items = []
#     for i in range(num_items):
#         items.append(Item(str(i),
#                   random.randint(1, max_val),
#                   random.randint(1, max_weight)*random.random()))

#     return items

