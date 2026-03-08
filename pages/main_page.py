from tkinter import *
import customtkinter as ctk

ctk.set_default_color_theme("blue")
def load_main_page(frame, callbacks):
    title = ctk.CTkLabel(frame, text="Student Management System", bg_color="#3B8ED0", text_color="white", corner_radius=10)
    student_management_button = ctk.CTkButton(frame, text="Student Management", command=callbacks['student_management'])
    view_students_button = ctk.CTkButton(frame, text="View Students", command=callbacks['view_students'])
    exit_button = ctk.CTkButton(frame, text="Exit", command=callbacks['exit_app'])


    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)
    student_management_button.place(relx=0.5, rely=0.25, relwidth=0.15, relheight=0.05, anchor=CENTER)
    view_students_button.place(relx=0.5, rely=0.35, relwidth=0.15, relheight=0.05, anchor=CENTER)
    exit_button.place(relx=0.5, rely=0.45, relwidth=0.15, relheight=0.05, anchor=CENTER)