"""
WAP for calculator using class,operation to perform : Add, subtract, multiplicatiion, division.
The class will take two argument and both needs to be a no.
"""
class Calculator:
    def __init__(self,a:int,b:int):
        self.num1=a
        self.num2=b

    def add(self)->int:
        return self.num1+self.num2
    
    def subtract(self)->int:
        return self.num1-self.num2
    
    def multiply(self)->int:
        return self.num2*self.num1
    
    def divide(self):
        try:
            return self.num1/self.num2
        except ZeroDivisionError:
            return("Number can't divide by zero")

x=Calculator(5,0)
print(x.add())
print(x.subtract())
print(x.multiply())
print(x.divide())
