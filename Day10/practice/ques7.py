with open("Day10/practice/file4.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("Python" in line):
        print(f"Hai bhai. Line number: {lineno}")
        break
    lineno +=1
else:
    print("Le re Land ke, python likha hi nahi")

