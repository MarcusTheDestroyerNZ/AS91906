"""Student management page for the Student Management System application."""

import tkinter
from tkinter import messagebox
from tkinter.ttk import Treeview

from data_manager import Student


def load_student_management_page(frame, data_manager, callbacks):
    """Load the student management page and all of its components."""
    """Load student info to ensure we have the most up-to-date data when we
    enter the student management page.
    """
    data_manager.load_student_info()

    """Back button to return to the main page."""
    back_button = tkinter.Button(
        frame, text="Back", command=lambda: back_to_main_menu(callbacks, frame)
    )
    back_button.place(
        relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER
    )

    """ Title for the student management page. """
    title = tkinter.Label(frame, text="Student Management Page")

    """ Title for the student list. """
    student_list_label = tkinter.Label(frame, text="Students in School")

    """Treeview to display all students in the school.
    It has two columns: ID and Name.
    """
    headings = ["ID", "Name"]
    student_list = Treeview(frame, columns=("ID", "Name"), show="headings")

    for heading in headings:
        student_list.heading(heading, text=heading)
    student_list.column("ID", width=1, stretch=True)
    student_list.column("Name", width=200, stretch=True)

    """ Insert all students into the treeview. """
    for student in data_manager.students:
        student_list.insert("", "end", values=(
            student.id, student.full_name()
        ))

    """ Buttons to edit and remove students. They are disabled by default
    and will be enabled when a student is selected from the treeview.
    """
    edit_student_button = tkinter.Button(
        frame,
        text="Edit",
        command=lambda: edit_student(
            callbacks,
            data_manager=data_manager,
            student_id=student_list.item(student_list.focus())["values"][0],
        ),
    )
    remove_student_button = tkinter.Button(
        frame,
        text="Remove",
        command=lambda: remove_student(
            data_manager,
            student_list.item(student_list.focus())["values"][0],
            student_list,
        ),
    )

    """ Here is where the edit and remove buttons are enabled/disabled based
    on whether a student is selected in the treeview.
    """
    student_list.bind(
        "<<TreeviewSelect>>",
        lambda event: on_student_select(
            event, edit_student_button, remove_student_button
        ),
    )
    edit_student_button.config(state=tkinter.DISABLED)
    remove_student_button.config(state=tkinter.DISABLED)

    """ Labels and entry fields to add a new student. """
    add_student_first_name_label = tkinter.Label(frame, text="First Name:")
    add_student_last_name_label = tkinter.Label(frame, text="Last Name:")

    add_student_first_name_entry = tkinter.Entry(frame)
    add_student_last_name_entry = tkinter.Entry(frame)

    add_student_inputs = [
        add_student_first_name_entry,
        add_student_last_name_entry
    ]

    add_student_button = tkinter.Button(
        frame,
        text="Add Student",
        command=lambda: add_student(
            data_manager,
            add_student_inputs,
            student_list
        ),
    )

    """ Place all the components on the frame. """
    title.place(
        relx=0.5,
        rely=0.1,
        relwidth=0.2,
        relheight=0.05,
        anchor=tkinter.CENTER
    )

    student_list_label.place(
        relx=0.5,
        rely=0.175,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )
    student_list.place(
        relx=0.5,
        rely=0.4,
        relwidth=0.2,
        relheight=0.4,
        anchor=tkinter.CENTER
    )

    edit_student_button.place(
        relx=0.4,
        rely=0.65,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )
    remove_student_button.place(
        relx=0.6,
        rely=0.65,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )

    add_student_first_name_label.place(
        relx=0.45,
        rely=0.75,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )
    add_student_last_name_label.place(
        relx=0.55,
        rely=0.75,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )

    add_student_first_name_entry.place(
        relx=0.45,
        rely=0.8,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )
    add_student_last_name_entry.place(
        relx=0.55,
        rely=0.8,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )

    add_student_button.place(
        relx=0.5,
        rely=0.9,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )


