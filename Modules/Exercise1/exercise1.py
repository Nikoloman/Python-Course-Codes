from Operations import *

def read_numbers():
    num1 = int(input("Write the first number: "))
    num2 = int(input("Write the second number: "))
    return num1, num2

print("------ Menu ------")
print("1.- Sum")
print("2.- Subtraction")
print("3.- Multiplication")
print("4.- Division")

#A try just in case the user types a letter or another character
try:
    option = int(input("Option: "))
except ValueError:
    print("You need to write a number")
else:
    if option == 1:
        num1, num2 = read_numbers()
        print(f"{num1} + {num2} = {sum(num1, num2)}")

    if option == 2:
        num1, num2 = read_numbers()
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

    if option == 3:
        num1, num2 = read_numbers()
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    if option == 4:
        num1, num2 = read_numbers()
        print(f"{num1} / {num2} = {divide(num1, num2)}")

    if option > 4 or option < 1:
        print("Invalid option")