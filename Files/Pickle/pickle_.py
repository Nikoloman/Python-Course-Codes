import pickle

#------------ Binary Writting ---------------
list = [1, 2, 3, 4, 5]
file = open("list.pckl", "wb") # Creatting a binary file using pickle 

pickle.dump(list, file) # Putting the list into the pickle file
file.close()

#------------ Binary Reading ---------------
file = open("list.pckl", "rb") # Opening the file in binary reading
list_2 = pickle.load(file) # Loading the content of the file in list_2
print(list_2)
file.seek(0) # Don't forget to set the pointer at the start again