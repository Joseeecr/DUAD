from abc import ABC, abstractmethod

import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):

    def calculate_perimeter(self, diameter):
        perimeter = math.pi * diameter
        rounded_result = round(perimeter, 2)
        print(f"The perimeter of the circle is {rounded_result}cm")

    def calculate_area(self, radius):
        area = math.pi * radius**2
        rounded_result = round(area, 2)
        print(f"The area of the circle is {rounded_result}cm2")


class Square(Shape):

    def calculate_perimeter(self, side):
        perimeter = side * 4
        print(f"The perimeter of the square is {perimeter}cm")

    def calculate_area(self, side):
        perimeter = side * side
        print(f"The area of the square is {perimeter}cm2")


class Triangle(Shape):

    def calculate_perimeter(self, side_1, side_2, side_3):
        perimeter = side_1 + side_2 + side_3
        print(f"The perimeter of the triangle is {perimeter}cm")

    def calculate_area(self, base, height):
        perimeter = base * height / 2
        print(f"The area of the triangle is {perimeter}cm2")




my_circle = Circle()
my_circle.calculate_perimeter(10)
my_circle.calculate_area(5)
print()

my_square = Square()
my_square.calculate_perimeter(6)
my_square.calculate_area(6)
print()

my_triangle = Triangle()
my_triangle.calculate_perimeter(6, 6, 8.5)
my_triangle.calculate_area(6, 6)