def on_student_select(event, edit_student_button, remove_student_button):
    """Allow the edit and remove buttons to Enable and disable.

    It enables the edit and remove buttons. If no student is selected,
    it disables the buttons.
    """
    selected_item = event.widget.selection()
    if selected_item:
        """If a student is selected, enable the edit and remove buttons."""
        edit_student_button.config(state=tkinter.NORMAL)
        remove_student_button.config(state=tkinter.NORMAL)
    else:
        """If no student is selected, disable the edit and remove buttons."""
        edit_student_button.config(state=tkinter.DISABLED)
        remove_student_button.config(state=tkinter.DISABLED)


def edit_student(callbacks, data_manager, student_id):
    """Open the edit student page for the selected student.

    It opens the edit student page for the selected student.
    The edit student page allows the user to add or remove classes and
    change grades for the selected student. The student's current classes
    and grades are displayed in a treeview on the edit student page.
    The user can select a class from a dropdown menu and either add
    or remove it from the student's classes, or change the grade for a class.
    After making changes, the student's info is saved and the treeview is
    updated to reflect the changes.
    """
    """ Get the edit student frame from the callbacks. """
    edit_student_frame = callbacks["edit_student"]

    """ Get the full name of the student being edited.
    If the student is not found, use "Unknown Student".
    """
    student_name = next(
        (
            student.full_name()
            for student in data_manager.students
            if student.id == student_id
        ),
        "Unknown Student",
    )

    """ Back button to return to the student management page. """
    back_button = tkinter.Button(
        edit_student_frame,
        text="Back",
        command=lambda: back_to_student_management(edit_student_frame),
    )
    back_button.place(
        relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=tkinter.CENTER
    )

    """ Label to display the name of the student being edited. """
    edit_student_label = tkinter.Label(
        edit_student_frame, text=f"Editing {student_name}..."
    )
    edit_student_label.place(
        relx=0.5, rely=0.1, relwidth=0.3, relheight=0.05, anchor=tkinter.CENTER
    )

    """Treeview to display the current classes and grades of the student
    being edited. It has four columns: ID, Name, Classes, and Grades. """
    headings = ["ID", "Name", "Classes", "Grades"]
    current_selected_student_info_treeview = Treeview(
        edit_student_frame, columns=headings, show="headings"
    )

    for heading in headings:
        current_selected_student_info_treeview.heading(heading, text=heading)
        current_selected_student_info_treeview.column(
            heading,
            width=1,
            stretch=True
        )
    current_selected_student_info_treeview.column(
            "Classes",
            width=275,
            stretch=True
        )
    current_selected_student_info_treeview.column(
            "Grades",
            width=275,
            stretch=True
        )

    """Insert the current classes and grades of the student being edited
    into the treeview.
    """
    for student in data_manager.students:
        if student.id == student_id:
            grade_info = []
            classes_info = []
            for classes in student.classes:
                grade_info.append(
                    f"{classes['class_name']}: {classes['grade']}"
                )
                classes_info.append(
                    f"{classes['class_name']} (ID: {classes['class_id']})"
                )
            current_selected_student_info_treeview.insert(
                "",
                "end",
                values=(
                    student.id,
                    student.full_name(),
                    ", ".join(classes_info),
                    ", ".join(grade_info),
                ),
            )

    current_selected_student_info_treeview.place(
        relx=0.5, rely=0.2, relwidth=0.8, relheight=0.075, anchor=tkinter.N
    )

    """Options for the dropdown menus to add/remove classes and change grades.
    The classes options are generated from the classes in the data manager,
    and the grades options are hardcoded.
    """
    classes_options = [
        f"{classes.name} (ID: {classes.id})"
        for classes in data_manager.classes
    ]
    grades_options = [
        "A+",
        "A",
        "A-",
        "B+",
        "B",
        "B-",
        "C+",
        "C",
        "C-",
        "D+",
        "D",
        "D-",
        "E+",
        "E",
        "E-",
        "F+",
        "F",
        "F-",
    ]

    """ Dropdown menus to add/remove classes and change grades. """
    classes_option_menu_for_classes = tkinter.OptionMenu(
        edit_student_frame, tkinter.StringVar(), *classes_options
    )
    classes_option_menu_for_grades = tkinter.OptionMenu(
        edit_student_frame, tkinter.StringVar(), *classes_options
    )
    grades_option_menu = tkinter.OptionMenu(
        edit_student_frame, tkinter.StringVar(), *grades_options
    )

    """Buttons to add/remove classes and change grades.
    They call the respective functions when clicked.
    """
    add_class_button = tkinter.Button(
        edit_student_frame,
        text="Add Class",
        command=lambda: add_or_remove_class(
            "add",
            data_manager,
            student_id,
            current_selected_student_info_treeview,
            classes_option_menu_for_classes,
        ),
    )
    remove_class_button = tkinter.Button(
        edit_student_frame,
        text="Remove Class",
        command=lambda: add_or_remove_class(
            "remove",
            data_manager,
            student_id,
            current_selected_student_info_treeview,
            classes_option_menu_for_classes,
        ),
    )
    add_grades_button = tkinter.Button(
        edit_student_frame,
        text="Change Grades",
        command=lambda: change_grades(
            data_manager,
            student_id,
            current_selected_student_info_treeview,
            classes_option_menu_for_grades,
            grades_option_menu,
        ),
    )

    """ Place the dropdown menus and buttons on the frame. """
    classes_option_menu_for_classes.place(
        relx=0.5,
        rely=0.3,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )
    classes_option_menu_for_grades.place(
        relx=0.45,
        rely=0.45,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )
    grades_option_menu.place(
        relx=0.55,
        rely=0.45,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )

    add_class_button.place(
        relx=0.45,
        rely=0.35,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )
    remove_class_button.place(
        relx=0.55,
        rely=0.35,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )
    add_grades_button.place(
        relx=0.5,
        rely=0.5,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )

    edit_student_frame.place(
        relx=0.5,
        rely=0.5,
        relwidth=1,
        relheight=1,
        anchor=tkinter.CENTER
    )


