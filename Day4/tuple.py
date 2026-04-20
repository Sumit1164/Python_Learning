# Tuple

'''
A tuple is a built-in data type used to store multiple items in a single variable, similar to a list—but with one key difference:
Tuples are immutable (cannot be changed after creation).
'''

a = (1, 5, 8, 13, 13)
ax = () #empty tuple
axx = (1) #is it a integer why not it can be a tuple 
axxx = (1,) #it is a tuple because seprate with comma so python interpreater understand here are some values
# print(type(a))


# Tuple Methods

x = a.count(13) #Returns how many times a value appears - 2
# print(x)

zx = a.index(5) #Returns the first index of a value - 1
# print(zx)