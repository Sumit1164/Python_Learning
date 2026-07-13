class Employee:
    company = "S7Frage ITSolution"
    name = "Sumit"
    salary = 58975494094957
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")
    def aboutEmp(jon):
        name ="Sumit"
        gf = "404 Not Found"
        print(f"The {name} Girlfriend name is {gf}, and now she left him alone")
class Coder(Employee):
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language: {self.language}")
class Tester(Coder):
    language = "Python"
    def testLanguage(self):
        print(f"Here your coder is tested by the tester: {self.language}")
b = Tester()
b.testLanguage()
b.show()
b.printLanguage()
b.aboutEmp()