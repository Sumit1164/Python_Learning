words = ["Donkey", "bad", "ganda", "chiii"]

with open("Day10/practice/file4.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))

with open("Day10/practice/file4.txt", "w") as f:
    f.write(content)