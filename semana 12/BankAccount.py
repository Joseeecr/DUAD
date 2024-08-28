class BankAccount:

    def __init__(self):
        self.balance = 0

    def send_money_to_account(self, amount):
        if amount > 0:
            self.balance += amount
            print(self.balance)
        else:
            print("Negative numbers are not allowed")

    def take_out_money(self, amount):
        if amount > self.balance or amount < 0:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(self.balance)


class SavingsAccount(BankAccount):
    min_balance = 100

    def take_out_money(self, amount):
        if self.balance < SavingsAccount.min_balance:
            print("Your current balance is less thant the minimum balance!")
        else:
            self.balance -= amount
            print(self.balance)


jose = SavingsAccount()
jose.take_out_money(100)
jose.send_money_to_account(1000)
jose.take_out_money(1000)
jose.take_out_money(1000)