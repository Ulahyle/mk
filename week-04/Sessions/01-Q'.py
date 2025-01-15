class Book:
   def __init__(self, name, page, number):
      self.name = name
      self.page = page
      self.number = number
      

class Library:
  def __init__(self):
    self.db = {} 

  def add_book(self, book):
    self.db[book.name] = book 

  def get_book(self, book_name, amount):
    if book_name in self.db and amount > 0 and self.db[book_name].number >= amount:
      self.db[book_name].number -= amount
      return amount
    else:
      raise "invalid amount!"

  def return_book(self, book_name, amount):
   
    if book_name in self.db:
      self.db[book_name].number += amount
    else:
      print(f"Book '{book_name}' not found in the library.")​
کتاب کلاس:     def __init__(خود، نام، صفحه، شماره):        self.name = نام        self.page = صفحه        خود.شماره = عدد         کتابخانه کلاس:    def __init__(self):      self.db = {}      def add_book (خود، کتاب):      self.db[book.name] = کتاب      def get_book (خود، نام_کتاب، مقدار):      if book_name در self.db و مقدار > 0 و self.db[book_name].number >= مقدار:        self.db[book_name].number -= مقدار        مبلغ برگشتی      دیگر:        افزایش "مقدار نامعتبر!"     def return_book (خود، نام_کتاب، مبلغ):          if book_name در self.db:        self.db[book_name].number += مقدار      دیگر:        print(f"کتاب '{book_name}' در کتابخانه یافت نشد.").
