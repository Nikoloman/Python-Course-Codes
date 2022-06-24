from multiprocessing.sharedctypes import Value


def add_once(list, el):
    try:
        if el in list:
            raise ValueError
        else:
            list.append(el)
    except ValueError:
        print("Error: It's not posiible to have 2 same elements in the list -> {}".format(el))

elements = [1, 5, -2]

while True:
    new_element = int(input("Write a new element to the list:"))
    add_once(elements, new_element)
    print(elements)