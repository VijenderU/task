class BankAccount:
    def __init__(self, account_number, balance, account_holder_name):
        self.account_number = account_number
        self.__balance = balance
        self.account_holder_name = account_holder_name

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

account = BankAccount("123456", 1000, "John Doe")
print(account.get_balance())
account.withdraw(500)
print(account.get_balance()) 
account.withdraw(1000) 
