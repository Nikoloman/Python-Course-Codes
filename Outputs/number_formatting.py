v = "another text"
n = 10
print("This is a text,", v, "and a number:", n) #first way

c = "This is a text, {} and a number: {}".format(v, n) #second way
print(c)

c = "This is a text, {1} and a number: {0}".format(v, n) #changes order
print(c)

c = "This is a text, {text} and a number: {number}".format(text = v, number = n) #uses codes
print(c)

print("{:>30}".format("Palabra")) #align to right 30 spaces

print("{:<30}".format("Palabra")) #align to left 30 spaces

print("{:^30}".format("Palabra")) #align to center 30 spaces
    
print("{:.3}".format("Palabra")) #Truncate to 3 characters

print("{:^30.3}".format("Palabra")) #align to center and truncate 30 spaces

#integer numbers formating with spaces
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

#integer numbers formating with 0
print()
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

#float numbers formating with spaces
print()
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))

input("Press ENTER to exit")