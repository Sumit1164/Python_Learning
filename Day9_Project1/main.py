# import random
'''
1 for snake
-1 for water
0 for gun
'''

# computer = random.choice([-1, 0, 1])
# youStr = input("Enter your choice: ")
# youDict = {"s" : 1, "w" : -1, "g" : 0 }
# reverseDict = {1: "Snake", -1: "Water", 0 : "Gun"}
# you = youDict[youStr]

# print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

# if(computer == you):
#     print("Draw, Both are same!")
# else:
#     if(computer == -1 and you == 1):
#         print("You Win!")
#     elif(computer == -1 and you == 0):
#         print("You Lose!")

#     if(computer == 1 and you == -1):
#         print("You Lose!")
#     elif(computer == 1 and you == 0):
#         print("You Win!")

#     if(computer == 0 and you == -1):
#         print("You Win!")
#     elif(computer == 0 and you == 1):
#         print("You Lose!")
#     else:
#         print("Something went wrong!")


import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])

youStr = input("Enter your choice (s/w/g): ")

youDict = {"s": 1, "w": -1, "g": 0}

reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Check valid input first
if youStr not in youDict:
    print("Please Enter a valid Character: s or g or w")

else:
    you = youDict[youStr]

    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    if computer == you:
        print("Draw, both are same!")

    elif computer == -1 and you == 1:
        print("You Win!")

    elif computer == -1 and you == 0:
        print("You Lose!")

    elif computer == 1 and you == -1:
        print("You Lose!")

    elif computer == 1 and you == 0:
        print("You Win!")

    elif computer == 0 and you == -1:
        print("You Win!")

    elif computer == 0 and you == 1:
        print("You Lose!")

    else:
        print("Something went wrong!")


'''
# Replace with this 

if((computer - you) == -1 or(computer - you) == 2):
    print("You Lose!")
else:
    print("You Win!")



'''