def add_or_remove_class(
    add_or_remove, data_manager, student_id, student_list, class_option_menu
):
    """Add or remove the selected class.

    Adds or removes the selected class from the student's classes based on
    the add_or_remove parameter.
    """
    selected_class = class_option_menu.cget("text")

    """If a class is selected from the dropdown menu, proceed with adding
    or removing the class. If no class is selected, show a warning message.
    """
    if selected_class:
        """The class ID is extracted from the selected class string, and
        the class name is also extracted for use in messages.
        """
        class_id = int(selected_class.split("ID: ")[1].rstrip(")"))
        class_name = selected_class.split(" (ID:")[0]

        """Loop through the students in the data manager to find the
        student being edited.
        """
        for student in data_manager.students:
            """If the student is found, check if the selected class is already
            in the student's classes. If it is, either show a warning message
            (if adding) or remove the class (if removing). If the class is
            not in the student's classes, either show a warning message
            (if removing) or add the class (if adding). After adding or
            removing the class, save the student info and show an info
            message. Finally, reload the student's info in the treeview
            to reflect the changes.
            """
            """Check if the current student in the loop is the student being
            edited.
            """
            if student.id == student_id:
                """Check if the selected class is already in the student's
                classes.
                """
                if any(c["class_id"] == class_id for c in student.classes):
                    """If the class is already in the student's classes and
                    the add_or_remove parameter is "add", show a warning
                    message.
                    """
                    if add_or_remove == "add":
                        """If the class is already in the student's classes
                        and the add_or_remove parameter is "add", show a
                        warning message and return.
                        """
                        messagebox.showwarning(
                            "Class Exists",
                            f"{student.full_name()}",
                            f"is already enrolled in {class_name}."
                        )
                        return
                    else:
                        """ If the class is already in the student's classes
                        and the add_or_remove parameter is "remove", remove
                        the class from the student's classes, save the student
                        info, show an info message, and reload the student's
                        info in the treeview.
                        """
                        confirm = messagebox.askokcancel(
                            f"Do you want to remove {class_name}?",
                            f"Remove {class_name} from {student.full_name()}?",
                        )
                        if confirm:
                            student.classes = [
                                c for c in student.classes if c["class_id"]
                                != class_id
                            ]
                            data_manager.save_student_info()
                            reload_solo_student_info(
                                data_manager, student_id, student_list
                            )
                            break
                else:
                    if add_or_remove == "remove":
                        """ If the class is not in the student's classes and
                        the add_or_remove parameter is "remove", show a
                        warning message and return.
                        """
                        messagebox.showwarning(
                            "Class Not Found",
                            f"{student.full_name()}",
                            f"is not enrolled in {class_name}.",
                        )
                        return
                    else:
                        """ If the class is not in the student's classes and
                        the add_or_remove parameter is "add", add the class
                        to the student's classes, save the student info,
                        show an info message, and reload the student's info
                        in the treeview.
                        """
                        confirm = messagebox.askokcancel(
                            f"Do you want to add {class_name}?",
                            f"Add {class_name} to {student.full_name()}?",
                        )
                        if confirm:
                            student.classes.append(
                                {
                                    "class_id": class_id,
                                    "class_name": class_name,
                                    "grade": "N/A",
                                }
                            )
                            data_manager.save_student_info()
                            reload_solo_student_info(
                                data_manager, student_id, student_list
                            )
                            break


