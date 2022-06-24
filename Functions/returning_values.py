def greetings():
    return "Returned string"
print(greetings())

c = greetings()
print(c)

#----------------------------
def test():
    return [1, 2, 3, 4, 5]

print(test()[1:4])

l = test()[-1]
print(l)

#----------------------------
def test2():
    return "Hello", 12345, [1, 2, 3, 4, 5]

print(test2())

string1, number, list1 = test2()
print(f"{string1}, {number}, {list1}")