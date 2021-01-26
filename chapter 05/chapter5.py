# -*- coding: utf-8 -*-

# # Code fragment from page 89
# t1 = ()
# t2 = (1, 'two', 3)
# print(t1)
# print(t2)

# # Code fragment from page 90
# t1 = (1, 'two', 3)
# t2 = (t1, 3.25)
# print(t2)
# print((t1 + t2))
# print((t1 + t2)[3])
# print((t1 + t2)[2:5])

# # Code at top of page 91
# def intersect(t1, t2):
#     """Assumes t1 and t2 are tuples
#         Returns a tuple containing elements that are in
#           both t1 and t2"""
#     result = ()
#     for e in t1:
#         if e in t2:
#             result += (e,)
#     return result

# print(intersect((1, 'a', 2), ('b', 2, 'a')))

# # Code in paragarph starting Section 5.1.1 onpage 91
# x, y = (3, 4)
# print(x, y)
# a, b, c = 'xyz'
# print(a, b, c)

# # Code at bottom of page 91
# def find_extreme_divisors(n1, n2):
#     """Assumes that n1 and n2 are positive ints
#         Returns a tuple containing the smallest common divisor > 1 and 
#           the largest common divisor of n1 & n2. If no common divisor,
#           other than 1, returns (None, None)"""
#     min_val, max_val = None, None
#     for i in range(2, min(n1, n2) + 1):
#         if n1%i == 0 and n2%i == 0:
#             if min_val == None:
#                 min_val = i
#             max_val = i
#     return min_val, max_val

# # Code on page 92
# min_divisor, max_divisor = find_extreme_divisors(100, 200)
# print(min_divisor, max_divisor)
    
# print(range(10)[2:6][2])
# print(range(0, 7, 2) == range(0, 8, 2))
# print(range(0, 7, 2) == range(6, -1, -2))

# # Code on page 93 
# L = ['I did it all', 4, 'love']
# for e in L:
#     print(e)

# L1 = [1, 2, 3]
# L2 = L1[-1::-1]
# for i in range(len(L1)):
#     print(L1[i]*L2[i])

# # Code on page 94
# Techs = ['MIT', 'Caltech'] 
# Ivys = ['Harvard', 'Yale', 'Brown']

# # Code on page 95
# Univs = [Techs, Ivys]
# Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

# print('Univs =', Univs)
# print('Univs1 =', Univs1)
# print(Univs == Univs1)

# # Code on page 96
# print(Univs == Univs1) #test value equality
# print(id(Univs) == id(Univs1)) #test object equality
# print(Univs is Univs1) #test object equality
# print('Id of Univs =', id(Univs))
# print('Id of Univs1 =', id(Univs1))

# # Code on page 97
# print('Ids of Univs[0] and Univs[1]', id(Univs[0]), id(Univs[1]))
# print('Ids of Univs1[0] and Univs1[1]', id(Univs1[0]), id(Univs1[1]))

# Techs.append('RPI')

# # Code on top of page 98
# print('Univs =', Univs)
# print('Univs1 =', Univs1)

# # Code in middle of page 98
# L1 = [[]]*2
# L2 = [[], []]
# for i in range(len(L1)):
#     L1[i].append(i)
#     L2[i].append(i)
# print('L1 =', L1, 'but', 'L2 =', L2)

# # Code for finger exercise on page 98
# L = [1, 2, 3]
# L.append(L)
# print(L is L[-1])

# # Code on page 99
# def append_val(val, list_1 = []):
#     list_1.append(val)
#     print(list_1)
        
# append_val(3)
# append_val(4)

# L1 = [1,2,3]
# L2 = [4,5,6]
# L3 = L1 + L2
# print('L3 =', L3)
# L1.extend(L2)
# print('L1 =', L1)
# L1.append(L2)
# print('L1 =', L1)

# # Code on page 100
# def remove_dups(L1, L2):
#     """Assumes that L1 and L2 are lists.
#         Removes any element from L1 that also occurs in L2"""
#     for e1 in L1:
#         if e1 in L2:
#             L1.remove(e1)
# L1 = [1,2,3,4]
# L2 = [1,2,5,6]
# remove_dups(L1, L2)
# print('L1 =', L1)

