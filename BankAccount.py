#TASK 3

class BankAccount:
    owner=""
    balance=""
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.owner, "deposited PKR", amount, "| Your Balance: PKR", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        if amount <= self.balance:
            print("You have withdrawed:",amount, "| Your New Balance: PKR", self.balance)
        else:
            print("You have insufficent balance", self.balance)

acc1 = BankAccount("Hasnain", 150000)
acc2 = BankAccount("Rehman", 180000)

acc1.deposit(50000)
acc1.withdraw(35000)
acc2.deposit(250000)
acc2.withdraw(50000)

