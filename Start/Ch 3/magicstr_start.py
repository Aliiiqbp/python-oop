# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string
    def __str__(self):
        # more user friendly and readable
        return f"{self.title} by {self.author}, costs {self.price}$"

    # TODO: use the __repr__ method to return an obj representation
    def __repr__(self):
        # more precise representation of the object including it's attributes
        return f'title: {self.title}, author: {self.author}, price: {self.price}$'


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1)
print(b1.__str__())
print(b1.__repr__())
print()
print(b2)
print(b2.__str__())
print(b2.__repr__())
