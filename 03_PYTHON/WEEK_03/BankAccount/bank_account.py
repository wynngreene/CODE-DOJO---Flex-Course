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
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= amount
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
        
    def yield_interest(self):
        increase = self.balance * self.int_rate
        self.balance = self.balance + increase
        return self
    
    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
        
    @classmethod
    def all_balances(cls):
        sum = 0
        for balance in cls.balance:
            sum += balance
        return sum
        

# Users
user_account_01 = BankAccount(.01, 350)
user_account_02 = BankAccount(.01, 500)
user_account_03 = BankAccount(.01, 100)

# your code here
user_account_01.yield_interest().display_account_info()
user_account_03.withdraw(105).display_account_info()
print("-----------------")
user_account_01.deposit(500).deposit(100).deposit(50).withdraw(100).yield_interest().display_account_info()
user_account_02.deposit(500).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
print("-----------------")
