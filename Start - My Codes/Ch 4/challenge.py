# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: implement a dataclass

# Challenge: convert your classes to dataclasses
# The subclasses are required to override the magic method
# that makes them sortable
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Asset(ABC):
    price: float

    @abstractmethod
    def __lt__(self, other):
        pass
    
@dataclass
class Stock(Asset):
    shorten: str
    name: str

    def __lt__(self, other):
        return self.price < other.price

@dataclass
class Bond(Asset):
    desc: str
    years: int
    matyield: float

    def __lt__(self, other):
        return self.matyield < other.matyield


# ~~~~~~~~~ TEST CODE ~~~~~~~~~
stocks = [
    Stock(shorten="MSFT", price=342.0, name="Microsoft Corp"),
    Stock(shorten="GOOG", price=135.0, name="Google Inc"),
    Stock(shorten="META", price=275.0, name="Meta Platforms Inc"),
    Stock(shorten="AMZN", price=120.0, name="Amazon Inc")
]

bonds = [
    Bond(95.31, "30 Year US Treasury", 30, 4.38),
    Bond(96.70, "10 Year US Treasury", 10, 4.28),
    Bond(98.65, "5 Year US Treasury", 5, 4.43),
    Bond(99.57, "2 Year US Treasury", 2, 4.98)
]

try:
   ast = Asset(100.0)
except:
   print("Can't instantiate Asset!")

stocks.sort()
bonds.sort()

for stock in stocks:
   print(stock)
print("-----------")
for bond in bonds:
   print(bond)
