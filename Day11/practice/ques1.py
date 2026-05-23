class Programmer:
    company = "S7frage"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary =salary
        self.pin = pin


p = Programmer("Sumit Tripathi", 90000000000000, 272204)
print(f"Company: {p.company}, Name: {p.name}, Salary: {p.salary}, PinCode: {p.pin}")


p1 = Programmer("Amit Tripathi", 99000000000000, 272204)
print(f"Company: {p1.company}, Name: {p1.name}, Salary: {p1.salary}, PinCode: {p1.pin}")