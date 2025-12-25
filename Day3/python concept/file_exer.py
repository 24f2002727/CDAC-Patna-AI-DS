def store_details(name:str, age:str, phoneNum:str):
    f = open(f"{name}.txt", "w")

    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}\n")
    f.write(f"Phone No.: {phoneNum}\n")

    f.close()

def get_details(name:str):

    f = None

    try:
        f = open(f"{name}.txt", "r")
        content:str = f.read()
        print("user record Found!\n")
        print(content)

    except FileNotFoundError:
        print("User record not found")

    finally:

        if f:
            f.close()

def init_store():  
    name:str = input("Enter Name: ").strip()
    age:str = input("Enter age: ").strip()
    num:str = input("Enter phone number: ").strip()

    if not name.isalpha():
        print("Name must contain only letter")
        exit(-1)

    if not age.isdecimal():
        print("Age is not a number")
        exit(-1)

    if not num.isdecimal():
        print("Phone number is not a number")
        exit(-1)

    store_details(name, age, num)

def init_get_details():
    name:str = input("Enter Name: ").strip()
    get_details(name)

if __name__ == "__main__":
    
    init_get_details()