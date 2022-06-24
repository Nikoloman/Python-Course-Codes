from cmath import pi

def circle_area(r):
    return pi * r ** 2

radius = int(input("Write the radius of the circle: "))
print(f"The area of the circle is: {circle_area(radius)}")