from tkinter import *

def load_student_management_page(frame, data_manager, callbacks):
    back_button = Button(frame, text="Back", command=callbacks['back'])
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(frame, text="Student Management Page")
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    view_add_student_page_button = Button(frame, text="Add/Remove Students", command= callbacks['add_or_remove_students'])
    view_add_student_page_button.place(relx=0.5, rely=0.25, relwidth=0.1, relheight=0.05, anchor=CENTER)

    student_drop_down_label = Label(frame, text="Add")
    student_drop_down_label.place(relx=0.4, rely=0.5, relwidth=0.1, relheight=0.05, anchor=W)

    student_drop_down = OptionMenu(frame, StringVar(), *[student.full_name() for student in data_manager.students])
    student_drop_down.place(relx=0.6, rely=0.5, relwidth=0.1, relheight=0.05, anchor=E)

    class_drop_down_label = Label(frame, text="to")
    class_drop_down_label.place(relx=0.4, rely=0.55, relwidth=0.1, relheight=0.05, anchor=W)

    class_drop_down = OptionMenu(frame, StringVar(), *[class_.name for class_ in data_manager.classes])
    class_drop_down.place(relx=0.6, rely=0.55, relwidth=0.1, relheight=0.05, anchor=E)    

    add_to_class_button = Button(frame, text="Add to Class", command=lambda: print(f"Adding {student_drop_down.cget('text')} to {class_drop_down.cget('text')}"))
    add_to_class_button.place(relx=0.5, rely=0.6, relwidth=0.1, relheight=0.05, anchor=CENTER)

    remove_student_label = Label(frame, text="Remove")
    remove_student_label.place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.05, anchor=W)

    remove_student_drop_down = OptionMenu(frame, StringVar(), *[student.full_name() for student in data_manager.students])
    remove_student_drop_down.place(relx=0.6, rely=0.7, relwidth=0.1, relheight=0.05, anchor=E)

    remove_from_class_label = Label(frame, text="from")
    remove_from_class_label.place(relx=0.4, rely=0.75, relwidth=0.1, relheight=0.05, anchor=W)

    remove_from_class_drop_down = OptionMenu(frame, StringVar(), *[class_.name for class_ in data_manager.classes])
    remove_from_class_drop_down.place(relx=0.6, rely=0.75, relwidth=0.1, relheight=0.05, anchor=E)

    remove_from_class_button = Button(frame, text="Remove from Class", command=lambda: print(f"Removing {remove_student_drop_down.cget('text')} from {remove_from_class_drop_down.cget('text')}"))
    remove_from_class_button.place(relx=0.5, rely=0.8, relwidth=0.1, relheight=0.05, anchor=CENTER)
