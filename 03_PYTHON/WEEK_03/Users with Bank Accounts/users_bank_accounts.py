print("connected")

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    # def deposit(self, amount):
    #     self.balance = self.balance + amount
    #     return self

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

#--------------

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.balance = self.account.balance + amount
        print(f"New Balance:{self.account.balance}")
        return self
    
    def make_withdrawal(self,amount):
        if BankAccount.can_withdraw(self.account.balance,amount):
            self.account.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account.balance -= amount
            self.account.balance -= 5
        return self
    
    # def example_method(self):
    #     self.account.balance.deposit(100)
    #     print(self.account.balance)
    #     return self

    def user_display_balance(self):
        print(self.name)
        print(self.email)
        print(self.account.balance)

print("----------")
user_01_Ashley = User("Ashley", "ashley@gmail.com")
user_01_Ashley.user_display_balance()
print("----------")
user_01_Ashley.make_deposit(100)
user_01_Ashley.user_display_balance()
print("----------")
user_01_Ashley.make_withdrawal(110)
user_01_Ashley.user_display_balance()
print("----------")




