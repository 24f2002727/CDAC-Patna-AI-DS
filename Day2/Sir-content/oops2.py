class Animal:

    def __init__(self, name):
        self.__name = name
    
    def info(self):
        print("Name is:", self.__name)

class Dog(Animal):
    
    def sound(self):
        # should not access in real world programs
        print(self._Animal__name, "barks")

if __name__ == "__main__":

    d:Dog = Dog("Rocky")
    d.info()
    d.sound()

    