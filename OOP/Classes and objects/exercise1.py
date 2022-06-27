import math

class Dot:

    def __init__(self, x_axis = 0, y_axis = 0) -> None:
        self.x_axis = x_axis
        self.y_axis = y_axis
    
    def __str__(self) -> str:
        return f"({self.x_axis}, {self.y_axis})"

    def quadrant(self):
        if self.x_axis > 0 and self.y_axis > 0:
            print(f"The dot {self} is in the quadrant number 1")
        
        elif self.x_axis < 0 and self.y_axis > 0:
            print(f"The dot {self} is in the quadrant number 2")

        elif self.x_axis < 0 and self.y_axis < 0:
            print(f"The dot {self} is in the quadrant number 3")

        elif self.x_axis > 0 and self.y_axis < 0:
            print(f"The dot {self} is in the quadrant number 4")
        
        elif self.x_axis == 0 and self.y_axis == 0:
            print(f"The dot {self} is in the origin")

    def vector(self, dot):
        print(f"The vector between {self} and {dot} is ({dot.x_axis - self.x_axis}, {dot.y_axis - self.y_axis})")

    def distance(self, dot):
        dist = math.sqrt((dot.x_axis - self.x_axis) ** 2 + (dot.y_axis - self.y_axis) ** 2)
        print(f"The distance between {self} and {dot} is {dist}")

class Rectangle:

    def __init__(self, dot1 = Dot(), dot2 = Dot()) -> None:
        self.dot1 = dot1
        self.dot2 = dot2
    
    def length(self):
        self.length = abs(self.dot2.x_axis - self.dot1.x_axis)
        print(f"The length of the rectangle is {self.length}")
    
    def width(self):
        self.width = abs(self.dot2.y_axis - self.dot1.y_axis)
        print(f"The width of the rectangle is {self.width}")

    def area(self):
        self.length = abs(self.dot2.x_axis - self.dot1.x_axis)
        self.width = abs(self.dot2.y_axis - self.dot1.y_axis)
        self.area = self.length * self.width
        print(f"The area of the rectangle is {self.area}")

A = Dot(2, 3)
B = Dot(5, 5)
C = Dot(-3, -1)
D = Dot(0, 0)

A.quadrant()
B.quadrant()
C.quadrant()
D.quadrant()

A.vector(B)
B.vector(A)

A.distance(B)

RectangleA = Rectangle(A, B)
RectangleA.length()
RectangleA.width()
RectangleA.area()