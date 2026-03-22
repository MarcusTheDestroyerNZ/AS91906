"""This is the main file for the student management system application.

It sets up the main window and manages the different frames for the main
page, student management page, and view students page. The DataManager
class is used to load and manage the student data from a JSON file.
The application allows users to navigate between different pages
and view or edit student information.
"""

import tkinter
from data_manager import DataManager
from pages.main_page import load_main_page
from pages.student_management import load_student_management_page
from pages.view_students_page import load_view_students_page

"""The main window is created and configured with a title, size,
and background color.
"""
window = tkinter.Tk()
window.geometry("1280x720")
window.title("Student Management System")
window.config(background="grey")

"""Frames for different pages of the application are created and
stored in a dictionary for easy access. Each frame is configured with
a grey background.
"""
main_page_frame = tkinter.Frame(window, bg="grey")
student_management_frame = tkinter.Frame(window, bg="grey")
teacher_management_frame = tkinter.Frame(window, bg="grey")
view_students_frame = tkinter.Frame(window, bg="grey")
view_classes_frame = tkinter.Frame(window, bg="grey")
edit_students_frame = tkinter.Frame(window, bg="grey")

"""The frames are stored in a dictionary for easy access when switching
between pages.
"""
frames = {
    "main": main_page_frame,
    "student_management": student_management_frame,
    "view_students": view_students_frame,
    "edit_students": edit_students_frame,
}

"""The place_frame_values dictionary contains the parameters for placing
the frames on the window. This allows for consistent placement of frames
when switching between pages.
"""
place_frame_values = {
    "relx": 0.5,
    "rely": 0.5,
    "relwidth": 1,
    "relheight": 1,
    "anchor": tkinter.CENTER,
}

"""The DataManager instance is created to manage the student, teacher,
and class data. It loads the data from the JSON file when initialized.
"""
data_manager = DataManager()


def clear_all_frames():
    """This function hides all frames by calling the place_forget method
    on each frame in the frames dictionary. 
    
    This is used to clear the current view before showing a new page.
    """
    for frame in frames.values():
        frame.place_forget()


def show_frame(frame):
    """This function takes a frame as an argument, clears all frames,
    and then places the specified frame on the window using the parameters
    defined in place_frame_values. This is used to switch between different
    pages of the application.
    """
    clear_all_frames()
    load_pages()
    frame.place(**place_frame_values)


def open_main_page():
    """This function shows the main page frame by calling the show_frame
    function with the main_page_frame as an argument.
    """
    show_frame(main_page_frame)


def open_student_management_page():
    """This function shows the student management page frame by calling
    the show_frame function with the student_management_frame as an argument.
    """
    show_frame(student_management_frame)


def open_view_students_page():
    """This function shows the view students page frame by calling
    the show_frame function with the view_students_frame as an argument.
    """
    show_frame(view_students_frame)


def open_edit_students_page(student=None):
    """This function shows the edit students page frame by calling
    the show_frame function with the edit_students_frame as an argument.
    """
    show_frame(edit_students_frame)


def exit_program():
    """This function exits the program by calling the destroy method
    on the main window.
    """
    window.destroy()


def load_pages():
    """This function loads the different pages of the application by
    calling the respective load functions for each page.
    It also sets up the callback functions for navigation between pages.
    """

    """Callback functions for the main page buttons.
    These functions are passed to the load_main_page function to
    handle navigation when the buttons are clicked.
    """
    main_callbacks = {
        "exit_app": exit_program,
        "student_management": open_student_management_page,
        "view_students": open_view_students_page,
    }
    """Load the main page with the specified callbacks."""
    load_main_page(main_page_frame, main_callbacks)

    """Callback functions for the student management page buttons.
    These functions are passed to the load_student_management_page
    function to handle navigation when the buttons are clicked.
    """
    student_management_callbacks = {
        "back": open_main_page,
        "edit_student": edit_students_frame,
    }
    """Load the student management page with the specified callbacks
    and the data manager instance to manage student data.
    """
    load_student_management_page(
        student_management_frame, data_manager, student_management_callbacks
    )

    """Callback functions for the view students page buttons.
    These functions are passed to the load_view_students_page function
    to handle navigation when the buttons are clicked.
    """
    view_students_callbacks = {"back": open_main_page}
    """Load the view students page with the specified callbacks
    and the data manager instance to manage student data.
    """
    load_view_students_page(view_students_frame, data_manager, view_students_callbacks)

"""The load_pages function is called to initialize the pages of the
application, and the main page is shown by default when the application
starts. Finally, the main event loop is started to run the application.
"""
load_pages()
show_frame(main_page_frame)

window.mainloop()
