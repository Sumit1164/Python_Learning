'''
Recursion 
- Recursion is a function which calls itself.
- It is used to directly use a mathematical formula as a function.

Factorial of 5! is:
    factorial(1) -> 1
    factorial(2) -> 2 X 1
    factorial(3) -> 3 X 2 X 1
    factorial(4) -> 4 X 3 X 2 X 1
    factorial(5) -> 5 X 4 X 3 X 2 X 1
    factorial(n) -> n X n-1 X ... 3 X 2 X 1 

    factorial(n) = n x factorial (n - 1)
    EX: THIS FUNCTION CAN BE DEFINED AS FOLLOWS

'''
def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)
n = int(input("Enter the number: "))
print(f"The factorial of {n} is: {factorial(n)}")




'''
Recursion is a technique where a function solves a problem by calling itself on smaller problems.
A recursive function usually has:
    1. Base Case → condition to stop recursion
    2. Recursive Call → function calling itself

'''
def countdown(n):
    if n == 0:          # Base case
        print("Done!")
    else:
        print(n)
        countdown(n - 1)   # Recursive call

countdown(5)

'''
How it works
countdown(5) calls countdown(4)
countdown(4) calls countdown(3)
continues...
when n == 0, recursion stops
'''