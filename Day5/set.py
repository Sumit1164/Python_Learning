# Set 

'''
Set is an unordered collection of unique elements.
'''

s = set() #Empty Set

x = {1, 3, 5, 7, 9, "Zero", "MaxxUs7"}

print(type(x))
print(x)
print(s)



a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)         # {1, 2, 3, 4, 5}                a | b   # union
a.intersection(b)  # {3}                            a & b   # intersection
a.difference(b)    # {1, 2}                         a - b   # difference
a.symmetric_difference(b)  # {1, 2, 4, 5}           a ^ b   # symmetric difference

a.issubset(b)
a.issuperset(b)
a.isdisjoint(b)


new_set = a.copy()


fs = frozenset([1, 2, 3])   # cannot add or remove elements