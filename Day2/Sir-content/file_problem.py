import os

def store():

    name:str = input("Enter Name: ")
    age:str = input("Enter Age: ")
    state:str = input("Enter State: ")

    with open(f"{name}.txt", "w") as fp:
        fp.writelines([
                f"Name: {name}\n", 
                f"Age:{age}\n", 
                f"State:{state}\n"
            ])
        
    print("File Saved!")

def search():

    name:str = input("Enter name: ")

    if not os.path.exists(f"{name}.txt"):
        print("User not found!")
        return

    with open(f"{name}.txt") as fp:
        print("User Found:")
        print(fp.read())

def search_exp():

    name:str = input("Enter name: ")

    # if not os.path.exists(f"{name}.txt"):
    #     print("User not found!")
    #     return
    try:
        with open(f"{name}.txt", "r") as fp:
            print("User Found:")
            print(fp.read())
    except FileNotFoundError:
        print("User Not Found!")
    except Exception as e:
        print(e) # This will go in log file
        print("Something Went Wrong") # this will be given to user

opt_avail = {
                "1":store,
                "2": search_exp,
            }

if __name__ == "__main__":

    opt:str = input("Select Option:\n1. Store\n2. Search\n>>> ")

    call = opt_avail.get(opt)

    if call:
        call()
    else:
        print("Invalid Option!")