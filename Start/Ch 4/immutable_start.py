# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def tmp_func(self, new_value):
        self.value1 = new_value

# immutable class attributes can only assign at the beginning of their instantiation
obj = ImmutableClass(value1='sth new', value2=100)
print(obj.value1)
print(obj.value2)
# obj.value1 = "Value 2"
# print(obj.value1)
# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "Value 2"
# print(obj.value1)

# TODO: even functions within the class can't change anything
obj.tmp_func('ali')
