from tkinter import *
from tkinter import ttk

def load_view_classes_page(frame, data_manager, callbacks):
    back_button = Button(frame, text="Back", command=callbacks['back'])
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(frame, text="View Classes Page")
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    class_tree = ttk.Treeview(frame, columns=("ID", "Name", "Teacher","Students Count", "Students"), show="headings")
    class_tree.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.5, anchor=CENTER)

    class_tree.heading("ID", text="ID")
    class_tree.heading("Name", text="Name")
    class_tree.heading("Teacher", text="Teacher")
    class_tree.heading("Students Count", text="Students Count")
    class_tree.heading("Students", text="Students")

    for classes in data_manager.classes:
        students_list = [student.full_name() for student in data_manager.students if student.id in classes.student_ids]
        teacher_name = next((teacher.full_name() for teacher in data_manager.teachers if teacher.id == classes.teacher_id), "Unknown")
        class_tree.insert("", "end", values=(classes.id, classes.name, teacher_name, len(classes.student_ids), ", ".join(students_list)))
