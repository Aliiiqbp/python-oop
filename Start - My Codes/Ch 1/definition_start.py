# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions
# TODO: create a basic class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# TODO: create instances of the class
book1 = Book("brave new world", "ali ghorbanpour")
book2 = Book("how to cook with love", "ladan yeganeh rad")

# TODO: print the class and property
print(book1)
print(book2)
print('title:', book1.title)
print('author:', book1.author)
print('title:', book2.title)
print('author:', book2.author)
