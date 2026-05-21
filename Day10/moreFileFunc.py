f = open("Day10/filefun.txt")

# lines = f.readlines()
# print(lines)
# print(type(lines))



# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

line = f.readline()

while(line != ""):
    print(line)
    line = f.readline()
f.close()