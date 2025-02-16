from classes import BankAccount

try:
    account1=BankAccount("rahaf ahmed",100000000)
    account2=BankAccount("mohammed")

    print(account1.get_account_holder())
    print(account2.get_account_holder())

    account1.deposit(2000)
    account2.deposit(2000)

    print(account1.get_balance())
    print(account2.get_balance())

    account1.withdraw(300)
    account2.withdraw(2000)

except Exception as e:
    print(e)