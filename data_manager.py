from dataclasses import dataclass
import json
from typing import List

@dataclass
class Student:
    id: int
    first_name: str
    last_name: str
    dob: str
    email: str

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

@dataclass
class Teacher:
    id: int
    first_name: str
    last_name: str
    email: str

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