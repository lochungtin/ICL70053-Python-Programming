from q7 import CashAccount

from bank_account import BankAccount

def example_bank_account_usage():
    """ This is just an example of how you can use the provided BankAccount class """
    print("BankAccount example usage")
    initial_balance = 1000.0
    account = BankAccount(initial_balance)
    print(account.balance)
    account.deposit(10.0)
    print(account.balance)
    account.withdraw(20.0)
    print(account.balance)
    print("End of BankAccount example usage\n")


def test_simulation():
    initial_balance = 1000.0
    print(f"Creating a new cash account in October with an initial balance of £{initial_balance}.")
    account = CashAccount(initial_balance)
    
    print("User makes 10 deposits of £10 each in October...")
    for i in range(10):
        account.deposit(10.0)
    print(f"Balance after the 10 deposits: £{account.balance}")
    assert account.balance == 1100.0

    print("User makes 10 withdrawals of £100 each in October...")
    for i in range(10):
        account.withdraw(100.0)
    print(f"Balance after the 10 withdrawals: £{account.balance}")
    assert account.balance == 100.0
    
    print("The bank deducts its service fee at the end of October")
    account.deduct_monthly_fees()
    print(f"Balance after deduction: £{account.balance}")
    assert account.balance == 94.0

    account.deduct_monthly_fees()  # should not deduct any fee.
    print(f"Starting balance in November: £{account.balance}")
    assert account.balance == 94.0

    print("User makes 4 withdrawals of £10 each in November...")
    for i in range(4):
        account.withdraw(10.0)
    print(f"Balance after the 4 withdrawals: £{account.balance}")
    assert account.balance == 54.0

    print("The bank deducts its service fee at the end of November")
    account.deduct_monthly_fees() # should not deduct any fee,
    print(f"Balance after deduction: £{account.balance}")
    assert account.balance == 54.0


if __name__ == "__main__":
    #example_bank_account_usage()
    test_simulation()

