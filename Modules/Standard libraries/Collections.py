from collections import Counter

list1 = [1, 2, 3, 4, 1, 2, 3, 1, 2]

print(Counter(list1)) #Returns a dictionary with the elements and how many there are in a list

word = "International"

print(Counter(word)) #It also works with strings

animals = "Dog Cat Sparrow Cat Robin Dog Cat"
print(Counter(animals.split())) #This can be used to separate words and count them

count = Counter(animals.split())
print(count.most_common()) #Prints from the most common element .to the less common in tuples
print(count.most_common(1)) #Prints from the most common element
print(count.most_common(2)) #Prints from the two most common element

list2 = [10, 20, 30, 40, 10, 20, 30, 10, 20, 10]
count2 = Counter(list2)
print(count2.items()) #Prints all the elements like a dictionary
print(count2.keys()) #Prints the keys (the numbers)
print(count2.values()) #Prints the values (how many times a number appears)
print(sum(count2.values())) #Total of elements in the list
dict1 = dict(count2) #Back to dictionary 
print(dict1)
