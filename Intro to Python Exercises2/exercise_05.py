class BankAccount:
    def __init__(self,account_name,starting_balance):
        self.account_name=account_name
        self.balance=starting_balance
    def deposit(self, amount):
        self.balance +=amount
    def withdraw(self, amount):
        self.balance -=amount
    def get_balance(self):
        return "{} has a balance of {}".format(self.account_name,self.balance)
account=BankAccount("Riley Jenkins",5000)
account.deposit(1)
account.withdraw(500)
print(account.get_balance())