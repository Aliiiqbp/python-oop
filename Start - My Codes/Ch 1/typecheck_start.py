# Python Object-Oriented Programming by Joe Marini course example
# Checking class types and instances

class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# TODO: use type() to inspect the object type
print(type(b1))
print(type(b2))
print(type(n1))
print(type(n2))

# TODO: compare two types together
print(type(b1) is type(b2))
print(type(n1) is type(b2))

# TODO: use isinstance to compare a specific instance to a known type
print(isinstance(b1, Book))
print(isinstance(n1, Book))
# every instance of an object is an instance of its own class and the one that inherited from
# in python, all classes are inherited from the 'object' class
print(isinstance(b1, object))
