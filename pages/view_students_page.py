from tkinter import *
from tkinter import ttk

def load_view_students_page(frame, data_manager, callbacks):
    back_button = Button(frame, text="Back", command=callbacks['back'])
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(frame, text="View Students Page")
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    headings = ["ID", "Name", "Classes", "Grades"]

    student_tree = ttk.Treeview(frame, columns=headings, show="headings")
    student_tree.place(relx=0.5, rely=0.3, relwidth=0.8, relheight=0.6, anchor=N)

    for heading in headings:
        student_tree.heading(heading, text=heading)
        student_tree.column(heading, width=50, stretch=True)
    student_tree.column("Grades", width=150)

    for student in data_manager.students:
        grade_info = []
        for grade in student.grades:
            grade_info.append(f"Class: {grade['class_id']} Grade: {grade['grade']}")
        student_tree.insert("", "end", values=(student.id, student.full_name(), ", ".join([class_.name for class_ in data_manager.classes if student.id in class_.student_ids]), ", ".join(grade_info)))
