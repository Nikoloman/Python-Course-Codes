class Vehicle:

    def __init__(self, color, tires) -> None:
        self.color = color
        self.tires = tires

    def __str__(self) -> str:
        return f"color {self.color}, {self.tires} tires"

class Car(Vehicle):

    def __init__(self, color, tires, speed, cc) -> None:
        super().__init__(color, tires)
        self.speed = speed
        self.cc = cc

    def __str__(self) -> str:
        return super().__str__() + f", {self.speed} km/h, {self.cc} cc"

class Truck(Car):

    def __init__(self, color, tires, speed, cc, burden) -> None:
        super().__init__(color, tires, speed, cc)
        self.burden = burden

    def __str__(self) -> str:
        return super().__str__() + f", {self.burden} Kg capacity"

class Bike(Vehicle):

    def __init__(self, color, tires, type) -> None:
        super().__init__(color, tires)
        self.type = type

    def __str__(self) -> str:
        return super().__str__() + f", {self.type} type"

class Motorcycle(Bike):

    def __init__(self, color, tires, type, speed, cc) -> None:
        super().__init__(color, tires, type)
        self.speed = speed
        self.cc = cc

    def __str__(self) -> str:
        return super().__str__() + f", {self.speed} Km/h, {self.cc} cc"

def Catalog(list):
    for i in list:
        print(f"{type(i).__name__}", i)

def catalog(list, many_tires):
    count = 0
    for i in list:
        if i.tires == many_tires:
            print(i)
            count += 1
    print(f"There are {count} vehicles with {many_tires} tires")


c1 = Car("Orange", 4, 200, 1500)
t1 = Truck("Blue", 6, 100, 2500, 200)
b1 = Bike("Green", 2, "Sport")
m1 = Motorcycle("Red", 2, "Mountain", 150, 1000)

list1 = [c1, t1, b1, m1]

Catalog(list1)

catalog(list1, 2)