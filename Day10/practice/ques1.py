f = open("Day10/practice/poems.txt", encoding="utf-8")

Content = f.read()
if("broken song" in Content):
    print("The word broken is present in the Content")
else:
    print("The word broken is not present in the Content")

f.close()

# with open("Day10/practice/poems.txt", "r", encoding="utf-8") as f:
#     c = f.read()
#     print(c)