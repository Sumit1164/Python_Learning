# Functions
def avg():
    a = int(input("Enter a number a: "))
    b = int(input("Enter a number b: "))
    c = int(input("Enter a number c: "))
    average = (a+b+c) / 3
    print(average)
avg()

def greet():
    a = input("Enter Your Name: ")
    print(f"Hello {a}, Good Morning!")
greet()


# Function with argument
def goodDay(name):
    print("Good Day, " + name + "!")
goodDay("Sumit")


# Function with multiple argument
def goodDays(name, ending):
    print("Good Day, " + name + ending)
goodDays("Sumit ", "Thank You!")
goodDays("Kajal ", "Thanks!")


# Return function
def add(a, b):
    print("The sum of two number is: ",a+b)
    return "Done"
a = add(9, 7)
print(a)