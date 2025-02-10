class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side



square = Square(10)
print(f"Площадь квадрата: {square.area()}")

shape = Shape()
print(f"Площадь фигуры (Shape): {shape.area()}")