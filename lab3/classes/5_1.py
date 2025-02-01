class Account():
    def __init__ (self, owner, balance):
        self.owner=owner
        self.balance=balance
        print(f"Owner is {self.owner} and balance is {self.balance} tenge")
    def deposit(self, add):
        self.add=add
        print(f'{self.add} tenge were added to {self.owner}\'s balance')
        self.balance+=self.add
        print(f'your balance is {self.balance} tenge')
    def withdraw(self, take):
        self.take=take
        if self.take<0:
            print("cant be negative")
        elif self.take<=self.balance:
            self.balance-=self.take
            print(f"Your balance is {self.balance} tenge")
        elif self.take<0:
            print("cant be negative")
        else:
            print("you dont have enough money")
owner=input("Tvoe imya: ")
balance=int(input("balance: "))
cash=Account(owner, balance)
while True:
    choice=input("What do u wanna do? ")
    if choice =="deposit":
        add=int(input("how much money u wanna add: "))
        if add<0:
            print("cant be negative")
            continue
        cash.deposit(add)
    if choice =="withdraw":
        take=int(input("how much money you wanna withdraw: "))
        if take<0:
            print("cant be negative")
            continue
        cash.withdraw(take)

