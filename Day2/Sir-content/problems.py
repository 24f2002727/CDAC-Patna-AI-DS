
import file_ops

def seq_lines():
    lines:list[str] = []

    while True:

        line:str = input("Enter Something: ")

        if not line:
            break

        lines.append(line)

    for line in lines:
        print(line.lower())

def is_list_palindrome():

    l:list = ["h","j","hello", "j", "h"]

    if l == l[::-1]:
        print("Yes")
    else:
        print("No")

def print_all_key_value(dictionary:dict)->None:

    for key, value in dictionary.items():

        if type(value) == dict:
            print_all_key_value(value)
        else:
            print(f"{key} : {value}")

    

if __name__ == "__main__":
    # seq_lines()
    dictionary:dict = {
        "a": 1,
        "b": 2,
        "c": {
            "a": 3,
            "b": 4,
            "c":{
                "h": 54,
                "k": 57,
                "zzz": {
                    "k":32,
                    "l":54,
                }
            }
        }
    }
    # is_list_palindrome()
    print_all_key_value(dictionary)