# # Corrected version of remove_dups, per paragraph on page 101
# def remove_dups(L1, L2):
#     """Assumes that L1 and L2 are lists.
#        Removes any element from L1 that also occurs in L2"""
#     for e1 in L1.copy():
#         if e1 in L2:
#             L1.remove(e1)
# L1 = [1,2,3,4]
# L2 = [1,2,5,6]
# remove_dups(L1, L2)
# print('L1 =', L1)

# # Code on page 101 (with correction from errata sheet)           
# L = [2]
# L1 = [L]
# L2 = L1[:]
# L.append(3)
# print('L1 =', L1, 'L2 =', L2)

# # Code from page 101 with deepcopy, per pragraph on page 102
import copy           
# L = [2]
# L1 = [L]
# L2 = L1[:]
# L2 = copy.deepcopy(L1)
# L.append(3)
# print(f'L1 = {L1}, L2 = {L2}')

# # Code from page 102
# L1 = [2]
# L2 = [[L1]]
# L3 = copy.deepcopy(L2)
# L1.append(3)
# print('L2 =', L2, 'L3 =', L3)

# L1 = [2]
# L2 = [L1, L1]
# L3 = copy.deepcopy(L2)
# L3[0].append(3)
# print(L3)

# # Code from page 103
# print([e**2 for e in range(6)])
# print([e**2 for e in range(8) if e%2 == 0])
# print([x**2 for x in [2, 'a', 3, 4.0] if type(x) == int])

# L = [(x, y)
#       for x in range(6) if x%2 == 0
#       for y in range(6) if y%3 == 0]
# print(L)

# print([[(x,y) for x in range(6) if x%2 == 0]
#      for y in range(6) if y%3 == 0])

# # Code from page 104
# L = []
# for x in range(6):
#     if x%2 == 0:
#         for y in range(6):
#             if y%3 == 0:
#                 L.append((x, y))
# print(L)

# [x for x in range(2, 100) if all(x % y != 0  for y in range(3, x))]

# def gen_primes():
#     primes = []
#     for x in range(2, 100):
#         is_prime = True
#         for y in range(3, x):
#             if x%y == 0:
#                 is_prime = False
#         if is_prime:
#             primes.append(x)
#     return primes

# # # Code to test list comprehension on page 104
# e1 = [x for x in range(2, 100) if all(x % y != 0  for y in range(3, x))]
# e2 = gen_primes()
# print((e1 == e2))

# # Figure 5-5 on page 105
# def apply_to_each(L, f):
#     """Assumes L is a list, f a function
#       Mutates L by replacing each element, e, of L by f(e)"""
#     for i in range(len(L)):
#       L[i] = f(L[i])
      
# L = [1, -2, 3.33]
# print('L =', L)
# print('Apply abs to each element of L.')
# apply_to_each(L, abs)
# print('L =', L)
# print('Apply int to each element of', L)
# apply_to_each(L, int)
# print('L =', L)
# print('Apply squaring to each element of', L)
# apply_to_each(L, lambda x: x**2)
# print('L =', L)

# # Code from page 106
# print(list(map(str, range(10))))
# print([str(e) for e in range(10)])

# for i in map(lambda x: x**2, [2, 6, 4]):
#     print(i)

# L1 = [1, 28, 36]
# L2 = [2, 57, 9]
# for i in map(min, L1, L2):
#     print(i)

# # Code from page 109
# print('My favorite professor--John G.--rocks'.split(' '))
# print('My favorite professor--John G.--rocks'.split('-'))
# print('My favorite professor--John G.--rocks'.split('--'))

# # Code from page 110
# baseball_teams = {'Dodgers', 'Giants', 'Padres', 'Rockies'}
# football_teams = {'Giants', 'Eagles', 'Cardinals', 'Cowboys'}

# baseball_teams.add('Yankees')
# football_teams.update(['Patriots', 'Jets'])
# print(baseball_teams)
# print(football_teams)

# # Code from page 111
# print(baseball_teams.union({1, 2}))
# print(baseball_teams.intersection(football_teams))
# print(baseball_teams.difference(football_teams))
# print({'Padres', 'Yankees'}.issubset(baseball_teams))

