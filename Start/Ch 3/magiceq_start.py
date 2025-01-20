# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} - {self.author} - {self.price}"

    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f'{other} must be of type Book')
        return (self.title == other.title and
                self.author == other.author and
                self.price == other.price)

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f'{other} must be of type Book')
        return self.price >= other.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f'{other} must be of type Book')
        return self.price < other.price
    ''' so basically we have all 4 combination of
    gt (greater than), lt (less than), ge (greater than or equal), le (less than or equal)
    functions and we can define all 4 of them to compare two objects'''


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
print(b1 == b3)
print(b1.__eq__(b3))

# TODO: Check for greater and lesser value
print(b1 >= b2)
print(b3 < b4)

# TODO: Now we can sort them too
book_list = [b1, b2, b3, b4]
book_list.sort()
for bk in book_list:
    print(bk)

