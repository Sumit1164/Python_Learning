class Demo:
    a = 7

o = Demo()
print(o.a) # Print the class attribute because instance attribute is not present. 

o.a = 5 # Instance attribute is set.
print(o.a) # Print the instance attribute because instance attribute is present.

print(Demo.a) # But actual value does not changed, print the class Attribute.