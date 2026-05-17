def gretst(a, b, c):
    if(a > b > c):
        print(f"The greatest number is A: {a}")
    elif(a < b > c ):
        print(f"The greatest number is B: {b}")
    elif(a < c  > b):
        print(f"The greatest number is C: {c}")
    elif(a == 0 or b == 0 or c == 0):
        print(f"Please enter a number greater than 0: {a,b,c}")
    elif(a == 1 or b == 1 or c == 1):
        print(f"The given number is equal 1:  {a,b,c}")

gretst(1,10,1)