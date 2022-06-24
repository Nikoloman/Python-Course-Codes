from operator import length_hint
from turtle import width


def rectangle_area(w, l):
    return w * l

width = int(input("Write the width of the rectangle: "))
length = int(input("Write the length of the rectangle: "))

print(f"The area of the rectangle is: {rectangle_area(width, length)}")