class Book:
    def __init__ (self, name, page, number):
        self. name = name
        self. page = page
        self. numbe = number





class Library:
        
    def __init__ (self, Book_name, Book_avabality=0): 

        self.book_name = Book_name
        self.Book_avabality = Book_avabality

    def withdraw(self, number):

        if number > self.Book_avabality:
            print("Insufficient funds")

        else:
            self.Book_avabality -= number
            print(self.Book_avabality)

    def deposit(self, number):

        self.Book_avabality += number
        print(self.Book_avabality)


book1 = Library("Think Python", 4)

book1.deposit(2)
book1.withdraw(1)
