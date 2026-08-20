class Book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        Book.total_books+=1
    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split("-")
        if Book.is_valid_title(title):
            b=Book(title,author)
            return b
        else:
            print("Invalid title")
    @staticmethod
    def is_valid_title(title):
        return len(title)>=3

b1=Book.from_string("theship-author")
b2=Book.from_string("th-ontghe")
print(b1.title)
print(Book.from_string(f"{b2.title}-{b2.author}"))
print(f"total book: {Book.total_books}")

