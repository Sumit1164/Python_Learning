class Employee:
    a = 1
    @classmethod
    def show (cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname}{self.lname}"
    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

x = Employee()
x.a = 9
x.name= "Sumit Tripathi"
print(x.fname, x.lname)
x.show()