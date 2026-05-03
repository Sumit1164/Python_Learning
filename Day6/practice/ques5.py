names = ["Sumit", "Aarav", "Rohan", "Aman", "Karan", "Vivek", "Aditya", "Nikhil", "Suresh", "Arjun", "Ananya", "Priya", "Sneha", "Pooja", "Neha", "Kashish", "Riya", "Simran", "Aditi", "Divya"]

inoutx = input("Enter your name: ").capitalize()

if inoutx in names:
    print("Your name in the list: ", inoutx)
else:
    print("Your name is not in the list: ", inoutx)