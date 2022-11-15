# class Dog():
#     def __init__(self, spots, size):
#         self.spots = spots
#         self.size = size

# dalmation = Dog(True, 25)
# print(dalmation.size)

class Book:
    def __init__(self, author, title, final_page, current_page = 1):
        self.author = author
        self.title = title
        self.current_page = current_page
        self.final_page = final_page

    def turn_page(self):
        self.current_page += 1

    def turn_page_back(self):
        self.current_page -= 1

    def __str__(self) -> str:
        return f"The title of this book is {self.title} and the author is {self.author}"

    def specific_page(self):
        self.current_page = input("enter the page number ")

    def bookmark(self):
        self.specific_page

    def start_again(self):
        if self.current_page >= self.final_page:
            self.current_page = 1



my_book = Book("JK Rowling", "Harry Potter", 700)
my_book.turn_page()

print(my_book.title)
print(my_book)

my_book.specific_page()
print(f"the current page number is: {my_book.current_page}")
print(f"final page:{my_book.final_page}")