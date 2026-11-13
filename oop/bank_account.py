
class BankAccount:
    """A class representing a Bank Account with owner, balance, and transaction history."""
    
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance
        self.history = [f"Account created with balance: {balance}"]

    def deposit(self, amount):
        """Deposits a positive amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.balance += amount
        self.history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        """Withdraws an amount if balance is sufficient."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Withdrawal amount is larger than the balance.")
        self.balance -= amount
        self.history.append(f"Withdrew: {amount}")

    def __str__(self):
        """Returns string representation of the bank account."""
        return f"BankAccount(Owner: {self.owner}, Balance: {self.balance})"


if __name__ == "__main__":
    print("=== Testing BankAccount Class ===")
    
    acc = BankAccount("Sara", 100)
    print(acc)
    
    acc.deposit(50)
    acc.withdraw(30)
    print(acc)
    print("Transaction History:", acc.history)
    
    print("-" * 30)

    try:
        acc.withdraw(500)  # أكبر من الرصيد
    except ValueError as e:
        print("Caught expected ValueError:", e)