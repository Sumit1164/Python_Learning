with open("Day10/practice/file4.txt") as f:
    content1 = f.read()

with open("Day10/practice/this8_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical")
else:
    print("No these files are not identical")