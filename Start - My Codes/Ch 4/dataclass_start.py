# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def book_info(self):
        return f"{self.title} by {self.author} costs {self.price}"


# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book(title='the spider man', pages=123, price=39.95, author='ali')
b4 = Book(title='the spider man', pages=123, price=39.95, author='ali')
# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
print(b3)

# TODO: comparing two dataclasses - they implement __eq__
print(b3 == b4)
print(b2 == b1)

# TODO: change some fields
b3.author = 'ladan'
b3.price = 109.3
print(b3.book_info())
