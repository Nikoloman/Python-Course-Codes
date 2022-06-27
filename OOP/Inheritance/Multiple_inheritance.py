class A:
    def __init__(self) -> None:
        print("I'm from the A class")
    def a(self):
        print("This method if from A class")
    
class B:
    def __init__(self) -> None:
        print("I'm from the B class")

    def b(self):
        print("This method if from B class")

class C(B, A): #B class gets the priority
    def c(self):
        print("This method is from C class")

c = C()
c.a()
c.b()
c.c()