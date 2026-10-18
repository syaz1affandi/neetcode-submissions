class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
aliceAcc = BankAccount("Alice", 1000)
bobAcc = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
print(f"{aliceAcc.name}'s balance: ${aliceAcc.balance}")
print(f"{bobAcc.name}'s balance: ${bobAcc.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")