class BankAccount:
    
    def __init__(self, account_holder:str, balance:float=0):
        self.__account_holder=account_holder
        self.deposit(balance)=balance

    def deposit(self,amount:int):
        if not isinstance(amount,int):
            raise Exception("amount must be a number")
        self.__balance+=amount

    def withdraw(self,amount:int):
        if amount>self.__balance:

