from io import open
import sys

file = open("counter.txt", "a+") # Opening thefile in append and read mode
file.seek(0)
content = file.readline() 

if len(content) == 0:
    content = "0" # It'll put a zero if the file is empty
    file.write(content)
file.close()

try: # In case something bad happens
    counter = int(content)

    if len(sys.argv) == 2: # Reading if another value has been wrote in console
        if sys.argv[1] == "inc": # Increments
            counter += 1
        elif sys.argv[1] == "dec": # Decrements
            counter -= 1

    print(counter)

    file = open("counter.txt", "w")
    file.write(str(counter)) # Writing the new value in the flie
    file.close()

except:
    print("ERROR: Corrupted file")