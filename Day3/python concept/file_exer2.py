def copy_file(src:str, dst:str):
    with open(f"{src}.txt", "r") as srcf:
        with open(f"{dst}.txt", "w") as dstf:

            s_con:str = srcf.read()

            dstf.write(s_con)

if __name__ == "__main__":

    src:str = input("Enter source file: ")
    dst:str = input("Enter destination file: ")

    copy_file(src, dst)