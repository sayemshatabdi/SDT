class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.maxwithdraw = 100000
        self.minbalance = 500

    def get_balance(self):
        print( self.balance)
    def deposit(self, amount):
        if amount>0 :
            self.balance += amount
            print(f'Deposited {amount} successfully. New balance is {self.balance}.')

    def withdraw(self, amount):
        if amount> self.maxwithdraw:
            print(f'You can not withdraw more than {self.maxwithdraw}.')
        elif amount < self.minbalance:
            print(f'You can not withdraw less than {self.minbalance}.')
        elif amount > self.balance:
            print(f'You can not withdraw more than your balance {self.balance}.')   
        else:
            self.balance -= amount
            print(f'Withdrew {amount} successfully. New balance is {self.balance}.')
        
brac= Bank(100000)

brac.get_balance()
brac.deposit(500)
brac.get_balance()
brac.withdraw(2000)
brac.get_balance()
brac.withdraw(10)
