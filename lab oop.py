from classes import BankAccount
account1=BankAccount("rahaf ahmed",100000000)
account2=BankAccount("mohammed")

print(account1.get_account_holder())
print(account2.get_account_holder())

account1.deposit(2000)
account2.deposit(2000)

print(account1).getba