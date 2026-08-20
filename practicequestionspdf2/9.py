class LibraryMember:
    total_members=0
    limit=6
    def __init__(self,name,book_borrowed):
        self.name=name
        self.book_borrowed=book_borrowed
        LibraryMember.total_members+=1
    def borrowed_books(self,title,qty):
        if self.valid(title):
            k=self.book_borrowed+qty
            if k<=LibraryMember.limit:
                self.book_borrowed+=qty
                print(f"borrowed books are: {self.book_borrowed}")
            else:
                print("Exceed books")
        else:
            print("title was too small")
    @classmethod
    def update(cls,up):
        cls.limit=up
    @staticmethod
    def valid(title):
        return len(title)>5

l1=LibraryMember("shivani",4)
l1.borrowed_books("hjkdcv",2)
LibraryMember.update(4)
