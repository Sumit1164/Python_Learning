user_name = input("Enter your name: ")

name_length = 10

length_user_name = len(user_name)

if(name_length > length_user_name):
    print("The given user name is less than 10 characters:",user_name, "The length of given user name is:",length_user_name)
else:
    print("The given user name is greater than 10 characters:",user_name, "The length of given user name is:",length_user_name)