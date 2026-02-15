from tkinter import *
import json

window = Tk()
window.geometry("1280x720")
window.title("Student Management System")
# window.config(background="grey")

main_page_frame = Frame(window, bg="grey")

admin_page_frame = Frame(window, bg="yellow")
student_page_frame = Frame(window, bg="grey")

def exit_program():
    window.destroy()
    print("Should Have Closed")

def open_admin_page():
    main_page_frame.place_forget()
    admin_page_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

def open_student_page():
    main_page_frame.place_forget()
    student_page_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

    title = Label(student_page_frame, text="Student Page", width=20)

    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

def open_main_page():
    admin_page_frame.place_forget()
    student_page_frame.place_forget()
    main_page_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

    title = Label(main_page_frame, text="Student Management System", width=20)

    admin_button = Button(main_page_frame, text="Admin", width=20)
    student_button = Button(main_page_frame, text="Student", width=20, command=open_student_page)
    exit_button = Button(main_page_frame, text="Exit", width=20, command=exit_program)

    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    admin_button.place(relx=0.5, rely=0.25, relwidth=0.1, relheight=0.05, anchor=CENTER)
    student_button.place(relx=0.5, rely=0.35, relwidth=0.1, relheight=0.05, anchor=CENTER)
    exit_button.place(relx=0.5, rely=0.45, relwidth=0.1, relheight=0.05, anchor=CENTER)

open_main_page()

window.mainloop()
