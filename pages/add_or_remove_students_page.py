from tkinter import *

def load_add_or_remove_students_page(frame, data_manager, callbacks):
    back_button = Button(frame, text="Back", command= lambda: callbacks['back']())
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(frame, text="Add/Remove Students Page")
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    add_student_label = Label(frame, text="Add a new student...")
    add_student_label.place(relx=0.5, rely=0.25, relwidth=0.2, relheight=0.05, anchor=CENTER)

    new_student_first_name_label = Label(frame, text="First name:")
    new_student_first_name_label.place(relx=0.4, rely=0.3, relwidth=0.1, relheight=0.05, anchor=W)

    new_student_first_name_input = Entry(frame)
    new_student_first_name_input.place(relx=0.6, rely=0.3, relwidth=0.1, relheight=0.05, anchor=E)

    new_student_last_name_label = Label(frame, text="Last name:")
    new_student_last_name_label.place(relx=0.4, rely=0.35, relwidth=0.1, relheight=0.05, anchor=W)

    new_student_last_name_input = Entry(frame)
    new_student_last_name_input.place(relx=0.6, rely=0.35, relwidth=0.1, relheight=0.05, anchor=E)

    new_student_id_label = Label(frame, text="ID:")
    new_student_id_label.place(relx=0.4, rely=0.4, relwidth=0.1, relheight=0.05, anchor=W)

    new_student_id_input = Entry(frame)
    new_student_id_input.place(relx=0.6, rely=0.4, relwidth=0.1, relheight=0.05, anchor=E)

    add_student_button = Button(frame, text="Add Student", command=lambda: print(f"Adding student: {new_student_first_name_input.get()} {new_student_last_name_input.get()} with ID {new_student_id_input.get()}"))
    add_student_button.place(relx=0.5, rely=0.45, relwidth=0.1, relheight=0.05, anchor=CENTER)

    remove_student_label = Label(frame, text="Remove a student...")
    remove_student_label.place(relx=0.5, rely=0.6, relwidth=0.2, relheight=0.05, anchor=CENTER)

    remove_student_options_label = Label(frame, text="Select student:")
    remove_student_options_label.place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.05, anchor=W)

    remove_student_option_menu = OptionMenu(frame, StringVar(), *[student.full_name() for student in data_manager.students])
    remove_student_option_menu.place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.05, anchor=E)

    remove_student_button = Button(frame, text="Remove Student", command=lambda: print(f"Removing student: {remove_student_option_menu.cget('text')}"))
    remove_student_button.place(relx=0.5, rely=0.7, relwidth=0.1, relheight=0.05, anchor=CENTER)