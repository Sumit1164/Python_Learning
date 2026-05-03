a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))
d = int(input("Enter the number 4: "))


if(a > b and a > c and a> d):
    print("The greatest number is a: ", a)
elif(b > a and b > c and b > d):
    print("The greatest number is b: ", b)
elif(c > a and c > b and c > d):
    print("The greatest number is c: ", c)
elif(d > a and d > b and d > c):
    print("The greatest number is d: ", d)