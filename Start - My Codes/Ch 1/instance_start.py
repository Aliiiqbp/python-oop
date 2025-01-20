# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'secret string'

    # TODO: create instance methods
    def get_price(self):
        if hasattr(self, '_discount'):
            return (1 - self._discount) * self.price
        else:
            return self.price

    def set_discount(self, discount):
        self._discount = discount

    def remove_discount(self):
        try:
            del self._discount
        except AttributeError:
            print('AttributeError: discount is not defined')


# TODO: create some book instances
b1 = Book("War and Peace", 'ali', 300, 100)
b2 = Book("The Catcher in the Rye", 'ladan', 180, 200)

# TODO: print the price of book1
print(b1.get_price())
print(b2.get_price())


# TODO: try setting the discount
b1.set_discount(0.1)
print(b1.get_price())
b1.remove_discount()
print(b1.get_price())


# TODO: properties with double underscores are hidden by the interpreter
try:
    print(b1.__secret)
except:
    print('No secret')
finally:
    print(b1.__dict__)

