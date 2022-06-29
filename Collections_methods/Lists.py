from traceback import print_tb


list1 = [1, 2, 3, 4]
list1.append(5) #Adds a new element to the list
print(list1)

list1.clear() #Clears all the elements of the list
print(list1)

list2 = [1, 2, 3, 4, 5]
list3 = [6, 7, 8, 9, 10]
list2.extend(list3) #Adds a list to another list
print(list2) 

list4 = ["Hello", "there", "there"]
print(list4.count("there")) #Counts how many times a element is on the list
print(list4.index("Hello")) #Prints the index of a given element

list5 = [1, 2, 3, 4, 5]
list5.insert(0, 0) #Inserts elements in a certain index "(index, element)"
print(list5)

list6 = [10, 20, 30, 40, 50]
list6.pop() #Deletes the last element in the list
print(list6)
list6.pop(0) #It can also delete an element with a given index
print(list6)
list6.remove(30) #Deletes an element with the given value of the element and not with the index
print(list6)

list7 = [10, 20, 30, 40, 50]
list7.reverse() #Reverses the list
print(list7)

list8 = list("Hello There") #Converts a string into a list separing each character
print(list8)

list9 = [5, -2, 10, -20, 0, 3]
list9.sort() #Sorts the elements of the list in order
print(list9)
list9.sort(reverse=True)
print(list9) #Sorts the elements of the list and in reverse