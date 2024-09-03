class BankAccount:

    def __init__(self):
        self.balance = 0

    def send_money_to_account(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Negative numbers are not allowed")

    def take_out_money(self, amount):
        if amount > self.balance or amount < 0:
            print("Insufficient funds")
        else:
            self.balance -= amount


class SavingsAccount(BankAccount):

    def __init__(self, min_balance):
        self.balance = 0
        self.min_balance = min_balance

    def take_out_money_considering_min(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            raise ValueError("You can't take out more money than the minimum")
            

    def check_balances(self):
        print(f"Balance = {self.balance} and min balance = {self.min_balance}")            
            


person = SavingsAccount(100)
person.send_money_to_account(100)
person.send_money_to_account(100)
person.check_balances()