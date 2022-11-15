import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def square(self):
        if self.width == self.height:
            print("it is a square")
        else:
            print("it is not a square")


object = Rectangle(3, 4)
object.square()
print(object.area())
print(object.perimeter())
print(object.diagonal())