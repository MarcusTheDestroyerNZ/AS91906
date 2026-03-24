"""The is the file for the data_manager.

This file defines the data structures for students, teachers, and
classes, as well as a DataManager class that handles loading and saving
this information from a JSON file. The DataManager class provides methods
to load student information from a file and save it back to the file when
changes are made. The Student, Teacher, and Class classes are defined using
the @dataclass decorator for simplicity and ease of use. Each class has
attributes corresponding to their respective data and methods to return
full names for students and teachers.
"""

from dataclasses import dataclass
import json


@dataclass
class Student:
    """Create a Student class to represent each student in the system.

    The Student class represents a student with an ID, first name,
    last name, and a list of classes they are enrolled in.
    """

    id: int
    first_name: str
    last_name: str
    classes: list

    def full_name(self):
        """Return the full name of the student."""
        return f"{self.first_name} {self.last_name}"


@dataclass
class Teacher:
    """Create a Teacher class to represent each teacher in the system.

    The Teacher class represents a teacher with an ID, first name,
    and last name.
    """

    id: int
    first_name: str
    last_name: str

    def full_name(self):
        """Return the full name of the teacher."""
        return f"{self.first_name} {self.last_name}"


@dataclass
class Class:
    """Create a Class class to represent each class in the system.

    The Class class represents a class with an ID, name, and the
    ID of the teacher who teaches it.
    """

    id: int
    name: str
    teacher_id: int


class DataManager:
    """Create a DataManager class to manage the data.

    The DataManager class is responsible for managing the student,
    teacher, and class data. It loads this information from a JSON
    file and provides methods to save it back to the file when
    changes are made.
    """

    def __init__(self):
        """Init method for the DataManager class.

        The constructor initializes empty lists for students, teachers,
        and classes, and calls the load_student_info method to populate
        these lists with data from the JSON file.
        """
        self.students: list[Student] = []
        self.teachers: list[Teacher] = []
        self.classes: list[Class] = []
        self.load_student_info()

    def load_student_info(self):
        """Load student information from a JSON file.

        It reads the file, extracts the students, teachers, and classes data,
        and populates the respective lists with instances of the Student,
        Teacher, and Class classes.
        """
        with open("student_info.json", "r") as file:
            data = json.load(file)

            students = data.get("students", [])
            teachers = data.get("teachers", [])
            classes = data.get("classes", [])

            self.students = [Student(**student) for student in students]
            self.teachers = [Teacher(**teacher) for teacher in teachers]
            self.classes = [Class(**class_) for class_ in classes]

    def save_student_info(self):
        """Save the current student information back to the JSON file.

        It converts the lists of Student, Teacher, and Class instances
        into dictionaries and writes them to the file in a structured format.
        """
        data = {
            "students": [student.__dict__ for student in self.students],
            "teachers": [teacher.__dict__ for teacher in self.teachers],
            "classes": [class_.__dict__ for class_ in self.classes],
        }
        with open("student_info.json", "w") as file:
            json.dump(data, file, indent=4)
