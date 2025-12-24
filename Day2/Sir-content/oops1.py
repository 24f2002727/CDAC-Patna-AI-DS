class Student:

    def __init__(self, name:str, mark1:int, mark2:int, mark3:int):
        self.__name:str =  name
        self.__marks:list[int] = [mark1, mark2, mark3]

    def calculate_avg(self) -> float:
        return sum(self.__marks)/len(self.__marks)

if __name__ == "__main__":

    s:Student = Student("karan", 23, 24, 23)

    avg:float = s.calculate_avg()

    print(f"Avg: {avg}")
        
