# Dictionary Methods

a = {
    1 : "Sumit",
    "Sumit" : "Tripathi",
    "Tripathi" : "Brand",
    "lst" : [4, 7, 5, 8, "Sumit"]
}

x ={} #Empty dictionary 

# print(a.items()) #Returns key–value pairs.
# print(a.keys()) #Returns all keys.
# print(a.values()) #Returns all values.
# print(a["Sumit7"]) #Accessing Values #! Return an error 
# print(a.get("Sumit7")) #Accessing Values #! Prints none
# a.update({"lst":[1, 3, 5, 7, 9, "Sumit Tripathi", "@MaxxUs7"]}) #Adds or updates elements.
# print(a.get("marks", 0))   # returns 0 if key not found "OR"  Returns value of key (safe access).
# a.pop("lst") #Removes a specific item.
# a.popitem() #Removes the last inserted item.
# a.clear() #Removes all elements.
x = a.copy() #Creates a copy of dictionary.
# print("Original: ", a)
# print("Copy:  ", x)