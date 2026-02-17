from tkinter import *
from data_manager import Student, Teacher, Class, DataManager
from tkinter import ttk


window = Tk()
window.geometry("1280x720")
window.title("Student Management System")
window.config(background="grey")

main_page_frame = Frame(window, bg="grey")

admin_page_frame = Frame(window, bg="grey")
student_page_frame = Frame(window, bg="grey")

student_management_frame = Frame(window, bg="grey")
view_students_frame = Frame(window, bg="grey")
view_classes_frame = Frame(window, bg="grey")

place_frame_values = {"relx": 0.5, "rely": 0.5, "relwidth": 1, "relheight": 1, "anchor": CENTER}

global data_manager
data_manager = DataManager()

def exit_program():
    window.destroy()

def open_admin_page():
    view_students_frame.place_forget()
    student_management_frame.place_forget()
    view_classes_frame.place_forget()
    main_page_frame.place_forget()
    admin_page_frame.place(**place_frame_values)

    back_button = Button(admin_page_frame, text="Back", command=open_main_page)

    title = Label(admin_page_frame, text="Admin Page")
    
    add_student_button = Button(admin_page_frame, text="Student Management", command=lambda: student_management_page())
    view_students_button = Button(admin_page_frame, text="View Students", command=lambda: view_students_page())

    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    add_student_button.place(relx=0.5, rely=0.25, relwidth=0.1, relheight=0.05, anchor=CENTER)
    view_students_button.place(relx=0.5, rely=0.35, relwidth=0.1, relheight=0.05, anchor=CENTER)

    view_classes_button = Button(admin_page_frame, text="View Classes", command=lambda: view_classes_page())
    view_classes_button.place(relx=0.5, rely=0.45, relwidth=0.1, relheight=0.05, anchor=CENTER)

def open_student_page():
    main_page_frame.place_forget()
    student_page_frame.place(**place_frame_values)

    back_button = Button(student_page_frame, text="Back", command=open_main_page)
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(student_page_frame, text="Student Page", width=20)
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    view_classes_label = Label(student_page_frame, text="Your classes:")
    view_classes_label.place(relx=0.5, rely=0.2, relwidth=0.2, relheight=0.05, anchor=CENTER)

    view_classes_tree = ttk.Treeview(student_page_frame, columns=("ID", "Name", "Teacher"), show="headings")
    view_classes_tree.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.5, anchor=CENTER)

    view_classes_tree.heading("ID", text="ID")
    view_classes_tree.heading("Name", text="Name")
    view_classes_tree.heading("Teacher", text="Teacher")

    for classes in data_manager.classes:
        teacher_list = [teacher.full_name() for teacher in data_manager.teachers if teacher.id == classes.teacher_id]
        view_classes_tree.insert("", "end", values=(classes.id, classes.name, teacher_list[0] if teacher_list else "No Teacher Assigned"))

def open_main_page():
    admin_page_frame.place_forget()
    student_page_frame.place_forget()
    main_page_frame.place(**place_frame_values)

    title = Label(main_page_frame, text="Student Management System", width=20)

    admin_button = Button(main_page_frame, text="Admin", command=open_admin_page)
    student_button = Button(main_page_frame, text="Student", command=open_student_page)
    exit_button = Button(main_page_frame, text="Exit", command=exit_program)

    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    admin_button.place(relx=0.5, rely=0.25, relwidth=0.1, relheight=0.05, anchor=CENTER)
    student_button.place(relx=0.5, rely=0.35, relwidth=0.1, relheight=0.05, anchor=CENTER)
    exit_button.place(relx=0.5, rely=0.45, relwidth=0.1, relheight=0.05, anchor=CENTER)

