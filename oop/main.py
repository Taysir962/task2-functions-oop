
# oop/main.py
from bank_account import BankAccount
from course import Student, Course

def transfer(from_acc, to_acc, amount):
    """Transfers money from one account to another, catching ValueError and returning True or False."""
    try:
        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    print("=== Testing Bank Transfer and Imports ===")
    
    acc1 = BankAccount("Ali", 200)
    acc2 = BankAccount("Omar", 50)
    
    print("Before transfer:")
    print(acc1)
    print(acc2)
    
    print("-" * 30)
    
    success_transfer = transfer(acc1, acc2, 70)
    print("Transfer 70 successful?:", success_transfer)
    print(acc1)
    print(acc2)
    
    print("-" * 30)
    
    failed_transfer = transfer(acc2, acc1, 500)
    print("Transfer 500 successful?:", failed_transfer)
    print("After failed transfer state remains safe.")