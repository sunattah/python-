class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          
        self.balance = balance  
            
    def deposit(self, amount):
        self.balance += amount
        self.print_receipt()        
        
    def print_receipt(self):
        print(f"{self.owner}: {self.balance}")

account = BankAccount("Alice", 100) 
account.deposit(50)               