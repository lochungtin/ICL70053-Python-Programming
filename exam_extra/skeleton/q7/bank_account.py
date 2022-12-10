class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount


