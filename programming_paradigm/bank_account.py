class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")


def main():
    account = BankAccount()

    # Example usage – replace or remove these for actual tests or input
    account.deposit(67)          # Deposited: $67.00
    account.withdraw(50)         # Withdrew: $50.00
    account.display_balance()    # Current Balance: $17.00
    account.withdraw(300)        # Insufficient funds.

if __name__ == "__main__":
    main()