def change_grades(
    data_manager, student_id, student_list,
    classes_option_menu, grades_option_menu
):
    """Change the grade of the selected class.

    Changes the grade of the selected class for the student being edited to
    the selected grade.
    """
    selected_class = classes_option_menu.cget("text")
    selected_grade = grades_option_menu.cget("text")
    """If a class and grade are selected from the dropdown menus, proceed
    with changing the grade.
    """
    if selected_class and selected_grade:
        """ The class ID is extracted from the selected class string."""
        class_id = int(selected_class.split("ID: ")[1].rstrip(")"))
        """ Loop through the students in the data manager to find the student
        being edited.
        """
        for student in data_manager.students:
            """ If the student is found, check if the selected class is in
            the student's classes.
            """
            if student.id == student_id:
                found = 0
                """ Loop through the student's classes to find the selected
                class.
                """
                for classes in student.classes:
                    """ If the selected class is found in the student's
                    classes..."""
                    if classes["class_id"] == class_id:
                        """...change the grade of the class to the selected
                        grade, save the student info, show an info message
                        and reload the student's info in the treeview.
                        """
                        confirm = messagebox.askokcancel(
                            "Grade Updated",
                            f"Updated grade for",
                            f"{selected_class.split(' (ID:')[0]} to",
                            f"{selected_grade} for {student.full_name()}.",
                        )
                        if not confirm:
                            return
                        classes["grade"] = selected_grade
                        data_manager.save_student_info()
                        reload_student_list(data_manager, student_list)
                        found += 1
                if found == 0:
                    """ If the selected class is not found in the student's
                    classes, show a warning message.
                    """
                    messagebox.showwarning(
                        "Class Not Found",
                        f"{student.full_name()} is not enrolled in",
                        f"{selected_class.split(' (ID:')[0]}.",
                    )
    reload_solo_student_info(data_manager, student_id, student_list)


def remove_student(data_manager, student_id, student_list):
    """Remove the selected student from the data manager.

    This removes the student from the data manager, saves the student info,
    shows an info message, and reloads the student list in the treeview.
    """
    """Find the student to remove from the data manager's students list using
    the student ID.
    """
    student_to_remove = next(
        (student for student in data_manager.students
            if student.id == student_id),
        None
    )

    """If the student to remove is found, remove the student from the data
    manager's students list, save the student info, show an info message,
    and reload the student list in the treeview.
    If the student is not found, do nothing.
    """
    if student_to_remove:
        data_manager.students.remove(student_to_remove)
        data_manager.save_student_info()
        reload_student_list(data_manager, student_list)
        messagebox.showinfo(
            "Student Removed",
            f"Removed {student_to_remove.full_name()} from the system.",
        )


