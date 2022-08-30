import csv

contacts = [ # Creating a contact list with touples
    ("Hector Velázquez", "Android Developer", "hector@example.com"),
    ("Oscar Cabrales", "Web Developer", "oscar@example.com"),
    ("Maximiliano Ledezma", "Project Manager", "max@example.com"),
    ("Michel Ortiz", "Graphic Designer", "michel@example.com")
]

#-------------- Writting csv --------------
with open("contacts.csv", "w", newline="\n") as csvfile: # Opening a csv file
    writer = csv.writer(csvfile, delimiter=",") # Setting the variable writer with it's file and delimiter
    for contact in contacts:
        writer.writerow(contact) # Writes in the file all the info

#-------------- Reading csv --------------
with open("contacts.csv", newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=",") 
    for contact in contacts: # Reading  the file back in touples
        print(contact)

#------- Reading csv with values --------
with open("contacts.csv", newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=",") 
    for name, job, email in contacts: # Reading the file in a diferent way 
        print(name, job, email)

#-------- Writting in Dictionary -------
with open("contacts.csv", "w", newline="\n") as csvfile: # Opening a csv file
    fields = ["name", "job", "email"]
    writer = csv.DictWriter(csvfile, fieldnames=fields) # Setting the variable writer with it's file and delimiter
    writer.writeheader()
    for name, job, email in contacts:
        writer.writerow({
            "name": name, "job": job, "email": email
        }) # Writes in the file all the info

#-------- Reading in Dictionary -------
with open("contacts.csv", newline="\n") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",") 
    for contact in reader: # Reading the file in a diferent way 
        print(contact["name"], contact["job"], contact["email"])