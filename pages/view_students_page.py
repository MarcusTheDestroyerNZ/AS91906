"""This file defines the view students page for the application."""

import tkinter
from tkinter import ttk


def load_view_students_page(frame, data_manager, callbacks):
    """Load the view students page.

    It displays a treeview that shows a list of students along with their
    classes and grades. The student data is retrieved from the data manager
    and displayed in the treeview.
    """
    """The back button allows the user to return to the main menu."""
    back_button = tkinter.Button(frame, text="Back", command=callbacks[
        "back"
    ])
    back_button.place(
        relx=0.2,
        rely=0.1,
        relwidth=0.1,
        relheight=0.05,
        anchor=tkinter.CENTER
    )

    """Title label."""
    title = tkinter.Label(frame, text="View Students Page")
    title.place(
        relx=0.5,
        rely=0.1,
        relwidth=0.2,
        relheight=0.05,
        anchor=tkinter.CENTER
    )

    """ The treeview is set up with columns for ID, Name,
    Classes, and Grades.
    """
    headings = ["ID", "Name", "Classes", "Grades"]
    student_tree = ttk.Treeview(frame, columns=headings, show="headings")
    student_tree.place(
        relx=0.5, rely=0.3, relwidth=0.8, relheight=0.6, anchor=tkinter.N
    )

    """The treeview columns are configured with appropriate headings
    and widths.
    """
    for heading in headings:
        student_tree.heading(heading, text=heading)
        student_tree.column(heading, width=50, stretch=True)
    student_tree.column("Grades", width=150)
    student_tree.rowconfigure(2, weight=1)

    """Loop through the students in the data manager and insert their
    information into the treeview.
    """
    for student in data_manager.students:
        grade_info = []
        classes_names = []
        """Loop through the student's classes to extract the class names and
        grades for display in the treeview.
        """
        for classes in student.classes:
            grade_info.append(f"{classes['class_name']}: {classes['grade']}")
            classes_names.append(f"{classes['class_name']}")

        """Insert the student's ID, full name, classes, and grades into the
        treeview.
        """
        student_tree.insert(
            "",
            "end",
            values=(
                student.id,
                student.full_name(),
                ", ".join(classes_names),
                ", ".join(grade_info),
            ),
        )
