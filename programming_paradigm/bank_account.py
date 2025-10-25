class BankAccount:

    def __init__(self, initial_balance = 0):
        # Encapsulated attribute (account balance)
        self.account_balance = initial_balance

    def deposit(self, amount):
        #Add money to the account.
        self.account_balance += amount

    def withdraw(self, amount):
        #Withdraw money from account
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        #Show the current balance.
        print(f"Current Balance: ${self.account_balance:.2f}")