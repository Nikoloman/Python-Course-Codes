import pickle

class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

names = ["Hector", "Oscar", "Max"]
people = []

for n in names:
    p = Person(n)
    people.append(p) # Inserting the objects in the list

file = open("people.pckl", "wb")
pickle.dump(people, file) # Inserting the objects in the list in a binary file
file.close()

file_2 = open("people.pckl", "rb")
people_2 = pickle.load(file_2) # Getting the list from the binary file

for p in people_2:
    print(p)