print("connected")

class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
        
    def yield_interest(self):
        pass

# Users
user_account_01 = BankAccount(.01, 350)
user_account_02 = BankAccount(.01, 500)

# your code here

user_account_01.deposit(500).deposit(100).deposit(50).withdraw(100).display_account_info()
user_account_02.deposit(500).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).display_account_info()

