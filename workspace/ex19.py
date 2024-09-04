import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @property
    @abstractmethod
    def shape_name(self) -> str:
        ...

    @abstractmethod
    def calculate_area(self) -> float:
        ...


class Circle(Shape):
    def __init__(self, radius=1):
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * (self.radius ** 2)

    @property
    def shape_name(self) -> str:
        return "circle"


class Triangle(Shape):
    def __init__(self, base=1, height=1):
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        return 0.5 * self.base * self.height

    @property
    def shape_name(self) -> str:
        return "triangle"


def process_shape(shape: Shape) -> None:
    if not isinstance(shape, Shape):
        raise TypeError('Invalid type of object passed. Only Shape instances are allowed')

    area = shape.calculate_area()
    print(f'Area of {shape.shape_name} is {area} sq.units')


if __name__ == '__main__':
    t1 = Triangle(base=1.2, height=3.4)
    c1 = Circle(3.4)
    s1 = "Vinod"

    process_shape(t1)
    process_shape(c1)
    process_shape(s1)
