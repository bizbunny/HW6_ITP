
>>> from hw6 import *


NOTE: set does not guarantee order, so we have to use equality checks for problems 1-3


##### Problem 1 #####

Write a function intersect(set1, set2) that takes as input two sets of numbers, set1 and set2 and RETURNS a set of unique numbers appearing in BOTH sets.
NOTE: we did this before with lists, but sets make this much easier.

>>> intersect({3, 4, 5, 8, 9, 10, 12}, {5, 6, 7})
{5}
>>> intersect(set(range(0,10)), {1,2,3}) == {1, 2, 3}
True
>>> intersect(set(range(0,10)), {1,7,9}) == {1, 7, 9}
True


##### Problem 2 #####

Write a function union(set1, set2) that takes as input two sets of numbers, set1 and set2 and RETURNS a set of unique numbers appearing in EITHER set.
NOTE: we did this before with lists, but sets make this much easier.

>>> union({3, 4, 5, 8, 9, 10, 12}, {5, 6, 7}) \
...    == {3, 4, 5, 6, 7, 8, 9, 10, 12}
True
>>> union(set(range(0,10)), {1,2,3}) == set(range(10))
True
>>> union(set(range(0,10)), {1,7,10,11}) == set(range(12))
True



##### Problem 3 #####

Write a function uniqueWords(text) that takes as input a text string and RETURNS a set of all unique words.
NOTE: we have performed this logic before, but sets make this much easier.

>>> uniqueWords("it was the best of times it was the worst of times") \
...     == {'it', 'was', 'the', 'best', 'of', 'times', 'worst'}
True
>>> uniqueWords("my bologna has a first name") \
...     == {'my', 'bologna', 'has', 'a', 'first', 'name'}
True
>>> uniqueWords("na na na na na na na na batman") \
...     == {'na', 'batman'}
True



##### Problem 4 ######

Write a function printWithAge that takes as parameters a JSON file name and an age and prints out the name of each player that is that age:
NOTE: we did this before with csv files, but json files and the python json library make this much easier.

>>> printWithAge('cubsRoster.json', 35)
Tony Barnette
Cole Hamels
Jon Lester
>>> printWithAge('cubsRoster.json', 24)
Adbert Alzolay
Ian Happ
Duane Underwood Jr.
>>> printWithAge('cubsRoster.json', 31)
Craig Kimbrel
>>> printWithAge('cubsRoster.json', 38)
Ben Zobrist




##### Problem 5 #####

Write a function reverse(dct) that takes as input a dict and returns a new dict where the keys and values have been flipped.
You can assume the input dict has only string values.

>>> reverse({"boy": "ragazzo", "girl": "ragazza", "baby": "bambino"})
{'ragazzo': 'boy', 'ragazza': 'girl', 'bambino': 'baby'}
>>> reverse({"boy": "niño", "girl": "niña", "baby": "bebe"})
{'niño': 'boy', 'niña': 'girl', 'bebe': 'baby'}
>>> reverse({"boy": "garcon", "girl": "fille", "baby": "bébé"})
{'garcon': 'boy', 'fille': 'girl', 'bébé': 'baby'}