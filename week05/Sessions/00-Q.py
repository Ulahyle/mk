class BankAccount:
    bank_name = "Python Bank"

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if self.is_valid_amount(amount):
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Invalid amount. Please enter a positive number.")

    def withdraw(self, amount):
        if not self.is_valid_amount(amount):
            print("Invalid amount. Please enter a positive number.")
            return

        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Current balance: {self.balance}")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"Bank name changed to {cls.bank_name}.")

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        print(f"Interest amount based on the current balance: {interest}")
        return interest


if __name__ == "__main__":
    account = BankAccount("ali", 11)
    print(f"Welcome to {account.bank_name}, {account.account_holder}!")
    account.deposit(1)
    account.withdraw(1)
    account.display_balance()


    BankAccount.change_bank_name("C Bank")
    print(f"New bank name is: {BankAccount.bank_name}")


    savings = SavingsAccount("ali", 1, 2)
    print(f"Welcome to {savings.bank_name}, {savings.account_holder}!")
    savings.calculate_interest()
    savings.deposit(1)
    savings.withdraw(1)
    savings.display_balance()
