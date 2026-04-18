# String
'''
string is a data type in python.
string is a squence of characters enclosed in quotes.
we can primarily write a string in these three ways -> 'single quoted', "double quoted", """Triple quoted""".
String is immutable that means we were never change anything is already string.
string me increment me indexing 0 se start and decrement me indexing -1 se start .
'''

# Index in a Srting start from 0 to (length - 1) in python.
name = "Sumit Tripathi"

names = name[0:3] # 0 to (3 - 1 = 2) -> SUM.
char1 = name[0]
# print(names)
# print(char1)

"""String slicing"""
# print(name[-10 :-1])
# print(name[4:13])



"""Skip value slicing"""
word = "Supercalifragilisticexpialidocious is word"
x = word[0:35:4]
# print(x)




"""String Functions"""
# print(len(word))
# print(word.endswith("ous"))
# print(word.startswith("Supe"))
# print(word.capitalize()) # it converted into capital, first character of the word 
# print(word.lower()) # it make all the character in the word into small latter
# print(word.upper()) # it make all the character in the word into capital latter
# print(word.title()) # it make captilizes the first character of each word in the string

# Triming and Padding 
z = "        hello       "
# print(z.strip()) # removing leading and trailing whitespace
# print(z.lstrip()) # removing leading whitespace
# print(z.rstrip()) # removing trailing whitespace
zx="57"
# print(zx.zfill(15)) #zfill(width) -> Pads the string with zero on the left, to fill the specified width