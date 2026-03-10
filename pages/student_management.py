import tkinter
from tkinter import messagebox
from tkinter.ttk import Treeview

from data_manager import Student

""" This is the student management page, where you can add/remove students, edit their classes and grades, and view all of their information. """

def load_student_management_page(frame, data_manager, callbacks):
    """ This function loads the student management page and all of its components. """

    """ Load student info to ensure we have the most up-to-date data when we enter the student management page. """
    data_manager.load_student_info()

    """ Back button to return to the main page. """
    back_button = tkinter.Button(frame, text="Back", command=lambda: back_to_student_management(callbacks, frame))
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)

    """ Title for the student management page. """
    title = tkinter.Label(frame, text="Student Management Page")

    """ Title for the student list. """
    student_list_label = tkinter.Label(frame, text="Students in School")

    """ Treeview to display all students in the school. It has two columns: ID and Name. """
    headings = ["ID", "Name"]
    student_list = Treeview(frame, columns=("ID", "Name"), show="headings")

    for heading in headings:
        student_list.heading(heading, text=heading)
    student_list.column("ID", width=1, stretch=True)
    student_list.column("Name", width=200, stretch=True)

    """ Insert all students into the treeview. """
    for student in data_manager.students:
        student_list.insert("", "end", values=(student.id, student.full_name()))

    """ Buttons to edit and remove students. They are disabled by default and will be enabled when a student is selected from the treeview. """
    edit_student_button = tkinter.Button(frame, text="Edit", command=lambda: edit_student(callbacks, data_manager=data_manager, student_id=student_list.item(student_list.focus())['values'][0]))
    remove_student_button = tkinter.Button(frame, text="Remove", command=lambda: remove_student(data_manager, student_list.item(student_list.focus())['values'][0], student_list))

    """ Here is where the edit and remove buttons are enabled/disabled based on whether a student is selected in the treeview. """
    student_list.bind("<<TreeviewSelect>>", lambda event: on_student_select(event, edit_student_button, remove_student_button))
    edit_student_button.config(state=tkinter.DISABLED)
    remove_student_button.config(state=tkinter.DISABLED)

    """ Labels and entry fields to add a new student. """
    add_student_first_name_label = tkinter.Label(frame, text="First Name:")
    add_student_last_name_label = tkinter.Label(frame, text="Last Name:")

    add_student_first_name_entry = tkinter.Entry(frame)
    add_student_last_name_entry = tkinter.Entry(frame)

    add_student_inputs = [add_student_first_name_entry, add_student_last_name_entry]

    add_student_button = tkinter.Button(frame, text="Add Student", command=lambda: add_student(data_manager, add_student_inputs, student_list))

    """ Place all the components on the frame. """
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=tkinter.CENTER)

    student_list_label.place(relx=0.5, rely=0.175, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)
    student_list.place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.4, anchor=tkinter.CENTER)

    edit_student_button.place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)
    remove_student_button.place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)

    add_student_first_name_label.place(relx=0.45, rely=0.75, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)
    add_student_last_name_label.place(relx=0.55, rely=0.75, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)

    add_student_first_name_entry.place(relx=0.45, rely=0.8, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)
    add_student_last_name_entry.place(relx=0.55, rely=0.8, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)

    add_student_button.place(relx=0.5, rely=0.9, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)

def on_student_select(event, edit_student_button, remove_student_button):
    """ This function is called when a student is selected from the treeview. It enables the edit and remove buttons. If no student is selected, it disables the buttons. """
    selected_item = event.widget.selection()
    if selected_item:
        """ If a student is selected, enable the edit and remove buttons. """
        edit_student_button.config(state=tkinter.NORMAL)
        remove_student_button.config(state=tkinter.NORMAL)
    else:
        """ If no student is selected, disable the edit and remove buttons. """
        edit_student_button.config(state=tkinter.DISABLED)
        remove_student_button.config(state=tkinter.DISABLED)

