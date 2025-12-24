class Student:

    def __init__(self, name):
        self.__name = name

    def __print_name(self):
        print("Name:", self.__name)

    def print_dup(self):
        self.__print_name()


if __name__ == "__main__":

    s:Student = Student("Karan")
    s.print_dup()
    # s.__name = "Suresh"
    # s.print_name()