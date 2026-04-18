# Operators -> Arithmetic operator, Assignment operator, Comparison operator, Logical operator


# Arithmetic operator 
# 7 + 4 = 11 -> [7 , 4 -> Operands], { +  -> Operator} (11  -> Result)  

a = 5
b = 7

'''
print(a+b)
print(a-b)
print(a*b)
print(a/b)
'''

# Assignment operator

x = 4 - 3
# print(x)
f = 5
f += 7  # Same as -=, *=, /=
# print(f)

# Comparison operator

'''
n = 5 < 4 # Same '<='
print(n) # O/P -> False
m = 5 > 4 # Same '>='
print(m) # O/P -> True
k = 5 != 7
print(k) # O/P -> True 
g = 4 == 4
print(g) # O/P -> True
'''

# Logical operator

# AND --> T T --- T another will be F
'''
de = True and True
print("True and True ", de)
df = True and False
print("True and False ", df)
dg = False and True
print("False and True ", dg)
dh = False and False
print("False and False ", dh)
'''

# OR -> F F --- F anothe will be T
'''
de = True or True
print("True or True ", de)
df = True or False
print("True or False ", df)
dg = False or True
print("False or True ", dg)
dh = False or False
print("False or False ", dh)
'''

# NOT  T -> F, F -> T
a = not(False)
print(a)
b = not(True)
print(b)