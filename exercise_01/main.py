from BankAccount import BankAccount
if __name__ == "__main__":
    account = BankAccount("Jared", 1000000)
    account.deposit(350000)
    account.withdraw(500000)
    print(account.get_balance())