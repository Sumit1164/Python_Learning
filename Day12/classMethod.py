# A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.

class Employee:
    a = 1
    def show (self):
        print(f"The class attribute of a is {self.a}")

class Computers:
    a = 1
    @classmethod # show class attribute 
    def show (cls):
        print(f"The class attribute of a is {cls.a}")


x = Employee()
x.a = 9 # show instance attribute
x.show()

e = Computers()
e.a = 9
e.show()