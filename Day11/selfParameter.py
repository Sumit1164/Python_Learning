class Employee:
    language = "C++ and Python" #This is a class attribute
    salary = 12900200

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


    def greet(self):  #self replace with any string such new or bad...
        print("Hello, Good Morning!")

    @staticmethod
    def greetX():
        print("Hi, Good Night!")


# Static method - sometimes we need a function that does not use the self-parameter. We can define as static method like: 

raka = Employee()
raka.getInfo()
# Employee.getInfo(raka)

raka.greet()
raka.greetX()

# self refers to the instance of the class. it is automatically passed with a function call from an object.