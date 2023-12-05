import math

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self):
        areas = [math.pi * r**2 for r in self.radius_list]
        return areas

# given list is :
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radius_list)
areas = circle_instance.calculate_area()

for i, area in enumerate(areas):
    print(f"Circle {i+1}: Radius = {radius_list[i]}, Area = {area:.2f}")
