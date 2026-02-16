from tkinter import *
import json
from tkinter import ttk

window = Tk()
window.geometry("1280x720")
window.title("Student Management System")
window.config(background="grey")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12, "bold"), background="lightblue", foreground="black")

main_page_frame = Frame(window, bg="grey")

admin_page_frame = Frame(window, bg="grey")
student_page_frame = Frame(window, bg="grey")

place_frame_values = {"relx": 0.5, "rely": 0.5, "relwidth": 1, "relheight": 1, "anchor": CENTER}

def exit_program():
    window.destroy()

def open_admin_page():
    main_page_frame.place_forget()
    admin_page_frame.place(**place_frame_values)

    back_button = Button(admin_page_frame, text="Back", command=open_main_page)
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(admin_page_frame, text="Admin Page")
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

def open_student_page():
    main_page_frame.place_forget()
    student_page_frame.place(**place_frame_values)

    back_button = Button(student_page_frame, text="Back", command=open_main_page)
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(student_page_frame, text="Student Page", width=20)

    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

def open_main_page():
    admin_page_frame.place_forget()
    student_page_frame.place_forget()
    main_page_frame.place(**place_frame_values)

    title = ttk.Label(main_page_frame, text="Student Management System", width=20, style="TLabel")

    admin_button = Button(main_page_frame, text="Admin", command=open_admin_page)
    student_button = Button(main_page_frame, text="Student", command=open_student_page)
    exit_button = Button(main_page_frame, text="Exit", command=exit_program)

    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    admin_button.place(relx=0.5, rely=0.25, relwidth=0.1, relheight=0.05, anchor=CENTER)
    student_button.place(relx=0.5, rely=0.35, relwidth=0.1, relheight=0.05, anchor=CENTER)
    exit_button.place(relx=0.5, rely=0.45, relwidth=0.1, relheight=0.05, anchor=CENTER)

open_main_page()

window.mainloop()
