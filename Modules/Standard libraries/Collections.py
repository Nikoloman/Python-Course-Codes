from collections import Counter, namedtuple
from collections import defaultdict
from unicodedata import name

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

dict2 = {}
dict2 = defaultdict(float) #Sets a default type value
print(dict2["something"])
print(dict2)

numbers = {}
numbers["Zero"] = "Cero"
numbers["One"] = "Uno"
numbers["Two"] = "Dos"
numbers["Three"] = "Tres"
print(numbers) #Adding ordered numbers

person = namedtuple("Person", "Name Last_name Age") #We can name each value of a tuple
p = person(Name= "Hector", Last_name= "Velázquez", Age= 21)
print(p.Name)
print(p.Last_name)
print(p.Age)
print(p)
print(p[0]) #It can also print the values using like index