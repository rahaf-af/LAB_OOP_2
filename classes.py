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
    