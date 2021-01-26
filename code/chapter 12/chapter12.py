# -*- coding: utf-8 -*-

# # Code from page 235
# for i in range(len(L)):
#     if L[i] == e:
#         return True
# return False

# # Figure 12-2 from page 238
def search(L, e):
    """Assumes L is a list, the elements of which are in
          ascending order.
       Returns True if e is in L and False otherwise"""
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e: 
            return False
    return False
   
# L = [1,2,3,4,5]
# print(search(L, 4))
# print(search(L, 2.4))

# # Figure 12-3 from page 239
def search(L, e):
    """Assumes L is a list, the elements of which are in
          ascending order.
       Returns True if e is in L and False otherwise"""
    
    def bin_search(L, e, low, high):
        #Decrements high - low
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bin_search(L, e, low, mid - 1)
        else:
            return bin_search(L, e, mid + 1, high)
        
    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, 0, len(L) - 1)
    
# L = [1,2,3,4,5]
# print(search(L, 4))
# print(search(L, 2.4))

# # Figure 12-4 from page 243
def sel_sort(L):
    """Assumes that L is a list of elements that can be
         compared using >.
       Sorts L in ascending order"""
    suffix_start = 0
    while suffix_start != len(L):
        #look at each element in suffix
        for i in range(suffix_start, len(L)):
            if L[i] < L[suffix_start]:
                #swap position of elements
                L[suffix_start], L[i] = L[i], L[suffix_start]
        suffix_start += 1

# # Figure 12-5 from page 245
def merge(left, right, compare):
    """Assumes left and right are sorted lists and
         compare defines an ordering on the elements.
       Returns a new sorted (by compare) list containing the
         same elements as (left + right) would contain."""
    
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L, compare = lambda x, y: x < y):
    """Assumes L is a list, compare defines an ordering
         on elements of L
       Returns a new sorted list with the same elements as L"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

# # Code from page 246
# L = [2,1,4,5,3]
# print(merge_sort(L), merge_sort(L, lambda x, y: x > y))

# # Figure 12-6 from page 248
def last_name_first_name(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
        return arg1[1] < arg2[1]
    else: #last names the same, sort by first name
        return arg1[0] < arg2[0]
def first_name_last_name(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else: #first names the same, sort by last name
        return arg1[1] < arg2[1]

# L = ['Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
# newL = merge_sort(L, last_name_first_name)
# print('Sorted by last name =', newL)
# newL = merge_sort(L, first_name_last_name)
# print('Sorted by first name =', newL)

# # Code from page 248
# L = [3,5,2]
# D = {'a':12, 'c':5, 'b':'dog'}
# print(sorted(L))
# print(L)
# L.sort()
# print(L)
# print(sorted(D))
# D.sort()

# # Code from page 249
# L = [[1,2,3], (3,2,1,0), 'abc']
# print(sorted(L, key = len, reverse = True))

# # Figure 12-7 from page 252
class Int_dict(object):
    """A dictionary with integer keys"""
    
    def __init__(self, num_buckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.num_buckets = num_buckets
        for i in range(num_buckets):
            self.buckets.append([])
            
    def add_entry(self, key, dict_val):
        """Assumes key an int. Adds an entry."""
        hash_bucket = self.buckets[key%self.num_buckets]
        for i in range(len(hash_bucket)):
            if hash_bucket[i][0] == key:
                hash_bucket[i] = (key, dict_val)
                return
        hash_bucket.append((key, dict_val))
        
    def get_value(self, key):
        """Assumes key an int.
           Returns value associated with key"""
        hash_bucket = self.buckets[key%self.num_buckets]
        for e in hash_bucket:
            if e[0] == key:
                return e[1]
        return None
    
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result += f'{e[0]}:{e[1]},'
        return result[:-1] + '}' #result[:-1] omits the last comma

# # Code from page 253
# import random
# random.seed(1) # So results are consistent
# D = Int_dict(17)
# for i in range(20):
#     #choose a random int in the range 0 to 10**5 - 1
#     key = random.choice(range(10**5))
#     D.add_entry(key, i)
# print('The value of the Int_dict is:')
# print(D)
# print('The buckets are:')
# for hash_bucket in D.buckets: #violates abstraction barrier
#     print('  ', hash_bucket)
