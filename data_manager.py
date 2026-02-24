from dataclasses import dataclass
import json
from typing import List

@dataclass
class Student:
    id: int
    first_name: str
    last_name: str
    grades: list

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

@dataclass
class Teacher:
    id: int
    first_name: str
    last_name: str

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

@dataclass
class Class:
    id: int
    name: str
    teacher_id: int
    student_ids: List[int]

class DataManager:
    def __init__(self):
        self.students: list[Student] = []
        self.teachers: list[Teacher] = []
        self.classes: list[Class] = []
        self.load_student_info()

    def load_student_info(self):
        with open("student_info.json", "r") as file:
            data = json.load(file)

            students = data.get("students", [])
            teachers = data.get("teachers", [])
            classes = data.get("classes", [])

            self.students = [Student(**student) for student in students]
            self.teachers = [Teacher(**teacher) for teacher in teachers]
            self.classes = [Class(**class_) for class_ in classes]

    def save_student_info(self):
        data = {
            "students": [student.__dict__ for student in self.students],
            "teachers": [teacher.__dict__ for teacher in self.teachers],
            "classes": [class_.__dict__ for class_ in self.classes]
        }
        with open("student_info.json", "w") as file:
            json.dump(data, file, indent=4)