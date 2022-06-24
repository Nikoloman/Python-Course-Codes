from tkinter import N


try:
    n = float(input("Write a number: "))
    5 / n
except ValueError:
    print("You need to write a number")
except TypeError:
    print("You can't divide a number with a chain")
except ZeroDivisionError:
    print("You can't divide with zero")
except Exception as e:
    print(type(e).__name__) #Prints the type of the error