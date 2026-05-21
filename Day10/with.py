# f = open("Day10/myfile.txt")

# print(f.read())

# f.close()


# THE SAME CAN BE WRITTEN USING WITH STATEMENT LIKE THIS:

with open("Day10/file.txt") as f:
    print(f.read())

#  YOU DON'T HAVE TO EXPLICITLY CLOSE THE FILE