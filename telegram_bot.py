class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


a = input("enter your name: ")
b = int(input("enter your age: "))
p1 = Person(a, b)

print(p1.name)
print(p1.age)
