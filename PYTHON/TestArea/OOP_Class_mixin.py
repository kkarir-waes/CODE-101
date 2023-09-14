class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        print(f'Height : {self.height}')
        print(f'Width  : {self.width}')

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)

s1 = Square(20)   
print(s1.area())
