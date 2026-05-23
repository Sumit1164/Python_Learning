class Employee:
    language = "C++ and Python" 
    salary = 12900200

    def __init__(self, name, salary, language): #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):  #self replace with any string such new or bad...
        print("Hello, Good Morning!")

    @staticmethod
    def greetX():
        print("Hi, Good Night!")

raka = Employee("Raka", 18649434, "Rust")
print(f"NAME: {raka.name}, SALARY: {raka.salary}, LANGUAGE: {raka.language}")