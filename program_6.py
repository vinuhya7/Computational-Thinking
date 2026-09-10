from dataclasses import dataclass


# Traditional Class
class Student:
    def __init__(self, name: str, age: int, marks: float) -> None:
        self.name = name
        self.age = age
        self.marks = marks

    def __repr__(self) -> str:
        return f"Student({self.name}, {self.age}, {self.marks})"


# Dataclass
@dataclass
class Employee:
    name: str
    age: int
    salary: float


# Objects
s = Student("vinuhya", 21, 85.5)
e = Employee("arithi", 25, 45000.0)

print("Traditional Class:", s)
print("Dataclass:", e)