def student_management_page():
    admin_page_frame.place_forget()
    student_management_frame.place(**place_frame_values)

    back_button = Button(student_management_frame, text="Back", command=open_admin_page)
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(student_management_frame, text="Student Management Page")
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    add_student_label = Label(student_management_frame, text="Add a new student...")
    add_student_label.place(relx=0.5, rely=0.25, relwidth=0.2, relheight=0.05, anchor=CENTER)

    new_student_first_name_label = Label(student_management_frame, text="First name:")
    new_student_first_name_label.place(relx=0.4, rely=0.3, relwidth=0.1, relheight=0.05, anchor=W)

    new_student_first_name_input = Entry(student_management_frame)
    new_student_first_name_input.place(relx=0.6, rely=0.3, relwidth=0.1, relheight=0.05, anchor=E)

    new_student_last_name_label = Label(student_management_frame, text="Last name:")
    new_student_last_name_label.place(relx=0.4, rely=0.35, relwidth=0.1, relheight=0.05, anchor=W)

    new_student_last_name_input = Entry(student_management_frame)
    new_student_last_name_input.place(relx=0.6, rely=0.35, relwidth=0.1, relheight=0.05, anchor=E)

    add_student_button = Button(student_management_frame, text="Add Student", command=lambda: print(f"Adding student: {new_student_first_name_input.get()} {new_student_last_name_input.get()}"))
    add_student_button.place(relx=0.5, rely=0.4, relwidth=0.1, relheight=0.05, anchor=CENTER)

    student_drop_down_label = Label(student_management_frame, text="Add")
    student_drop_down_label.place(relx=0.4, rely=0.5, relwidth=0.1, relheight=0.05, anchor=W)

    student_drop_down = OptionMenu(student_management_frame, StringVar(), *[student.full_name() for student in data_manager.students])
    student_drop_down.place(relx=0.6, rely=0.5, relwidth=0.1, relheight=0.05, anchor=E)

    class_drop_down_label = Label(student_management_frame, text="to")
    class_drop_down_label.place(relx=0.4, rely=0.55, relwidth=0.1, relheight=0.05, anchor=W)

    class_drop_down = OptionMenu(student_management_frame, StringVar(), *[class_.name for class_ in data_manager.classes])
    class_drop_down.place(relx=0.6, rely=0.55, relwidth=0.1, relheight=0.05, anchor=E)    

    add_to_class_button = Button(student_management_frame, text="Add to Class", command=lambda: print(f"Adding {student_drop_down.cget('text')} to {class_drop_down.cget('text')}"))
    add_to_class_button.place(relx=0.5, rely=0.6, relwidth=0.1, relheight=0.05, anchor=CENTER)

    remove_student_label = Label(student_management_frame, text="Remove")
    remove_student_label.place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.05, anchor=W)

    remove_student_drop_down = OptionMenu(student_management_frame, StringVar(), *[student.full_name() for student in data_manager.students])
    remove_student_drop_down.place(relx=0.6, rely=0.7, relwidth=0.1, relheight=0.05, anchor=E)

    remove_from_class_label = Label(student_management_frame, text="from")
    remove_from_class_label.place(relx=0.4, rely=0.75, relwidth=0.1, relheight=0.05, anchor=W)

    remove_from_class_drop_down = OptionMenu(student_management_frame, StringVar(), *[class_.name for class_ in data_manager.classes])
    remove_from_class_drop_down.place(relx=0.6, rely=0.75, relwidth=0.1, relheight=0.05, anchor=E)

    remove_from_class_button = Button(student_management_frame, text="Remove from Class", command=lambda: print(f"Removing {remove_student_drop_down.cget('text')} from {remove_from_class_drop_down.cget('text')}"))
    remove_from_class_button.place(relx=0.5, rely=0.8, relwidth=0.1, relheight=0.05, anchor=CENTER)

def view_students_page():
    admin_page_frame.place_forget()
    view_students_frame.place(**place_frame_values)

    back_button = Button(view_students_frame, text="Back", command=open_admin_page)
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(view_students_frame, text="View Students Page")
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    student_tree = ttk.Treeview(view_students_frame, columns=("ID", "First Name", "Last Name", "Class Count", "Classes"), show="headings")
    student_tree.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.5, anchor=CENTER)

    student_tree.heading("ID", text="ID")
    student_tree.heading("First Name", text="First Name")
    student_tree.heading("Last Name", text="Last Name")
    student_tree.heading("Class Count", text="Class Count")
    student_tree.heading("Classes", text="Classes")

    for student in data_manager.students:
        student_tree.insert("", "end", values=(student.id, student.first_name, student.last_name, len([class_ for class_ in data_manager.classes if student.id in class_.student_ids]), ", ".join([class_.name for class_ in data_manager.classes if student.id in class_.student_ids])))

def view_classes_page():
    admin_page_frame.place_forget()
    view_classes_frame.place(**place_frame_values)

    back_button = Button(view_classes_frame, text="Back", command=open_admin_page)
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(view_classes_frame, text="View Classes Page")
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    class_tree = ttk.Treeview(view_classes_frame, columns=("ID", "Name", "Students Count", "Students"), show="headings")
    class_tree.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.5, anchor=CENTER)

    class_tree.heading("ID", text="ID")
    class_tree.heading("Name", text="Name")
    class_tree.heading("Students Count", text="Students Count")
    class_tree.heading("Students", text="Students")

    for classes in data_manager.classes:
        students_list = [student.full_name() for student in data_manager.students if student.id in classes.student_ids]
        class_tree.insert("", "end", values=(classes.id, classes.name, len(classes.student_ids), ", ".join(students_list)))

open_main_page()

window.mainloop()
