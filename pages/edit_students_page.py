from tkinter import *

def load_edit_students_page(frame, data_manager, callbacks):
    back_button = Button(frame, text="Back", command= lambda: callbacks['back']())
    back_button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05, anchor=CENTER)

    title = Label(frame, text=f"Editing Student...")
    title.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.05, anchor=CENTER)

    