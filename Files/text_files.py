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

