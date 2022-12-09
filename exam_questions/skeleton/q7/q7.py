from bank_account import BankAccount

# class CashAccount(BankAccount):
#     def __init__(self, initial_balance=0):
#         super().__init__(initial_balance)
#         self.numWithdrawls = -4
#     def withdraw(self, amount):
#         super().withdraw(amount)
#         self.numWithdrawls += 1
#     def deduct_monthly_fees(self):
#         super().withdraw(max(self.numWithdrawls, 0))
#         self.numWithdrawls = -4


class CashAccount(BankAccount):
    def __init__(self, initial_balance=0):
        super().__init__(initial_balance)
        self.w = -4

    def withdraw(self, amount):
        super().withdraw(amount)
        self.w += 1

    def deduct_monthly_fees(self):
        super().withdraw(max(self.w, 0))
        self.w = -4