def add_student(data_manager, add_student_inputs, student_list):
    """Add a new student to the data manager.

    It adds a new student with the entered first and last name to the data
    manager, saves the student info, shows an info message, and reloads
    the student list in the treeview.
    """
    first_name = add_student_inputs[0].get()
    last_name = add_student_inputs[1].get()
    if not first_name or not last_name:
        """If either the first name or last name entry is empty, show
        a warning message and return."""
        messagebox.showwarning(
            "Input Error",
            "Please enter both a first name and last name for the student.",
        )
        return
    """ Generate a new unique ID for the student by finding the maximum
    existing student ID and adding 1. If there are no students, start
    with ID 1.
    """
    new_id = (
        max(student.id for student in data_manager.students) + 1
        if data_manager.students
        else 1
    )
    """ Add the new student to the data manager's students list, save the
    student info, show an info message, and reload the student list in the
    treeview.
    """
    data_manager.students.append(
        Student(
            id=new_id,
            first_name=first_name.capitalize(),
            last_name=last_name.capitalize(),
            classes=[],
        )
    )
    data_manager.save_student_info()
    messagebox.showinfo(
        "Student Added",
        f"Added {first_name} {last_name} to the system with ID {new_id}.",
    )
    """ After adding the student, clear the input fields. The student list
    is reloaded to show the new student.
    """
    reload_student_list(data_manager, student_list)
    for entry in add_student_inputs:
        entry.delete(0, tkinter.END)


def reload_solo_student_info(
    data_manager, student_id, current_selected_student_info_treeview
):
    """Reload the current selected student's info in the treeview.

    This function reloads the current selected student's info in the
    treeview. It is called after adding/removing classes or changing
    grades to reflect the changes in the treeview.
    """
    current_selected_student_info_treeview.delete(
        *current_selected_student_info_treeview.get_children()
    )
    """ Loop through the students in the data manager to find the student
    being edited. If the student is found, extract the class and grade info
    and insert it into the treeview.
    """
    for student in data_manager.students:
        if student.id == student_id:
            grade_info = []
            classes_info = []
            """ Loop through the student's classes to extract the class names
            and grades for display in the treeview.
            """
            for classes in student.classes:
                grade_info.append(
                    f"{classes['class_name']}: {classes['grade']}"
                )
                classes_info.append(
                    f"{classes['class_name']} (ID: {classes['class_id']})"
                )
            """ Insert the student's ID, full name, classes, and grades into
            the treeview.
            """
            current_selected_student_info_treeview.insert(
                "",
                "end",
                values=(
                    student.id,
                    student.full_name(),
                    ", ".join(classes_info),
                    ", ".join(grade_info),
                ),
            )


def reload_student_list(data_manager, student_list):
    """Reload the student list in the treeview.

    This function reloads the student list in the treeview. It is called
    after adding/removing students to reflect the changes in the treeview.
    """
    student_list.delete(*student_list.get_children())
    """ Loop through the students in the data manager and insert their ID
    and full name into the treeview.
    """
    for student in data_manager.students:
        student_list.insert(
            "", "end", values=(student.id, student.full_name())
        )


def back_to_main_menu(callbacks, student_management_frame):
    """Hide the student management frame and return to the main menu.

    This function hides the student management frame and then calls the
    back callback to return to the main menu.
    """
    student_management_frame.place_forget()
    callbacks["back"]()


def back_to_student_management(edit_student_frame):
    """Hide the edit student frame and return to the student management page.

    This function hides the edit student frame, showing the
    student management frame below.
    """
    edit_student_frame.place_forget()
