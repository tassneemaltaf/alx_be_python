class BankAccount():
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance < amount:
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        print("Your current account balaance is: ", self.account_balance)

