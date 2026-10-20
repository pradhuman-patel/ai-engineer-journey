class BankAccount:
    """A simple bank account with deposits and withdrawals."""

    bank_name = "Chase"

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Add money to the account."""
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """ Withdraw money from the account if sufficient funds are available."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        else:
            self.balance -= amount

a = BankAccount("Pradhuman", 100)
b = BankAccount("Alex")
a.deposit(50)
print(a.owner, a.balance)
print(b.owner, b.balance)
print(a.bank_name, b.bank_name)

a.withdraw(30)
print(a.balance)
a.withdraw(1000)