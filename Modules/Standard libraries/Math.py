import math

pi = 3.14159
print(round(pi)) #Rounds numbers
print(round(4.5)) #Rounds up in .5
print(round(4.49)) #Rounds down in .49

print(math.floor(4.8)) #With .floor it will always round down
print(math.ceil(4.2)) #With .ceil it will always round up

print(abs(5))
print(abs(-5)) #Abs gives the absolute value of a number

n = [1, 2, 3, 4, 5]
print(math.fsum(n)) #fsum gives a sum even with ints, floats and more types of numbers

print(math.trunc(128.5792)) #trunc gives an int out of a float

print(math.pow(5, 3)) #Gives the result of 5 raised to the third power

print(math.pi) #Pi number
print(math.e) #Euler number