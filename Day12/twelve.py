#Inheritance 
class Employee:
    company = "S7Frage InfoTech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "S7Frage"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(f"The company of a is: {a.company}\nThe company of b is: {b.company}")