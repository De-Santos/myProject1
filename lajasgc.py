from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


p1 = Person("John", 36)
p1.age
print(p1.name, p1.age)
