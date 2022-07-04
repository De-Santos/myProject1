def type_check(types):
    if type(types) == int:
        return True
    else:
        print("вы ввели неправиотное значение")
        return False


def correct_input(strings):
    while True:
        variables = input(strings)
        if variables.isdigit():
            return int(variables)


def create_house():
    length = correct_input(strings="длинна: ")

    width = correct_input(strings="ширина: ")

    height = correct_input(strings="высота: ")

    return House(length, width, height)


class House:
    def __init__(self, length, width, height):
        self.height = height
        self.width = width
        self.length = length

    def volume(self):
        return self.height * self.width * self.length

    def __eq__(self, other):
        return self.volume() == other.volume()

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __lt__(self, other):
        return self.volume() < other.volume()


print("Введите значения первого дома: ")
house1 = create_house()

print("\nВведите значения второго дома: ")
house2 = create_house()

if house1 == house2:
    print("\nsame")

if house1 > house2:
    print("house1 bigger")

if house1 < house2:
    print("second bigger")

