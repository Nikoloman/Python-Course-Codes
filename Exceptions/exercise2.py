try:
    list = [1, 2, 3, 4, 5]
    print(list[10])
except IndexError:
    print("Error: The index you try to access doesn't exit")