def open_file_and_write():

    f = open("test.txt","a")
    f.write("line55\n")
    f.write("line66\n")

    f.writelines(['line77\n','line88\n'])

    f.close()

def open_file_and_read():

    f = None

    try:

        f = open("test.txt","r")

        lines = f.readlines() # read all lines
        print(lines)
    except FileNotFoundError:
        print("File does not exist")

    finally:
        if f:
            f.close()

def open_file_with():

    with open("test1.txt", "w") as f:

        f.write("line1\n")
        f.write("line2\n")

        f.writelines(['line4\n','line5\n'])

if __name__ == "__main__":
    # open_file_and_write()
    # open_file_and_read()
    open_file_with()