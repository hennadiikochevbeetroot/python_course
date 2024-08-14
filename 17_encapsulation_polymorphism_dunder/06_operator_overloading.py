from __future__ import annotations  # for using class name in its methods typehints


class Rectangle:
    def __init__(self, side1: int, side2: int):
        self.side1 = side1
        self.side2 = side2

    @property
    def area(self):
        return self.side1 * self.side2

    # self - first argument, other - second, operator +
    def __add__(self, other: Rectangle) -> int:
        return self.area + other.area

    # self - first argument, other - second, operator -
    def __sub__(self, other: Rectangle) -> int:
        return self.area - other.area

    # self - first argument, other - second, operator *
    def __mul__(self, other: Rectangle) -> int:
        return self.area * other.area

    # self - first argument, other - second, operator /
    def __truediv__(self, other: Rectangle) -> int | float:
        return self.area / other.area

    # self - first argument, other - second, operator //
    def __floordiv__(self, other: Rectangle) -> int | float:
        return self.area // other.area

    # abs function overload
    def __abs__(self) -> int:
        return abs(self.area)

    # self - first argument, other - second, operator >
    def __gt__(self, other: Rectangle) -> bool:
        return self.area > other.area

    # self - first argument, other - second, operator >=
    def __ge__(self, other: Rectangle) -> bool:
        return self.area >= other.area

    # self - first argument, other - second, operator <
    def __lt__(self, other: Rectangle) -> bool:
        return self.area < other.area

    # self - first argument, other - second, operator <=
    def __le__(self, other: Rectangle) -> bool:
        return self.area <= other.area

    # self - first argument, other - second, operator ==
    def __eq__(self, other: Rectangle) -> bool:
        return self.side1 == other.side1 and self.side2 == other.side2

    # self - first argument, other - second, operator !=
    def __ne__(self, other: Rectangle) -> bool:
        return self.side1 != other.side1 or self.side2 != other.side2

    # bool function call
    def __bool__(self) -> bool:
        return self.side1 > 0 and self.side2 > 0

    # len function call
    def __len__(self):
        return max(self.side1, self.side2)


r1 = Rectangle(3, 4)
r2 = Rectangle(2, 5)
print('Sum:', r1 + r2)
print('Sum:', r1.__add__(r2))

# All others work in same way
