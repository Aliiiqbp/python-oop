# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints
import math
from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return format(self.radius * self.radius * math.pi, '.2f')


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


# g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
