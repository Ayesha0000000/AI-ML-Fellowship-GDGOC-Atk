class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance   # Encapsulation

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def __str__(self):
        return f"Account Holder: {self.owner}, Balance: {self._balance}"


class SavingsAccount(BankAccount):   # Inheritance
    def add_interest(self, rate):
        interest = self._balance * rate
        self._balance += interest
        print(f"Interest added: {interest}")


# Testing
acc = SavingsAccount("Ayesha", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.add_interest(0.05)
print(acc)
