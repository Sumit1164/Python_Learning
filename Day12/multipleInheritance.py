class Employee:
    company = "S7Frage ITSolution"
    name = "Sumit"
    salary = 58975494094957
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language: {self.language}")

class Programmmer(Employee, Coder):
    company = "S7Frage"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmmer()

b.show()
b.printLanguage()
b.showLanguage()