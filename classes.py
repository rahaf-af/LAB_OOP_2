class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0):
        self.__account_holder = account_holder
        self.__balance = 0
        self.deposit(balance)

    def deposit(self, amount: int):
        if not isinstance(amount, (int, float)):
            raise Exception("amount must be a number")
        if amount <= 0:
            raise Exception("Deposit amount must be positive")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount: int):
        if not isinstance(amount, (int, float)):
            raise Exception("amount must be a number")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise Exception("Insufficient funds")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.__account_holder
 
try:
    account = BankAccount("Ali", 500)
    print(f"Account Holder: {account.get_account_holder()}")
    print(f"Initial Balance: {account.get_balance()}")

    account.deposit(200)
    print(f"Balance after deposit: {account.get_balance()}")

    account.withdraw(100)
    print(f"Balance after withdrawal: {account.get_balance()}")

    account.withdraw(700)  
except Exception as e:
    print(f"Error: {e}")