def edit_student(callbacks, data_manager, student_id):
    """ This function is called when the edit button is clicked. It opens the edit student page for the selected student. """

    """ Get the edit student frame from the callbacks. """
    edit_student_frame = callbacks['edit_student']

    """ Get the full name of the student being edited. If the student is not found, use "Unknown Student". """
    student_name = next((student.full_name() for student in data_manager.students if student.id == student_id), "Unknown Student")

    """ Back button to return to the student management page. """
    back_button = tkinter.Button(edit_student_frame, text="Back", command=lambda: back_to_student_management(callbacks, edit_student_frame))
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)
 
    edit_student_label = tkinter.Label(edit_student_frame, text=f"Editing {student_name}...")
    edit_student_label.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.05, anchor=tkinter.CENTER)

    headings = ["ID", "Name", "Classes", "Grades"]
    current_selected_student_info_treeview = Treeview(edit_student_frame, columns=headings, show="headings")

    for heading in headings:
        current_selected_student_info_treeview.heading(heading, text=heading)
        current_selected_student_info_treeview.column(heading, width=1, stretch=True)
    current_selected_student_info_treeview.column("Classes", width=275, stretch=True)
    current_selected_student_info_treeview.column("Grades", width=275, stretch=True)

    for student in data_manager.students:
        if student.id == student_id:
            grade_info = []
            classes_info = []
            for classes in student.classes:
                grade_info.append(f"{classes['class_name']}: {classes['grade']}")
                classes_info.append(f"{classes['class_name']} (ID: {classes['class_id']})")
            current_selected_student_info_treeview.insert("", "end", values=(student.id, student.full_name(), ", ".join(classes_info), ", ".join(grade_info)))

    current_selected_student_info_treeview.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.075, anchor=tkinter.N)

    classes_options = [f"{class_.name} (ID: {class_.id})" for class_ in data_manager.classes]
    grades_options = [
        "A+", "A", "A-", 
        "B+", "B", "B-", 
        "C+", "C", "C-", 
        "D+", "D", "D-",
        "E+", "E", "E-",
        "F+", "F", "F-"
    ]

    classes_option_menu_for_classes = tkinter.OptionMenu(edit_student_frame, tkinter.StringVar(), *classes_options)
    classes_option_menu_for_grades = tkinter.OptionMenu(edit_student_frame, tkinter.StringVar(), *classes_options)
    grades_option_menu = tkinter.OptionMenu(edit_student_frame, tkinter.StringVar(), *grades_options)

    add_class_button = tkinter.Button(edit_student_frame, text="Add Class", command=lambda: add_or_remove_class("add", data_manager, student_id, current_selected_student_info_treeview, classes_option_menu_for_classes))
    remove_class_button = tkinter.Button(edit_student_frame, text="Remove Class", command=lambda: add_or_remove_class("remove", data_manager, student_id, current_selected_student_info_treeview, classes_option_menu_for_classes))
    add_grades_button = tkinter.Button(edit_student_frame, text="Change Grades", command=lambda: change_grades(data_manager, student_id, current_selected_student_info_treeview, classes_option_menu_for_grades, grades_option_menu))

    classes_option_menu_for_classes.place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)
    classes_option_menu_for_grades.place(relx=0.45, rely=0.45, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)
    grades_option_menu.place(relx=0.55, rely=0.45, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)

    add_class_button.place(relx=0.45,rely=0.35, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)
    remove_class_button.place(relx=0.55, rely=0.35, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)
    add_grades_button.place(relx=0.5, rely=0.5, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER)

    edit_student_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=tkinter.CENTER)

