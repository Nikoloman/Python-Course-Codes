numbers = [-12, 84, 13, 20, -33, 101, 9]

def separate(list):
    list.sort()
    even = []
    odd = []
    for num in list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    return even, odd

even, odd = separate(numbers)

print(even)
print(odd)