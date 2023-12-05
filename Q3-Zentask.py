class rectangle:
    def __init__(self, length,width):
        self.length = length
        self.width = width
    def area(self) :
        return self.length * self.width
    def perimeter(self) :
        return 2*(self.length + self.width)
given_list = [10, 501, 22, 37, 100, 999,7, 351]
#create instances of class rectangle
rectangles = [rectangle(given_list[i], given_list[i+1]) for i in range(0, len(given_list), 2)] 
for i, rectangle in enumerate(rectangles, start=1):
    print(f"Rectangle {i}:")
    print(f"Area: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}\n")