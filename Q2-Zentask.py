class Circle:
    def __init__(self, radius_list):
        #member variable
        self.__pi = 3.141
        #instance variable
        self.radius_list = radius_list

    def calculate_area(self):
        areas = [self.__pi * r**2 for r in self.radius_list]
        return areas

# given list is :
radius_list = [10, 501, 22, 37, 100, 999,7, 351]
circle_instance = Circle(radius_list)
areas = circle_instance.calculate_area()

for i, area in enumerate(areas):
    print(f" Radius = {radius_list[i]}, Area = {area:.2f}")
