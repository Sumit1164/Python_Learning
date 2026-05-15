year = int(input("Enter the year to check is it leap year or not: "))

print("Processing...")

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Yeah, is this year is a leap year")
else:
    print("Oh no, is this year is not a leap year")