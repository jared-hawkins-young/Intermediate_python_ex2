# Bank Account class
class BankAccount:
    # constructor initialzing instance variables
    def __init__(owner, account_name, starting_balance):
        owner.account_name = account_name
        owner.balance = starting_balance

    # method to deposit money
    def deposit(owner, amount):
        # adding money
        owner.balance = owner.balance + amount
 
    # method to withdraw money
    def withdraw(owner, amount):
        # if amount is less than or equal to balance, then withdraw money
        if owner.balance >= amount:
            # withdraw money from balance
            owner.balance = owner.balance - amount
        # else
        else:
            print("Insufficient balance to withdraw")

    # getter method for balance
    def get_balance(owner):
        return str(owner.account_name)  + " has a balnce of $" + str(owner.balance)