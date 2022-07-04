from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


dict_person = {"name": "Улан", "age": 16}
object_person = Person(**dict_person)
print(object_person)
print(object_person.name, object_person.age)
