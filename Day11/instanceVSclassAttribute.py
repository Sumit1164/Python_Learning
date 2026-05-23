class Employee:
    language = "C++ and Python" #This is a class attribute
    salary = 12900200

sumit = Employee()
sumit.language = "JavaScript"
print(sumit.language)           # Instance attributes, take preference over class attributes during assignment & retrieval.


