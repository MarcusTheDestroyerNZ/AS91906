from tkinter import *
from tkinter import ttk

def load_view_classes_page(frame, data_manager, callbacks):
    back_button = Button(frame, text="Back", command=callbacks['back'])
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(frame, text="View Classes Page")
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    headings = ["ID", "Name", "Teacher", "Students Count", "Students"]

    class_tree = ttk.Treeview(frame, columns=("ID", "Name", "Teacher","Students Count", "Students"), show="headings")
    class_tree.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.5, anchor=CENTER)

    for heading in headings:
        class_tree.heading(heading, text=heading)
        class_tree.column(heading, width=50, stretch=True)
    class_tree.column("Students", width=150, stretch=True)

    for classes in data_manager.classes:
        students_list = [student.full_name() for student in data_manager.students if student.id in classes.student_ids]
        teacher_name = next((teacher.full_name() for teacher in data_manager.teachers if teacher.id == classes.teacher_id), "Unknown")
        class_tree.insert("", "end", values=(classes.id, classes.name, teacher_name, len(classes.student_ids), ", ".join(students_list)))
