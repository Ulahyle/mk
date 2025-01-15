import json

class Users:
    def __init__ (self, User_id, Name, Family):

        self.user_id = User_id
        self.name = Name
        self.family = Family
    
    def create_user(self):

        with open("Users.json", "r") as file:

        self.user_id = json.load(file)[User]

        




class BankAccount:
        
    def __init__ (self, Owner_name, balance=0.0): 

        self.owner_name = Owner_name
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount
        print(self.balance)

    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient funds")

        else:
            self.balance -= amount
            print(self.balance)

my_account = BankAccount("ali", 1000)
my_account.deposit(2000)
my_account.withdraw(2000)