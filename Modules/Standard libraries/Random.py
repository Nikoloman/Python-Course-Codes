import random

print(random.random()) #Gives a random float number from 0 to 1 --- x > 0 and x < 1

print(random.uniform(1, 10)) #Gives a ramdom float number between two given numbers

print(random.randrange(10)) #Gives a random integer number between 0 and a given number --- x > 0 and x < 10

print(random.randrange(0, 101, 2)) #Gives a random int number between 0 and a given number and steps

s = "Hello There! :D" 
print(random.choice(s)) #Gives a random character from a given string

l = [1, 2, 3, 4, 5]
print(random.choice(l)) #It also works with lists
random.shuffle(l) #Shuffles a list 
print(l)
print(random.sample(l, 2)) #Gives as much random numbers as wanted 