# print(baseball_teams | {1, 2})
# print(baseball_teams & football_teams)
# print(baseball_teams - football_teams)
# print({'Padres', 'Yankees'} <= baseball_teams)

# # Code from page 112
# month_numbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,
#                 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
# print(month_numbers)
# print('The third month is ' + month_numbers[3])
# dist = month_numbers['Apr'] - month_numbers['Jan']
# print('Apr and Jan are', dist, 'months apart')

# month_numbers['June'] = 6
# month_numbers['May'] = 'V'

# # Figure 5-9 on page 114
# EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je',
#         'eat':'mange', 'drink':'bois', 'John':'Jean',
#         'friends':'amis', 'and': 'et', 'of':'du','red':'rouge'}
# FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I',
#         'mange':'eat', 'bois':'drink', 'Jean':'John',
#         'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'}
# dicts = {'English to French':EtoF, 'French to English':FtoE}

# def translate_word(word, dictionary):
#     if word in dictionary:
#         return dictionary[word]
#     elif word != '':
#         return '"' + word + '"'
#     return word
    
# def translate(phrase, dicts, direction):
#     UC_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     LC_letters = 'abcdefghijklmnopqrstuvwxyz'
#     punctuation = '.,;:?'
#     letters = UC_letters + LC_letters
#     dictionary = dicts[direction]
#     translation = ''
#     word = ''
#     for c in phrase:
#         if c in letters:
#             word = word + c
#         elif word != '':
#             if c in punctuation:
#                 c = c + ' '
#             translation = (translation +
#                            translate_word(word, dictionary) + c)
#             word = ''
#     return f'{translation} {translate_word(word, dictionary)}'

# print(translate('I drink good red wine, and eat bread.',
#                 dicts,'English to French'))
# print(translate('Je bois du vin rouge.',
#                 dicts, 'French to English'))

# # Code from page 113
# FtoE['bois'] = 'wood'
# print(translate('Je bois du vin rouge.', dicts, 'French to English'))

# # Code from page 115
# def key_search(L, k):
#     for elem in L:
#         if elem[0] == k:
#             return elem[1]
#     return None

# capitals = {'France': 'Paris', 'Italy': 'Rome', 'Japan': 'Kyoto'}
# for key in capitals:
#     print('The capital of', key, 'is', capitals[key])

# # Code from page 116
# cities = []
# for val in capitals.values():
#     cities.append(val)
# print(cities, 'is a list of capital cities')

# cap_vals = capitals.values()
# print(cap_vals)
# capitals['Japan'] = 'Toyko'
# print(cap_vals)

# for key, val in capitals.items():
#     print(val, 'is the capital of', key)

# # Header for finger exercise on page 117
def get_min(d):
    """d a dict mapping letters to ints
    returns the value in d with the key that occurs first in the
    alphabet. E.g., if d = {x = 11, b = 12}, get_min returns 12."""

# # Code on page 118
# number_to_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 10: 'ten'}
# word_to_number = {w: d for d, w in number_to_word.items()}
# word_to_number = {w: d for d, w in number_to_word.items() if d < 10}

# # Code on pages 119-120 
gen_code_keys = (lambda book, plain_text:(
{c: str(book.find(c)) for c in plain_text}))

plain_text = 'no is no'
book = 'Once upon a time, in a house in a land far away'
print(gen_code_keys(book, plain_text))

Don_Quixote = 'In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing.'
print(gen_code_keys(Don_Quixote, plain_text))

encoder = (lambda code_keys, plain_text:
    ''.join(['*' + code_keys[c] for c in plain_text])[1:])

encrypt = (lambda book, plain_text:
    encoder(gen_code_keys(book, plain_text), plain_text))

print(encrypt(Don_Quixote, 'no is no'))
    
gen_decode_keys = (lambda book, cipher_text:
    {s: book[int(s)] for s in cipher_text.split('*')})

print(gen_decode_keys(Don_Quixote, '1*13*2*6*57*2*1*13'))

# # Test string for finger exercise on page 120
'22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*59*11*23*11*1*57*6*173*7*11'
