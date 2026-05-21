word = "Donkey"

with open("Day10/practice/file4.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("Day10/practice/file4.txt", "w") as f:
    f.write(contentNew)