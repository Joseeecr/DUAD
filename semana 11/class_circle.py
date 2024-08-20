import math

class Circle:
    def __init__(self, radius):
        self.radius = radius


    def get_area(self):
        area = math.pi * self.radius**2
        rounded_result = round(area, 4)
        print(f"The area of the circle is {rounded_result}cm2")
        return rounded_result


circle_area_object = Circle(5)
circle_area_object.get_area()