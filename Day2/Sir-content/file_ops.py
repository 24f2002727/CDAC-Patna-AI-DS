
# open(file_name:str, mode:str)

def file_write():
    f = open("text.txt", "w")

    num:int = f.write("hello\n")
    print(num)
    f.writelines(["lin1\n", "line2\n"])

    f.close()

def file_read():
    f = open("text.txt", "r")

    con = f.read(6)
    print(con)

    f.readline()

    f.close()

def with_file_read():

    with open("text.txt", "r") as f:
        con:str = f.readlines()
        print(con)


if __name__ == "__main__":
    # file_write()
    # file_read()
    with_file_read()