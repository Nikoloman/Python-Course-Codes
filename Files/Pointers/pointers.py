from io import open

quote = "I want my revenge.\nAgainst him.\nAgainst Caesar.\nI want to call it my own, to make my anger God's anger.\nTo justify the things I've done."
file = open("joshua's_quote.txt", "w")
file.write(quote)
file.close()

file = open("joshua's_quote.txt", "r")
file.seek(10) #Puts the pointer in the character #10 of the file
print(file.read() + "\n") #Now the program starts reading in the character #10
print(file.read() + "\n") #The pointer is at the end of the file, that's why it doesn't print
file.seek(0) #Putting the pointer at the start of the file
print(file.read() + "\n") #Printing all the file again

file.seek(0)
print(file.read(5)) #Prints the 5 characters ahead the pointer
print(file.read(5) + "\n") #Prints another 5 characters beyond the pointer

complete_quote = file.read()
file.seek( len(complete_quote) / 2 ) #Setting the pointer at the middle of the file
print(file.read()) #Printing the second half of the file

file.seek(0)
file.seek( len(file.readline()) ) #Starts reading at the second line
print(file.read())
file.close()

file = open("joshua's_quote.txt", "r+")
file.write("Joshua Graham") #Changing for a string in the file in the respective characters
file.close()
file = open("joshua's_quote.txt", "w")
file.write(quote)

file = open("joshua's_quote.txt", "r+")
lines = file.readlines()
print(lines)
lines[2] = "Changing a line of the quote in memory\n" #Cahnging a line
print(lines)
file.seek(0)
file.writelines(lines) #Changing all the lines again