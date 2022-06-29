from ssl import SSL_ERROR_WANT_X509_LOOKUP


set1 = set()
set1.add(1) #Adds an element to the set
set1.add(2)
set1.add(3)
print(set1)
set1.discard(1) #Removes a given element in the set
print(set1)

set2 = set1.copy() #Copies a set to another

set3 = {1, 2, 3}
set4 = {3, 4, 5}
set5 = {1, 2, 3, 4, 5}
set6 = {-2, -1, 0}
print(set3.isdisjoint(set6)) #Shows if two sets doesn't shares elements, it's True here
print(set3.isdisjoint(set4)) #It's False here
print(set3.issubset(set5)) #Shows if all the elements of a set are in another set, it's true here
print(set3.issubset(set4)) #It's False here
print(set5.issuperset(set3)) #Shows if a set has all the elements of another set, it's true here
print(set5.issuperset(set6)) #It's False here
print(set3.union(set4)) #Unit two sets
print(set3.union(set4) == set5) #True
set3.update(set4) #Same as in union with the difference that set3 changed it's value
print(set3)

set3 = {1, 2, 3}
set4 = {3, 4, 5}
set5 = {1, 2, 3, 4, 5}
set6 = {-2, -1, 0}
print(set3.difference(set4)) #Shows the difference between set3 and set4 but only showing set3
set3.difference_update(set4) #Same as in difference, but it updates in set3
print(set3)

set3 = {1, 2, 3}
set4 = {3, 4, 5}
print(set3.intersection(set4)) #Shows the elements that two sets have in common
print(set3.symmetric_difference(set4)) #Shows the elements that two sets doesn't have in common