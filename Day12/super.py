class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1
class Coder(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Coder")
    b = 2
class Tester(Coder):
    def __init__(self):
        super().__init__() # Run the Coder Constructor using super
        print("Constructor of Tester")
    c = 3

# o = Employee()
# print(o.a)

# o = Coder()
# print(o.a, o.b)

o = Tester()
print(o.a, o.b, o.c)