def add_or_remove_class(add_or_remove, data_manager, student_id, student_list, class_option_menu):
    selected_class = class_option_menu.cget("text")
    if selected_class:
        class_id = int(selected_class.split("ID: ")[1].rstrip(")"))
        class_name = selected_class.split(" (ID:")[0]
        for student in data_manager.students:
            if student.id == student_id:
                if any(c['class_id'] == class_id for c in student.classes):
                    if add_or_remove == "add":
                        messagebox.showwarning("Class Exists", f"{student.full_name()} is already enrolled in {class_name}.")
                        return
                    else:
                        student.classes = [c for c in student.classes if c['class_id'] != class_id]
                        data_manager.save_student_info()
                        messagebox.showinfo("Class Removed", f"Removed {class_name} from {student.full_name()}.")
                        reload_solo_student_info(data_manager, student_id, student_list)
                        break
                else:
                    if add_or_remove == "remove":
                        messagebox.showwarning("Class Not Found", f"{student.full_name()} is not enrolled in {class_name}.")
                        return
                    else:
                        student.classes.append({"class_id": class_id, "class_name": class_name, "grade": "N/A"})
                        data_manager.save_student_info()
                        messagebox.showinfo("Class Added", f"Added {class_name} to {student.full_name()}.")
                        reload_solo_student_info(data_manager, student_id, student_list)
                        break

def change_grades(data_manager, student_id, student_list, classes_option_menu, grades_option_menu):
    selected_class = classes_option_menu.cget("text")
    selected_grade = grades_option_menu.cget("text")
    print(f"Selected class from dropdown: {selected_class}")
    if selected_class and selected_grade:
        class_id = int(selected_class.split("ID: ")[1].rstrip(")"))
        print(f"Selected class ID: {class_id}, Selected grade: {selected_grade}")
        for student in data_manager.students:
            if student.id == student_id:
                found = 0
                for classes in student.classes:
                    print(f"Comparing {class_id} with {classes['class_id']}")
                    if classes['class_id'] == class_id:
                        classes['grade'] = selected_grade
                        data_manager.save_student_info()
                        messagebox.showinfo("Grade Updated", f"Updated grade for {selected_class.split(' (ID:')[0]} to {selected_grade} for {student.full_name()}.")
                        reload_student_list(data_manager, student_list)
                        found += 1
                if found == 0:
                        messagebox.showwarning("Class Not Found", f"{student.full_name()} is not enrolled in {selected_class.split(' (ID:')[0]}.")
    reload_solo_student_info(data_manager, student_id, student_list)

def remove_student(data_manager, student_id, student_list):
    student_to_remove = next((student for student in data_manager.students if student.id == student_id), None)
    if student_to_remove:
        data_manager.students.remove(student_to_remove)
        data_manager.save_student_info()
        reload_student_list(data_manager, student_list)
        messagebox.showinfo("Student Removed", f"Removed {student_to_remove.full_name()} from the system.")

def add_student(data_manager, add_student_inputs, student_list):
    first_name = add_student_inputs[0].get()
    last_name = add_student_inputs[1].get()
    new_id = max(student.id for student in data_manager.students) + 1 if data_manager.students else 1
    data_manager.students.append(Student(id=new_id, first_name=first_name.capitalize(), last_name=last_name.capitalize(), classes=[]))
    data_manager.save_student_info()
    messagebox.showinfo("Student Added", f"Added {first_name} {last_name} to the system with ID {new_id}.")
    reload_student_list(data_manager, student_list)
    for entry in add_student_inputs:
        entry.delete(0, tkinter.END)

def reload_solo_student_info(data_manager, student_id, current_selected_student_info_treeview):
    current_selected_student_info_treeview.delete(*current_selected_student_info_treeview.get_children())
    for student in data_manager.students:
        if student.id == student_id:
            grade_info = []
            classes_info = []
            for classes in student.classes:
                grade_info.append(f"{classes['class_name']}: {classes['grade']}")
                classes_info.append(f"{classes['class_name']} (ID: {classes['class_id']})")
            current_selected_student_info_treeview.insert("", "end", values=(student.id, student.full_name(), ", ".join(classes_info), ", ".join(grade_info)))

def reload_student_list(data_manager, student_list):
    student_list.delete(*student_list.get_children())
    for student in data_manager.students:
        student_list.insert("", "end", values=(student.id, student.full_name()))

def back_to_student_management(callbacks, edit_student_frame):
    edit_student_frame.place_forget()
    callbacks['back']()