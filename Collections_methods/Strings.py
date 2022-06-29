#--------------------------------------------------------------------------------
#Logic methods with diferent returns

string1 = "Hello there :D"

print(string1.upper()) #Prints all the characters in the chain in uppercase

print(string1.lower()) #Prints all the characters in the chain in lowercase

print(string1.capitalize()) #Prints the string but the first character in uppercase

print(string1.title()) #Prints the string but the first character of each word in uppercase

print(string1.count("e")) #Counts how many times a character is in the string

print(string1.count("there")) #It can also count words or a combination of characters in sequence

print(string1.find("there")) #Prints the index in the string

print(string1.rfind("there")) #Prints the last index

print("Hello there there there".rfind("there")) #A better example of rfind

#--------------------------------------------------------------------------------
#Methods that return boolean values

c = "1000" #A number in a string

print(c.isdigit()) #Prints if the string is a digit

c2 = "ABC123def" #Aphanumeric

print(c2.isalnum()) #Prints if the strings is alphanumeric

print(c2.isalpha()) #Prints if the string is just letters

c3 = "Hello There :D"

print(c3.islower()) #Prints if all the characters are in lowercase

print(c3.isupper()) #Prints if all the characters are in uppercase

print(c3.istitle()) #Prints if the string is a title

print(c3.isspace()) #Prints if all the characters in the string are spaces

print(c3.startswith("H")) #Prints if the string starts with a given character

print(c3.endswith("f")) #Prints if the string starts with a given character

#--------------------------------------------------------------------------------
#Methods that sepates a string

string2 = "Hello There :D"

print(string2.split()) #Split each word between spaces in a list

print(string2.split()[1]) #Split each word between spaces in a list and only shows the indexed one

string3 = "Hello,There,My,Friends"

print(string3.split(",")) #Split each word between a given character in a list

print(",".join(string2)) #Separates each character with a given character in between

print(" ".join(string2)) #Another example

string4 = "       Hello There :D     "

print(string4.strip()) #Deleates all the spaces that aren't useful

print(string2.replace("e", "3")) #Replaces a character with another given character

print(string2.replace("There", "World")) #It works even with words