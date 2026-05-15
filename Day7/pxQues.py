'''
Question:

Write a Python program using a while loop that:

Starts from number 1
Prints numbers one by one
Stops when it reaches 10
But skips printing multiples of 3 (like 3, 6, 9)



i =1

while (i <= 10):
    if i % 3 == 0:
        i+=1
        continue
    print(i)
    i+=1

    
'''


'''
Question:

Write a Python program using a while loop that:

Takes a number n = 5 (you can hardcode it)
Calculates the factorial of that number using a while loop
Prints the final result


n = int(input("Enter the number: "))
ans = 1
i = n
while i > 0:
    ans = ans * i
    i-=1
print(ans)

'''




'''
Question:

Write a Python program using a while loop that:

Takes a number (e.g., n = 12345)
Reverses the number
Prints the reversed number
'''
'''
x = int(input("Enter the number: "))

xx = 0
while x > 0:
    print(xx)
    i -= 1


    digit = x % 10
    reversed_num = reversed_num * 10 + digit
    x = x // 10

print(reversed_num)
'''

i =1
while(i <=50):
    print(i)
    i += 1

j = 2
while(j <= 20):
    print(j)
    j += 2