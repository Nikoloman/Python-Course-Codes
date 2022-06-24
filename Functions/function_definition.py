#--------------------
#create a function
def greetings():
    print ("Hello Twitter!")

#calling the function
greetings()

#--------------------
def five_times_table():
    for i in range (11):
        print(f"5 * {i} = {i * 5}")

five_times_table()

#--------------------
m = 10

def test():
    print(m)

test()

#--------------------
def test2():
    x = 10 #it's a local variable
    print (x)
test2()
x = 5
test2()
print(x)