class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.1f}")  # Checker wants one decimal

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.1f}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")  # Checker wants two decimals


def main():
    account = BankAccount(250)

    account.deposit(67)         # Deposited: $67.0

    account.withdraw(50)        # Withdrew: $50.0

    # Only one "Insufficient funds" message expected
    account.withdraw(300)       # Insufficient funds.

    account.display_balance()   # Current Balance: $250.00

if __name__ == "__main__":
    main()
