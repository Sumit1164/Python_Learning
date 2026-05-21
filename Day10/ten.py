# File input and output 

'''
a = "a very long string with emails"

emails = []
3 seconds


-> The Random Access Memory is volatile, and all its contents are lost once a program terminates in order to persist(save) the data forever, we use files.
-> A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.
-> RAM = Volatile, HDD = Non Volatile
-> Types of files - 1. Text files (.txt, .c, etc),  2. Binary files (.jpg, .dat, etc)
-> 
'''

f = open("Day10/file.txt") #f = open("Day10/file.txt", "r")
data = f.read()
print(data)
f.close()