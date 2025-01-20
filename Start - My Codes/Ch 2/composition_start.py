# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price

        self.author = author
        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append((chapter.name, chapter.page_count))

    def total_page_counter(self):
        total = 0
        for ch in self.chapters:
            total += ch[1]
        return total



class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Chapter:
    def __init__(self, name, page_count):
        self.name = name
        self.page_count = page_count


author1 = Author("leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, author1)
ch1 = Chapter("Chapter 1", 125)
ch2 = Chapter("Chapter 2", 97)
ch3 = Chapter("Chapter 3", 143)
b1.addchapter(ch1)
b1.addchapter(ch2)
b1.addchapter(ch3)


# b1.addchapter("Chapter 1", 125)
# b1.addchapter("Chapter 2", 97)
# b1.addchapter("Chapter 3", 143)

print(b1.title)
print(b1.author)
print(b1.author.first_name)
print(b1.author.last_name)
print(b1.chapters)
print(b1.total_page_counter())
