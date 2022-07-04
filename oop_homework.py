import math

pi = math.pi


def correct_input(strings) -> int:
    while True:
        variables = input(strings)
        if variables.isdigit():
            return int(variables)


class Figures():
    def area(self):
        pass


class Circle(Figures):
    def __init__(self, rad):
        self.__rad = rad

    def __area__(self) -> float:
        return pi * (self.__rad ** 2)


class Square(Figures):
    def __init__(self, side):
        self.__side = side

    def __area__(self) -> int:
        return self.__side ** 2


class Triangle(Figures):
    def __init__(self, side, height):
        self.__side = side
        self.__height = height

    def __area__(self) -> int:
        return 0.5 * self.__side * self.__height


if __name__ == '__main__':  # todo  Are you gay? No i'm monkey!( NIGGER)
    obj_circle = Circle(correct_input("input rad: "))
    print("Circle",obj_circle.__area__())
    obj_square = Square(correct_input("input side: "))
    print("Square",obj_square.__area__())
    obj_triangle = Triangle(correct_input("input side: "), correct_input("input height: "))
    print("Triangle",obj_triangle.__area__())
