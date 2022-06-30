colors = { "Yellow": "Amarillo", "Blue": "Azul", "Red":"Rojo"}
print(colors["Yellow"])

print(colors.get("Yellow", "It wasn't found")) #Shows the content of a key and a default message if not found
print(colors.get("Green", "It wasn't found"))

print("Green" in colors) #Shows if there is a key in the dictionary // False
print("Blue" in colors) #Shows if there is a key in the dictionary //True

print(colors.keys()) #Gives the keys of the dictionary in a list
print(colors.values()) #Gives the values of the dictionary in a list
print(colors.items()) #Gives the keys and values of the dictionary in tuples in a list

#Another ways to print keys, values or both
for c in colors.keys():
    print(c)

for c in colors.values():
    print(c)

for k, v in colors.items():
    print(f"{k}, {v}")

colors.pop("Blue", "It wasn't found") #Removes the whole item from the dictionary
print(colors)

colors.clear() #Deletes all the items in the dictionary
print(colors)