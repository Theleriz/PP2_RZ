class Account:
    balance = 0

    def __init__(self, owner:str = 'null'):
        self.owner = owner

    def deposit(self, value:int = 0):
        self.balance += value

    def withdraw(self, value:int = 0):
        if self.balance >= value:
            self.balance -= value
        else:
            print('Not enough balance to withdraw.')

pepe = Account('Pepe')
pepe.deposit(1000)
pepe.withdraw(500)
print(pepe.balance)