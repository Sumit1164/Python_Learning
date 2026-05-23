class Employee:
    language = "C++ and Python" #This is a class attribute
    salary = 12900200

sumit = Employee()
sumit.name = "Sumit" #This is an object(instance) attribute
print(sumit.name, sumit.language, sumit.salary)

kashish =Employee()
kashish.name = "Kashish"
kashish.address = "Sumit's home"
print(kashish.name, kashish.language, kashish.salary, kashish.address)



# Here name is object attribute and salary and language are class attributes as they directly  belong to the class
