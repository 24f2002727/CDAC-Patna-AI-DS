"""
Docstring for day1.oop.prob2
Create a account class with 2 attribute - balance and account no and create methods for debit
credit and printing the balance.If balance amount is less than equal to 0 do not let debit
"""
class Account:
    def __init__(self,acc_no:int,balance:float):
        self.acc_no=acc_no
        self.balance=balance

    def debit(self,amount:int)->str:
        if self.balance<amount:
            return"Not suffficient amount"
        else:
            self.balance=self.balance-amount
            return f"Account debited with {amount}"

    def credit(self,amount:int)->str:
        self.balance+=amount
        return f"Account credited with {amount}"

    def balance_info(self)->str:
        return(f'The balance for {self.acc_no} is {self.balance}')
            

ram=Account(1,100)
print(ram.debit(50))
print(ram.credit(100))
print(ram.balance_info())
print(ram.debit(500))
