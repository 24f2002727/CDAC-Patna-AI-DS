def file_handler(n):
    if n==1:
        username=input("Enter the username data:\n")
        name=input("enter the name :")
        age=input("Enter the age :")
        state=input("Enter the state :")
        with open(f'{username}.txt','a') as file:
            file.write(f"Name : {name}\n")
            file.write(f"Age : {age}\n")
            file.write(f"State : {state}\n")

    elif n==2:
        username=input("Input the username\n")
        try:
            with open(f'{username}.txt','r') as file:
                data=file.readlines()
                for line in data:
                    print(line)
        except:
            print("File not exist")

if __name__=="__main__":
    while(True):
        n=int(input("Enter 1 for storing data or enter 2 for search the data or press 0 for exit:"))
        if n==0:
            break
        elif n==1 or n==2:
            file_handler(n)
        else:
            print("enter valid input")