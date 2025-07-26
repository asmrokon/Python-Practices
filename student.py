class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):

        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ").title().strip()
    house = input("House: ").title().strip()
    student = Student(name, house)
    return student


main()
