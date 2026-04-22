#TASK 3

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.owner, "deposited PKR", amount, "| New Balance: PKR", self.balance)


acc1 = BankAccount("Hasnain", 15000)
acc2 = BankAccount("Rehman", 18000)

acc1.deposit(6000)
acc2.deposit(2500)