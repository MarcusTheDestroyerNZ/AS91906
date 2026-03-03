from tkinter import *
from tkinter import simpledialog
from tkinter.ttk import Treeview
from tkinter import messagebox

from data_manager import Student

def load_student_management_page(frame, data_manager, callbacks):
    data_manager.load_student_info()

    back_button = Button(frame, text="Back", command=lambda: back_to_student_management(callbacks, frame))
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(frame, text="Student Management Page")

    student_list_label = Label(frame, text="Students in School")

    headings = ["ID", "Name"]
    student_list = Treeview(frame, columns=("ID", "Name"), show="headings")

    for heading in headings:
        student_list.heading(heading, text=heading)
    
    student_list.column("ID", width=1, stretch=True)
    student_list.column("Name", width=200, stretch=True)

    for student in data_manager.students:
        student_list.insert("", "end", values=(student.id, student.full_name()))

    edit_student_button = Button(frame, text="Edit", command=lambda: edit_student(callbacks, data_manager=data_manager, student_id=student_list.item(student_list.focus())['values'][0]))
    remove_student_button = Button(frame, text="Remove", command=lambda: remove_student(data_manager, student_list.item(student_list.focus())['values'][0], student_list))

    student_list.bind("<<TreeviewSelect>>", lambda event: on_student_select(event, edit_student_button, remove_student_button))
    edit_student_button.config(state=DISABLED)
    remove_student_button.config(state=DISABLED)

    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    student_list_label.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.05, anchor=CENTER)
    student_list.place(relx=0.5, rely=0.35, relwidth=0.2, relheight=0.2, anchor=CENTER)

    edit_student_button.place(relx=0.4, rely=0.5, relwidth=0.1, relheight=0.05, anchor=CENTER)
    remove_student_button.place(relx=0.6, rely=0.5, relwidth=0.1, relheight=0.05, anchor=CENTER)

    add_student_first_name_label = Label(frame, text="First Name:")
    add_student_last_name_label = Label(frame, text="Last Name:")

    add_student_first_name_entry = Entry(frame)
    add_student_last_name_entry = Entry(frame)

    add_student_inputs = [add_student_first_name_entry, add_student_last_name_entry]

    add_student_button = Button(frame, text="Add Student", command=lambda: add_student(data_manager, add_student_inputs, student_list))

    add_student_first_name_label.place(relx=0.45, rely=0.75, relwidth=0.1, relheight=0.05, anchor=CENTER)
    add_student_last_name_label.place(relx=0.55, rely=0.75, relwidth=0.1, relheight=0.05, anchor=CENTER)

    add_student_first_name_entry.place(relx=0.45, rely=0.8, relwidth=0.1, relheight=0.05, anchor=CENTER)
    add_student_last_name_entry.place(relx=0.55, rely=0.8, relwidth=0.1, relheight=0.05, anchor=CENTER)

    add_student_button.place(relx=0.5, rely=0.9, relwidth=0.1, relheight=0.05, anchor=CENTER)

def on_student_select(event, edit_student_button, remove_student_button):
    selected_item = event.widget.selection()
    if selected_item:
        edit_student_button.config(state=NORMAL)
        remove_student_button.config(state=NORMAL)
    else:
        edit_student_button.config(state=DISABLED)
        remove_student_button.config(state=DISABLED)

def edit_student(callbacks, data_manager, student_id):
    edit_student_frame = callbacks['edit_student']

    student_name = next((student.full_name() for student in data_manager.students if student.id == student_id), "Unknown Student")

    edit_student_label = Label(edit_student_frame, text=f"Editing {student_name}...")
    edit_student_label.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.05, anchor=CENTER)

    headings = ["ID", "Name", "Classes", "Grades"]
    current_selected_student_info_treeview = Treeview(edit_student_frame, columns=headings, show="headings")

    for heading in headings:
        current_selected_student_info_treeview.heading(heading, text=heading)
        current_selected_student_info_treeview.column(heading, width=200, stretch=True)
    current_selected_student_info_treeview.column("ID", width=1, stretch=True)
    current_selected_student_info_treeview.column("Name", width=1, stretch=True)

    for student in data_manager.students:
        if student.id == student_id:
            grade_info = []
            for grade in student.grades:
                grade_info.append(f"Class: {grade['class_id']} Grade: {grade['grade']}")
            current_selected_student_info_treeview.insert("", "end", values=(student.id, student.full_name(), ", ".join([class_.name for class_ in data_manager.classes if student.id in class_.student_ids]), ", ".join(grade_info)))

    current_selected_student_info_treeview.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.075, anchor=N)
    change_classes_button = Button(edit_student_frame, text="Change Classes", command=lambda: edit_student_classes_popup(data_manager, student_id, current_selected_student_info_treeview))
    change_grades_button = Button(edit_student_frame, text="Change Grades", command=lambda: edit_student_grades_popup(data_manager, student_id, current_selected_student_info_treeview))

    change_classes_button.place(relx=0.6,rely=0.35, relwidth=0.1, relheight=0.05, anchor=CENTER)
    change_grades_button.place(relx=0.4, rely=0.35, relwidth=0.1, relheight=0.05, anchor=CENTER)

    edit_student_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

def edit_student_classes_popup(data_manager, student_id, student_list):
    new_classes = simpledialog.askstring("Change Classes", "Enter new classes (comma separated):")
    if new_classes:
        for student in data_manager.students:
            if student.id == student_id:
                student.classes = [class_.strip() for class_ in new_classes.split(",")]
                break
        data_manager.save_student_info()
        messagebox.showinfo("Classes Change", f"Classes changed to {new_classes}")
        reload_student_list(data_manager, student_list)

def edit_student_grades_popup(data_manager, student_id, student_list):
    new_grades = simpledialog.askstring("Change Grades", "Enter new grades (comma separated, format: class_id:grade):")
    if new_grades:
        for student in data_manager.students:
            if student.id == student_id:
                student.grades = []
                for grade in new_grades.split(","):
                    class_id, grade_value = grade.split(":")
                    student.grades.append({"class_id": int(class_id), "grade": grade_value})
                break
        data_manager.save_student_info()
        messagebox.showinfo("Grades Change", f"Grades changed to {new_grades}")
        reload_student_list(data_manager, student_list)

def remove_student(data_manager, student_id, student_list):
    student_to_remove = next((student for student in data_manager.students if student.id == student_id), None)
    if student_to_remove:
        data_manager.students.remove(student_to_remove)
        data_manager.save_student_info()
        print(f"Removed student: {student_to_remove.full_name()} with ID {student_id}")
        reload_student_list(data_manager, student_list)

def add_student(data_manager, add_student_inputs, student_list):
    first_name = add_student_inputs[0].get()
    last_name = add_student_inputs[1].get()
    new_id = max(student.id for student in data_manager.students) + 1 if data_manager.students else 1
    data_manager.students.append(Student(id=new_id, first_name=first_name.capitalize(), last_name=last_name.capitalize(), grades=[]))
    data_manager.save_student_info()
    print(f"Added student: {first_name} {last_name} with ID {new_id}")
    reload_student_list(data_manager, student_list)
    for entry in add_student_inputs:
        entry.delete(0, END)

def reload_student_list(data_manager, student_list):
    student_list.delete(*student_list.get_children())
    for student in data_manager.students:
        student_list.insert("", "end", values=(student.id, student.full_name()))

def back_to_student_management(callbacks, edit_student_frame):
    edit_student_frame.place_forget()
    callbacks['back']()