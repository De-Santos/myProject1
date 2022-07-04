class Ppoint():
    def __init__(self):
        self._a = 12345
        self.__b = 0
        self.q = 123

    def __Input_value(string):
        print("dfghj")
        while True:
            c = input(string)
            if c.isdigit():
                return int(c)

    def setCords(self):
        self._a = Ppoint.__Input_value(string="введите значение a: ")
        self.__b = Ppoint.__Input_value(string="введите значение b: ")

    def giv_info(self):
        print(self._a)
        print(self.__b)

    def qwer(x):
        print("sdfghjk")



pt = Ppoint()


class Das:
    def __init__(self):
        self.p = 10
    def output(self):
        print(self.p)

class Was(Das and Ppoint):
    pass


w = Was()
print(w)
w.qwer()
# print(w.Das.output())

# print(pt.setCords())
# print(pt.giv_info())

#
# print(Ppoint._Ppoint__qwer(2))
#
# print(pt._Ppoint__a)
#
