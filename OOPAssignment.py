import math
class shape:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"This is a {self.name}")
class circle(shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class rectangle(shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
class triangle(shape):
    def __init__(self, side1, side2, side3, height):
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height
        self.base = side1  # Assuming side1 is the base

    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
circle = circle(5)
rectangle = rectangle(4, 6)
triangle = triangle(3, 4, 5, 4)

circle.display()
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")

rectangle.display()
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")

triangle.display()
print(f"Area: {triangle.area()}")
print(f"Perimeter: {triangle.perimeter()}")

    





        