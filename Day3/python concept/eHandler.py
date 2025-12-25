def divideByZero(a:int, b:int):
    r = a/b 
    print(r)


def divideByZeroHandled(a:int, b:int):

    try:
        r = a/b 
        print(r)
    except ZeroDivisionError:
        print("Division by zero is not allowed")

def divideByZeroHandled_Finally(a:int, b:int):

    try:
        r = a/b 
        print(r)
    except ZeroDivisionError:
        print("Execption happened")
    except Exception as e:
        print(e)
    finally:
        print("Execution of function is done")

def try_with_finally():

    try:
        print("In try block")
    finally:
        print("In finally block")

def generic_exception_handler():

    try:
        print("Try block")
    except:
        print("Except block")
    

if __name__ == "__main__":
    num1:int = None
    num2:int = None
    num1_str:str = input("Enter 1st number: ")

    if num1_str.isdecimal():
        num1 = int(num1_str)
    else:
        print("Invalid Input")
        exit(1)

    num2_str:str = input("Enter 2nd number: ")



    # divideByZero(num1, num2)
    # divideByZeroHandled(num1, num2)
    divideByZeroHandled_Finally(num1, num2)

