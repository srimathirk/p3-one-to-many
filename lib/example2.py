class Student:

    all = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # teacher is protected because it is not a part of the constructor
        self._teacher = None
        Student.all.append(self)

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError("Teacher must be an instance of Teacher class")
        self._teacher = value

class Teacher:
    def __init__(self, name):
        self.name = name

    def students(self):
        return [student for student in Student.all if student.teacher == self]

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of Student class")
        student.teacher = self

# Create a teacher and some students
teacher = Teacher("Alice")
student1 = Student("anu", 1)
student2 = Student("abi", 2)

# Add the grocery items to the shopper's list
teacher.add_student(student1)
teacher.add_student(student2)

# Print the shopper's grocery list

print(student1.name, student1.age)
