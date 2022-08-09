import random
import math

def read_number(start, end, message):
    while True:
        try:
            value = int(input(message))
        except:
            print("Error: Numero no valido")
        else:
            if value >= start and value <= end:
                break
    return value

def generator():
    numbers = read_number (1, 20, "How many numbers do you want to generate? [1 - 20]: ")
    mode = read_number (1, 3, "How do you wanna round the numbers? [1] Up, [2] Down, [3] Normal: ")

    list = []

    for i in range(numbers):
        number = random.uniform(0, 101)
        if mode == 1:
            print(f"{number} -> {math.ceil(number)}")
            number = math.ceil(number)
        elif mode == 2:
            print(f"{number} -> {math.floor(number)}")
            number = math.floor(number)
        elif mode == 3:
            print(f"{number} -> {round(number)}")
            number = round(number)

        list.append(number)
    return list
    
generator()