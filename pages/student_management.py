from tkinter import *
from tkinter import simpledialog
from tkinter.ttk import Treeview

from data_manager import Student

def load_student_management_page(frame, data_manager, callbacks):
    data_manager.load_student_info()

    back_button = Button(frame, text="Back", command=callbacks['back'])
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(frame, text="Student Management Page")

    student_list_label = Label(frame, text="Students in School")

    headings = ["ID", "Name"]
    student_list = Treeview(frame, columns=("ID", "Name"), show="headings")

    for heading in headings:
        student_list.heading(heading, text=heading)
    
    student_list.column("ID", width=10, stretch=True)
    student_list.column("Name", width=200, stretch=True)

    for student in data_manager.students:
        student_list.insert("", "end", values=(student.id, student.full_name()))

    edit_student_button = Button(frame, text="Edit")
    remove_student_button = Button(frame, text="Remove")

    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    student_list_label.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.05, anchor=CENTER)
    student_list.place(relx=0.5, rely=0.35, relwidth=0.2, relheight=0.2, anchor=CENTER)

    edit_student_button.place(relx=0.4, rely=0.5, relwidth=0.1, relheight=0.05, anchor=CENTER)
    remove_student_button.place(relx=0.6, rely=0.5, relwidth=0.1, relheight=0.05, anchor=CENTER)

    add_student_first_name_label = Label(frame, text="First Name:")
    add_student_last_name_label = Label(frame, text="Last Name:")

    add_student_first_name_entry = Entry(frame)
    add_student_last_name_entry = Entry(frame)

    add_student_button = Button(frame, text="Add Student", command=lambda: add_student(data_manager, add_student_first_name_entry.get(), add_student_last_name_entry.get()))

    add_student_first_name_label.place(relx=0.45, rely=0.75, relwidth=0.1, relheight=0.05, anchor=CENTER)
    add_student_last_name_label.place(relx=0.55, rely=0.75, relwidth=0.1, relheight=0.05, anchor=CENTER)

    add_student_first_name_entry.place(relx=0.45, rely=0.8, relwidth=0.1, relheight=0.05, anchor=CENTER)
    add_student_last_name_entry.place(relx=0.55, rely=0.8, relwidth=0.1, relheight=0.05, anchor=CENTER)

    add_student_button.place(relx=0.5, rely=0.9, relwidth=0.1, relheight=0.05, anchor=CENTER)

def add_student(data_manager, first_name, last_name):
    new_id = max(student.id for student in data_manager.students) + 1 if data_manager.students else 1
    data_manager.students.append(Student(id=new_id, first_name=first_name, last_name=last_name, grades=[]))
    data_manager.save_student_info()
    print(f"Added student: {first_name} {last_name} with ID {new_id}")