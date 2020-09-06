from tkinter import *


def New_file():
    print("this is new file")


def Open_file():
    print("Opening File")


def Save_file():
    print("Saving file")


def as_file():
    print("save as file ")


def Undo_text():
    print("Undo text ")


def Cut_text():
    print("Cut text ")


def Copy_text():
    print("Text Copied ")


def Paste_text():
    print("Text is paste ")


def Redo_text():
    print("Text is Redo")


def Font_view():
    print("Font viewed ")


def Zoom_view():
    print("Text is Zoom in ")


def Out_view():
    print("Text is Zoom Out ")


def Restore_view():
    print("All func.. is Restored")


def View_help():
    print("How can i help you")


def Send_Feedback():
    print("You can leave your msg  ")


def About_help():
    print("Nothing is here ")


window = Tk()
window.geometry("400x300+120+120")
window.resizable(0, 0)
window.title("Menu Bar")
window.config(bg="light blue")

menu_bar = Menu(window)
window.config(menu=menu_bar)

# ============FILE MENU====in_First_window ==========
filemenu = Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New File", command=New_file)
filemenu.add_command(label="Open", command=Open_file)
filemenu.add_command(label="Save", command=Save_file)
filemenu.add_command(label="Save as", command=as_file)

# ==============EDIT MENU=============
editmenu = Menu(menu_bar)
menu_bar.add_cascade(label="Edit", menu=editmenu)

editmenu.add_command(label="Undo", command=Undo_text)
editmenu.add_command(label="Redo", command=Redo_text)
editmenu.add_command(label="Copy", command=Copy_text)
editmenu.add_command(label="Cut", command=Cut_text)
editmenu.add_command(label="Paste", command=Paste_text)

# =============VIEW MENU===============
view_menu = Menu(menu_bar)
menu_bar.add_cascade(label="View", menu=view_menu)

view_menu.add_command(label="Font", command=Font_view)
view_menu.add_command(label="Zoom In", command=Zoom_view)
view_menu.add_command(label="Zoom out", command=Out_view)
view_menu.add_separator()
view_menu.add_command(label="Restore", command=Restore_view)

# ================HELP MENU============
Help_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu=Help_menu)

Help_menu.add_command(label="View Help", command=View_help)
Help_menu.add_command(label="Send Feedback", command=Send_Feedback)
Help_menu.add_separator()
Help_menu.add_command(label="About", command=About_help)

window.mainloop()
