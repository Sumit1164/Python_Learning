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