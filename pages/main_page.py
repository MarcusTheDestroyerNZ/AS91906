from tkinter import *

def load_main_page(frame, callbacks):
    title = Label(frame, text="Student Management System")
    student_management_button = Button(frame, text="Student Management", command=callbacks['student_management'])
    view_students_button = Button(frame, text="View Students", command=callbacks['view_students'])
    exit_button = Button(frame, text="Exit", command=callbacks['exit_app'])

    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)
    student_management_button.place(relx=0.5, rely=0.25, relwidth=0.15, relheight=0.05, anchor=CENTER)
    view_students_button.place(relx=0.5, rely=0.35, relwidth=0.15, relheight=0.05, anchor=CENTER)
    exit_button.place(relx=0.5, rely=0.45, relwidth=0.15, relheight=0.05, anchor=CENTER)