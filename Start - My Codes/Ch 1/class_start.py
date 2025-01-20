# Python Object-Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ('HORROR', 'COMEDY', 'SCIENCE')

    # TODO: double-underscore properties are hidden from other classes
    __book_list = None

    # TODO: create a class method
    @classmethod
    def get_book_type(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def get_book_list():
        if Book.__book_list is None:
            Book.__book_list = []
        return Book.__book_list

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, book_type):
        self.title = title
        if book_type not in Book.BOOK_TYPES:
            raise ValueError(f'{book_type} is not a valid book type!')
        else:
            self.book_type = book_type


# TODO: access the class attribute
print(Book.BOOK_TYPES)


# TODO: Create some book instances
b1 = Book('fear of god', 'HORROR')
b2 = Book('the quick brown fox', 'COMEDY')
print(b1.title)
print(b1.book_type)
# b3 = Book('the lazy', 'IDK')

# TODO: Use the static method to access a singleton object
the_books_list = Book.get_book_list()
print(the_books_list)
the_books_list.append(b1)
the_books_list.append(b2)
print(the_books_list)
