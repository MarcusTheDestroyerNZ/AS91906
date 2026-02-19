from tkinter import *
from tkinter import ttk

def load_view_students_page(frame, data_manager, callbacks):
    back_button = Button(frame, text="Back", command=callbacks['back'])
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(frame, text="View Students Page")
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    student_tree = ttk.Treeview(frame, columns=("ID", "First Name", "Last Name", "Class Count", "Classes"), show="headings")
    student_tree.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.5, anchor=CENTER)

    student_tree.heading("ID", text="ID")
    student_tree.heading("First Name", text="First Name")
    student_tree.heading("Last Name", text="Last Name")
    student_tree.heading("Class Count", text="Class Count")
    student_tree.heading("Classes", text="Classes")

    for student in data_manager.students:
        student_tree.insert("", "end", values=(student.id, student.first_name, student.last_name, len([class_ for class_ in data_manager.classes if student.id in class_.student_ids]), ", ".join([class_.name for class_ in data_manager.classes if student.id in class_.student_ids])))
