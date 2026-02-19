from tkinter import *
from tkinter import ttk

def load_view_students_page(frame, data_manager, callbacks):
    back_button = Button(frame, text="Back", command=callbacks['back'])
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(frame, text="View Students Page")
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    student_tree_label = Label(frame, text="Students:")
    student_tree_label.place(relx=0.25, rely=0.3, relwidth=0.1, relheight=0.05, anchor=S)

    headings = ["ID", "First Name", "Last Name", "Classes"]

    student_tree = ttk.Treeview(frame, columns=headings, show="headings")
    student_tree.place(relx=0.45, rely=0.3, relwidth=0.4, relheight=0.4, anchor=NE)

    for heading in headings:
        student_tree.heading(heading, text=heading)
        student_tree.column(heading, width=50, stretch=True)

    for student in data_manager.students:
        student_tree.insert("", "end", values=(student.id, student.first_name, student.last_name, ", ".join([class_.name for class_ in data_manager.classes if student.id in class_.student_ids])))

    select_student_label = Label(frame, text="Select a student to view details:")
    select_student_label.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.05, anchor=S)

    select_student_options = [f"{student.full_name()} (ID: {student.id})" for student in data_manager.students]
    select_student_menu = ttk.OptionMenu(frame, StringVar(), *select_student_options)
    select_student_menu.place(relx=0.7, rely=0.3, relwidth=0.2, relheight=0.05, anchor=S)
