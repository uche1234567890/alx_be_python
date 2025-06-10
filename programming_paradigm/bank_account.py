# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.__account_balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current balance: ₦{self.__account_balance:.2f}")
