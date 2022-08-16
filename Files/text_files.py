from io import open

#-------------Writting---------------
text = "War.\nWar never changes." #A text that will be in the file
file = open("file.txt", "w") #Opening a file with name "file.txt" in write mode
file.write(text) #Writing our text in the file
file.close() #Closing the file

text_2 = "War. War never changes.\nBut men do, through the roads they walk"
file = open("file.txt", "w") #Openig like this will change all the content of the file
file.write(text_2) #Writing the text 2
file.close()

#------------Reading----------------
file = open("file.txt", "r") #Opening the file in read mode
text_3 = file.read() #Gets the text of the file in a variable
print(text_3)
file.close()

file = open("file.txt", "r")
lines = file.readlines() #Gets the text in the file (each line) in a list
print(lines) #Printing all the list
print(lines[1]) #Printing a certain line (in the list)
file.close()

file = open("file.txt", "r")
line = file.readline() #Reads the first line
print(line)
line_2 = file.readline()
print(line_2) #Reads the second line in the file
file.close()

#-------------Append-----------------
file = open("file.txt", "a")
file.write("\n\nFallout: New Vegas") #Adds more text to a file without changing anything
file.close()

#---------Little Exercise------------
with open("file.txt", "r") as file:
    for line in file:
        print(line)