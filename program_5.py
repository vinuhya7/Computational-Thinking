from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass


class SavingsAccount(BankAccount):
    def withdraw(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")


class CurrentAccount(BankAccount):
    def withdraw(self, amount: float) -> None:
        self.balance -= amount


# Banking Management System
account: BankAccount = SavingsAccount("vinuhya", 10000)

account.deposit(2000)
account.withdraw(500)

print("Account Holder:", account.name)
print("Balance:", account.balance)