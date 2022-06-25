""" Example of structured programming """

from http import client


def show_client(clients, id):
    for c in clients:
        if id == c["Id"]:
            print("{} {}".format(c["Name"], c["Last_name"]))
            return
    print("Client wasn't found")

def remove_client(clients, id):
    for i, c in enumerate(clients):
        if id == c["Id"]:
            del clients[i]
            print(str(c), " Succesfully removed")
    print("Client wasn't found")

clients = [
    {"Name": "Hector", "Last_name": "Velazquez", "Id": "ABCD"},
    {"Name": "Melanie", "Last_name": "Acuña", "Id": "EFGH"}
]

show_client(clients, "ABCD")
remove_client(clients, "ABCD")
print(clients)