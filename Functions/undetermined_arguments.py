import string


def position_undetermined(*args):
    for arg in args:
        print(arg)

position_undetermined("Hi!", 404, [1, 2, 3, 4, 5])

#--------------------------------------------------
def name_undetermined(**kwargs):
    print(kwargs)

name_undetermined(string1 = "Hi!", number1 = 404, list1 = [1, 2, 3, 4, 5])

#--------------------------------------------------
def super_function(*args, **kwargs):
    t = 0 
    for arg in args:
        t += arg
    print("Undetermined sum is", t)

    for kwarg in kwargs:
        print(kwarg, " ", kwargs[kwarg])

super_function(10, 50, -1, 1.56, name = "Hector", age = 20)