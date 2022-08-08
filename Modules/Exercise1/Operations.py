#Module of operations

def sum(num1, num2):
    try:
        result = num1 + num2
    except TypeError:
        print("Data type isn't valid")
    else:
        return result
    
def subtract(num1, num2):
    try:
        result = num1 - num2
    except TypeError:
        print("Data type isn't valid")
    else:
        return result

def multiply(num1, num2):
    try:
        result = num1 * num2
    except TypeError:
        print("Data type isn't valid")
    else:
        return result

def divide(num1, num2):
    try:
        result = num1 * num2
    except TypeError:
        print("Data type isn't valid")
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        return result