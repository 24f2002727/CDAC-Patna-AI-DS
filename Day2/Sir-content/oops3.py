class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

# Child Class: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__ (name)

        # Call parent constructor
        self.breed = breed

    def details(self):
        print(self.name, "is a", self.breed)

if __name__ == "__main__":
    d = Dog("Buddy", "Golden Retriever")

    d.info() # Parent method
    d.details() # Child method