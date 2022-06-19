class Student:

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def show(self):
        print(f"student name : {self.name}")
        print(f"student age : {self.age}")
        print(f"student score : {self.score}")


if __name__ == '__main__':
    std1 = Student("Razicodes", 29, 990)
    std2 = Student("Alex", 50, 1000)
    std3 = Student("Gautam", 89, 999)

    std1.show()
    std2.show()
    std3.show()


