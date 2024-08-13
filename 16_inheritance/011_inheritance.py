

class Figure:
    def __init__(self, side: int | float):
        self.side = side

    def calculate_area(self):
        pass

    def __str__(self):
        return f'Figure with side {self.side}'


class Rectangle:
    def __init__(self, side1: int | float, side2: int | float):
        self.side1 = side1
        self.side2 = side2

    def calculate_area(self):
        return self.side1 * self.side2

    def __str__(self):
        return f'Rectangle with side1 {self.side1}, side2 {self.side2}'


class Square(Figure, Rectangle):
    def __init__(self, side: int | float):
        Figure.__init__(self, side)
        Rectangle.__init__(self, side, side)


square = Square(5)
print(square.calculate_area())
print(square)




class Triangle(Figure):

    def __init__(self, side: int | float, height: int | float):
        super().__init__(side)
        self.side = side * 2
        self.height = height

    def calculate_area(self):
        return self.height * self.side / 2


# triangle = Triangle(3, 5)
# print(triangle.calculate_area())
