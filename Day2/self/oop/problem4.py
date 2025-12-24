"""
WAP to create a class where user enters amount in inr,then ask user to which currency 
he/she want to convert to (Dollar,Euro,Pound,Ruble,etc) and print the converted amount.
create fn in class for each currency.
"""

class CurrencyConverter:
    def __init__(self,amount:int,currency:int):
        self.amount=amount
        #Currency change is as 1.Euro 2.Dollar 3.Pound 4.Ruble
        self.currency=currency

    def dollar_change(self)->float:
        return self.amount/83
    
    def euro_change(self)->float:
        return self.amount/90
    
    def pound_change(self)->float:
        return self.amount/105
    
    def ruble_change(self)->float:
        return self.amount*0.90
    
    def convertor(self):
        convert_chart={1:self.dollar_change(),2:self.euro_change(),3:self.pound_change(),4:self.ruble_change()}
        fn=convert_chart.get(self.currency)
        if fn:
            return fn
        return "Invalid input"

amount=int(input("Enter the amount:\t"))
n=int(input("Enter the conversion you want as 1.Dollar 2.Euro 3.Pound 4.Ruble:\t"))
x=CurrencyConverter(amount,n)  
print(x.convertor())
