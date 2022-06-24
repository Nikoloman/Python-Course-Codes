from pickletools import string1
import string


#formatting using "format"
name = "Hector"
string1 = "Hi {}!".format(name)
print(string1)

#formatting using "f"
name = "Hector"
string2 = f"Hi {name}!"
print(string2)

#formatting
a, b = 5, 10
print(f"The sum of {a} and {b} is {a+b}")

#formatting with functions
def func():
    return "Oscar"

print(f"My friend's name is {func()}")

#formatting with dictionaries
number = {"one": 1, "two": 2, "three": 3}
print(f"The number two is written {number['two']}")

#formatting with left aligment
print(f"{'Hello World!':40}")

#other aligments
text = "Hello Twitter!"

print(f"{text:40}")  #left
print(f"{text:^40}") #center
print(f"{text:>40}") #right

#formatting
limit = 5
length = 40

print(f"{text:<{length}.{limit}}")
print(f"{text:^{length}.{limit}}")
print(f"{text:>{length}.{limit}}")

#formatting
print(f"{1:6d}")
print(f"{10:6d}")
print(f"{100:6d}")
print(f"{1000:6d}")
print(f"{10000:6d}")
print(f"{100000:6d}")