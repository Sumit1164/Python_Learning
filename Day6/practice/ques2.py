s1 = int(input("Enter the Math marks: "))
s2 = int(input("Enter the Physics marks: "))
s3 = int(input("Enter the Chemistry marks: "))

p = 33
if(s1 >= p):
    print("You are pass in Math")
else:
    print("You are fail in Math")

if(s2 >= p):
    print("You are pass in Physics")
else:
    print("You are fail in Physic")

if(s3 >= p):
    print("You are pass in Chemistry")
else:
    print("You are fail in Chemistry")

pax= (s1 + s2 + s3) / 300 * 100

total_marks = s1 + s2 + s3

if s1 >= p and s2 >= p and s3 >= p and  pax >= 44:
    print("Toal marks obtained: ", total_marks)
    print("\nYou are passed", pax)
    print("-------------------------------------------------------------------------------------")
    print("Congratulations on your success.")
else:
    print("Toal marks obtained: ", total_marks)
    print("\nYou are failed", pax)
    print("-------------------------------------------------------------------------------------")
    print("Better luck next time, Try again")