# Q1. Student Result Manager - Encapsulation

class Student:
    def __init__(self, name, marks):
        self.name = name              # Public attribute
        self._marks = 0               # Protected attribute (convention)
        self.__grade = "F"            # Private attribute (name-mangled)
        self.set_marks(marks)

    def set_marks(self, marks):
        if not isinstance(marks, (int, float)) or isinstance(marks, bool):
            print("Invalid marks: enter a number from 0 to 100.")
            return False
        if not 0 <= marks <= 100:
            print("Invalid marks: marks must be between 0 and 100.")
            return False

        self._marks = marks
        if marks >= 80:
            self.__grade = "A"
        elif marks >= 60:
            self.__grade = "B"
        elif marks >= 40:
            self.__grade = "C"
        else:
            self.__grade = "F"
        return True

    def get_marks(self):
        return self._marks

    def get_grade(self):
        return self.__grade


if __name__ == "__main__":
    student1 = Student("Ayesha", 85)
    student2 = Student("Hamza", 35)

    print(f"{student1.name}: marks={student1.get_marks()}, grade={student1.get_grade()}")
    print(f"{student2.name}: marks={student2.get_marks()}, grade={student2.get_grade()}")

    print("\\nUpdating Ayesha's marks to 92:")
    student1.set_marks(92)
    print(f"Updated result: {student1.get_marks()}, grade={student1.get_grade()}")

    print("\\nTrying invalid marks (125):")
    student1.set_marks(125)
    print(f"Result remains: {student1.get_marks()}, grade={student1.get_grade()}")

    try:
        print(student1.__grade)
    except AttributeError:
        print("Direct access to __grade failed: it is name-mangled by Python.")
    print("The attribute can technically be accessed as _Student__grade, so this is not true security.")
