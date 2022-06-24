def relation(num1, num2):
    if num1 > num2:
        return 1
    if num1 < num2:
        return -1
    if num1 == num2:
        return 0
    print()

num1 = int(input("Write the first number: "))
num2= int(input("Write the second number: "))

print(f"Output: {relation(num1, num2)}")