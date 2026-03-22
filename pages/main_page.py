import tkinter


def load_main_page(frame, callbacks):
    """This function loads the main page of the application. It creates a title label and three buttons for navigating to the student management page, viewing students, and exiting the application. The buttons are linked to their respective callback functions passed in the callbacks dictionary."""
    title = tkinter.Label(frame, text="Student Management System")
    student_management_button = tkinter.Button(
        frame, text="Student Management", command=callbacks["student_management"]
    )
    """ The view students button opens a new window that displays a list of all students in the system. """
    view_students_button = tkinter.Button(
        frame, text="View Students", command=callbacks["view_students"]
    )
    exit_button = tkinter.Button(frame, text="Exit", command=callbacks["exit_app"])
    """ The title and buttons are placed on the frame. """
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=tkinter.CENTER)
    student_management_button.place(
        relx=0.5, rely=0.25, relwidth=0.15, relheight=0.05, anchor=tkinter.CENTER
    )
    view_students_button.place(
        relx=0.5, rely=0.35, relwidth=0.15, relheight=0.05, anchor=tkinter.CENTER
    )
    exit_button.place(relx=0.5, rely=0.45, relwidth=0.15, relheight=0.05, anchor=tkinter.CENTER)
