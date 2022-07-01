numbers = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modify(numbers):
    numbers = list(set(numbers)) #Deletes all duplicated elements

    numbers.sort(reverse=True) #Sorts from mayor to minor

    for i, n in enumerate(numbers): #Deletes all even numbers
        if n % 2 != 0:
            del(numbers[i])

    sumn = sum(numbers) #Sums all the numbers in the list
    numbers.insert(0, sumn) #Inserts the result of the sum in the 0 index

    return numbers

new_numbers = modify(numbers)

print(numbers)
print(new_numbers)