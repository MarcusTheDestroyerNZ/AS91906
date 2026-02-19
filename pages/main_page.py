from tkinter import *

def load_main_page(frame, callbacks):
    title = Label(frame, text="Student Management System", width=20)
    student_management_button = Button(frame, text="Student Management", command=callbacks['student_management'])
    teacher_management_button = Button(frame, text="Teacher Management", command=callbacks['teacher_management'])
    view_students_button = Button(frame, text="View Students", command=callbacks['view_students'])
    view_classes_button = Button(frame, text="View Classes", command=callbacks['view_classes'])
    exit_button = Button(frame, text="Exit", command=callbacks['exit_app'])


    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)
    student_management_button.place(relx=0.5, rely=0.25, relwidth=0.1, relheight=0.05, anchor=CENTER)
    teacher_management_button.place(relx=0.5, rely=0.35, relwidth=0.1, relheight=0.05, anchor=CENTER)
    view_students_button.place(relx=0.5, rely=0.45, relwidth=0.1, relheight=0.05, anchor=CENTER)
    view_classes_button.place(relx=0.5, rely=0.55, relwidth=0.1, relheight=0.05, anchor=CENTER)
    exit_button.place(relx=0.5, rely=0.65, relwidth=0.1, relheight=0.05, anchor=CENTER)