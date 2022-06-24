def double_value(number):
    return number * 2

n = 10
double_value(n) #doesn't change the value of "n"
print (n) #Output: 10

#-----------------------------
def double_value(number):
    return number * 2

n = 10
n = double_value(n) #does change the value of "n"
print (n) #Output: 20

#-----------------------------
def double_values(numbers):
    for i, n in enumerate(numbers):
        numbers[i] *= 2

ns = [10, 50, 100]
double_values(ns[:]) #doesn't change the value of "ns"
print(ns) #Output: [10, 50, 100]

#-----------------------------
def double_values(numbers):
    for i, n in enumerate(numbers):
        numbers[i] *= 2

ns = [10, 50, 100]
double_values(ns) #does change the value of "ns"
print(ns) #Output: [20, 100, 200]