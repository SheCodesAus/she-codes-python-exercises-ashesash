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
        return self.current_page

    def turn_page_back(self):
        self.current_page -= 1
        return self.current_page

    def __str__(self) -> str:
        return f"The title of this book is {self.title} and the author is {self.author}"

    def go_specific_page(self):
        self.specific_page = int(input("enter the page number "))
        #using self.current_page does not work

    def bookmark(self):
        self.specific_page

    def start_again(self):
        if self.specific_page >= self.final_page:
            self.begin_page = 1
            return self.begin_page
        else:
            return self.current_page


my_book = Book("JK Rowling", "Harry Potter", 700)
print(my_book)
print(my_book.turn_page())

my_book.go_specific_page()
# print(f"the current page number is: {my_book.current_page}")
# print(f"final page: {my_book.final_page}")
print(f"The book starts on page: {my_book.start_again()}")