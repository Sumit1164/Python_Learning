x = int(input("Enter the age: "))

if(x >= 18):
    print("you are eligible for that")
elif(x == 0):
    print("The given age is not a valid")
elif(x < 0):
    print("Age can not be negative")
else:
    print("You are under 18, Ghar ja lala")