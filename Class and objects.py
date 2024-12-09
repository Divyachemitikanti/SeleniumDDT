class BankAccount:
    def __init__(self,account_holder,balance =0):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited ${amount}.New balence:${self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print(f"insufficient funds!Current balance:${self.balance}")
        else:
            self.balance-=amount
            print(f"withdraw ${amount}.new balance:${self.balance}")

#create an object of BankAccount
account=BankAccount(account_holder="Divya",balance=200000)

account.deposit(50000)
account.withdraw(20000)





