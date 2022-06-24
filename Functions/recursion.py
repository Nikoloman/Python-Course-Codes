"""import time
from urllib.request import FancyURLopener

def count_down(number):
    number -= 1
    if number > 0:
        time.sleep(1) #pauses 1 second
        print(number)
        count_down(number) #RECURSION!!1!!1
    else:
        time.sleep(1)
        print("* * * BOOOOOOM!!! * * *")

time_bomb = int(input("Write the time (seconds) you want the bomb to explode: "))

count_down(time_bomb + 1) #Calling the function and sending the value

#----------------------------------------
def factorial(number):
    if number > 1:
        number = number * factorial(number - 1)
    return number

number = int(input("Write the number pf which you want to know its factorial: "))
print(f"Factorial of {number} is {factorial(number)}")"""

#----------------------------------------
def sum(num2):
    if num2 > 0:
        num2 += sum(num2 - 1)
    return num2

num = int(input("Write a number: "))
print(f"The result is: {sum(num)}" ) 