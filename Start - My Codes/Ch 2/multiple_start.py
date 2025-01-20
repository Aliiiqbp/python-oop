# Python Object-Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.common = 'common attr A'


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.common = 'common attr B'


class C(A, B):
    def __init__(self):
        super().__init__()
        # self.common = 'common attr C'

    def show_prop(self):
        print(self.prop1)
        print(self.prop2)
        print(self.common)


# Resolution Order:
# python will look in the order of classes.
# First the class itself, then the father's class
# in the same order that they have been inherited from, first A and then B, in this example
c = C()
c.show_prop()

# find the resolution order
print(C.__mro__)
