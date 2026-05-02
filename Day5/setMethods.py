x = {1, 3, 5, 7, 9, "Zero", "MaxxUs7"}

print(x, type(x))

x.add(55) #Adding Elements # Adds a single element
x.update([5, 6])  # Adds multiple elements
x.remove(2)   # Removes element; error if not found
x.discard(2)  # Removes element; no error if not found

x.pop() # Removes a random element
x.clear()     # Removes all elements