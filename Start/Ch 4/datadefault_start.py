# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes
import random
from dataclasses import dataclass, field


def price_func():
    return random.randrange(10, 30)


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = 'No Title'
    author: str = 'No Author'
    pages: int = 0
    price: float = field(default_factory=price_func)


b1 = Book()
b2 = Book()
print(b1)
print(b2)
