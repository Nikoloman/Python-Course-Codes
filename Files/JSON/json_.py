import json

contacts = [ # Creating a contact list with touples
    ("Hector Velazquez", "Android Developer", "hector@example.com"),
    ("Oscar Cabrales", "Web Developer", "oscar@example.com"),
    ("Maximiliano Ledezma", "Project Manager", "max@example.com"),
    ("Michel Ortiz", "Graphic Designer", "michel@example.com")
]

data = []

for name, job, email in contacts: # Creating the list as a Dictionary
    data.append({"name": name, "job": job, "email":email})

#-------------- Writing json --------------
with open("contacts.json", "w") as jsonfile:
    json.dump(data, jsonfile) # Inserting the data in the json file

#-------------- Reading json --------------
with open("contacts.json", "r") as jsonfile:
    data = json.load(jsonfile) # Inserting the data of the json into "data"
    for contact in data:
        print(contact["name"], contact["job"], contact["email"]) # Printing all the read data in "data"