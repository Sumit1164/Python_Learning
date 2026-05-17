# write a python function to remove a given word from a list ad  strip it at the same time, esay explanation and easy code in python 
def remove_word(words, remove_item):
    cleaned_list = []

    for word in words:
        word = word.strip()   # removes extra spaces

        if word != remove_item:
            cleaned_list.append(word)

    return cleaned_list


# Example
my_list = [" apple ", "banana ", " orange", "banana"]

result = remove_word(my_list, "an")

print(result)
print(my_list)