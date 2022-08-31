from io import open

file = open("people.txt", "r", encoding="utf8") # Using encode to print accent marks
lines = file.readlines()
file.close()

people = []

for line in lines:
    field = line.replace("\n", "").split(";") # Spliting the string and erasing "\n"
    person = {"id":field[0], "name":field[1], "last name":field[2], "birth date":field[3]}
    people.append(person)

for person in people:
    print(f"(id = {person['id']}) {person['name']} {person['last name']} => {person['birth date']}")