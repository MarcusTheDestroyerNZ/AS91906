from tkinter import *
from data_manager import DataManager
from pages.main_page import load_main_page
from pages.student_management import load_student_management_page
from pages.teacher_management_page import load_teacher_management_page
from pages.view_students_page import load_view_students_page
from pages.view_classes_page import load_view_classes_page
from pages.add_or_remove_students_page import load_add_or_remove_students_page

window = Tk()
window.geometry("1280x720")
window.title("Stu" \
"dent Management System")
window.config(background="grey")

main_page_frame = Frame(window, bg="grey")
student_management_frame = Frame(window, bg="grey")
teacher_management_frame = Frame(window, bg="grey")
view_students_frame = Frame(window, bg="grey")
view_classes_frame = Frame(window, bg="grey")
add_or_remove_students_frame = Frame(window, bg="grey")

frames = {
    "main": main_page_frame,
    "student_management": student_management_frame,
    "teacher_management": teacher_management_frame,
    "view_students": view_students_frame,
    "view_classes": view_classes_frame,
    "add_or_remove_students": add_or_remove_students_frame
}

place_frame_values = {"relx": 0.5, "rely": 0.5, "relwidth": 1, "relheight": 1, "anchor": CENTER}

data_manager = DataManager()

def clear_all_frames():
    for frame in frames.values():
        frame.place_forget()

def show_frame(frame):
    clear_all_frames()
    frame.place(**place_frame_values)

def open_main_page():
    show_frame(main_page_frame)

def open_student_management_page():
    show_frame(student_management_frame)

def open_teacher_management_page():
    show_frame(teacher_management_frame)

def open_view_students_page():
    show_frame(view_students_frame)

def open_view_classes_page():
    show_frame(view_classes_frame)

def exit_program():
    window.destroy()

def load_pages():
    main_callbacks = {'exit_app': exit_program, 'student_management': open_student_management_page, 'teacher_management': open_teacher_management_page, 'view_students': open_view_students_page, 'view_classes': open_view_classes_page}
    load_main_page(main_page_frame, main_callbacks)

    student_management_callbacks = {'back': open_main_page, 'add_or_remove_students': lambda: show_frame(add_or_remove_students_frame)}
    load_student_management_page(student_management_frame, data_manager, student_management_callbacks)

    teacher_management_callbacks = {'back': open_main_page}
    load_teacher_management_page(teacher_management_frame, data_manager, teacher_management_callbacks)

    view_students_callbacks = {'back': open_main_page}
    load_view_students_page(view_students_frame, data_manager, view_students_callbacks)

    view_classes_callbacks = {'back': open_main_page}
    load_view_classes_page(view_classes_frame, data_manager, view_classes_callbacks)

    add_or_remove_students_callbacks = {'back': open_student_management_page}
    load_add_or_remove_students_page(add_or_remove_students_frame, data_manager, add_or_remove_students_callbacks)

load_pages()
show_frame(main_page_frame)

window.mainloop()