from bank_account import BankAccount


class CashAccount(BankAccount):
    def __init__(self, initial_balance=0):
        super().__init__(initial_balance)
        self.withdrawal_count = 0
        self.fee_per_transaction = 1.0

    def withdraw(self, amount):
        super().withdraw(amount)
        self.withdrawal_count += 1

    def deduct_monthly_fees(self):
        fee = max([self.withdrawal_count - 4, 0]) * self.fee_per_transaction
        super().withdraw(fee)
        self.withdrawal_count = 0
