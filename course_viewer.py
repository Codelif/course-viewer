from ttkbootstrap.dialogs.dialogs import Messagebox, MessageDialog
from tkinter.filedialog import askdirectory
from ttkbootstrap.constants import *
import ttkbootstrap as ttk

import webbrowser
import os

from project.index_files import main

def callback(url):
    webbrowser.open_new_tab(url)

root = ttk.Window()
root.title("Course Viewer")
root.geometry("700x125")
root.minsize(700, 125)
root.maxsize(700, 125)

folder_path = ttk.StringVar()

def validate_path():
    path = folder_path.get()
    if not os.path.isabs(path):
        Messagebox.show_error("Please enter a absolute path. Alternatively use the path picker.", "Viewer Installer")
    elif path != "":
        path = os.path.abspath(path)


        url = main(path, os.path.abspath(os.path.dirname(__file__)))
        def browser():
            webbrowser.open_new_tab("file://" + url) 
        openin = MessageDialog("Course Viewer installed in parent folder '%s'.\nStart the app by opening 'course-viewer.html' in a modern browser." % os.path.join(path, "course-viewer"), "Viewer Installer", ["Open in Browser:primary"], command=browser)
        openin.show()
        
        
        # Messagebox.show_info("Course Viewer installed in parent folder '%s'.\nStart the app by opening 'viewer.html' in a modern browser." % os.path.join(path, "course-viewer"), "Viewer Installer")
        
        root.destroy()
    elif path == "":
        Messagebox.show_error("Directory path cannot be empty", "Viewer Installer", "Viewer Installer")
    else:
        Messagebox.show_error("An error has occured. Please restart the application.", "Viewer Installer")

def update_entry():
    folder_path.set(askdirectory())


ttk.Label(root, text="Course Viewer", font="TkDefaultFont 18 bold").grid(row=0, column=1, pady=7)

ttk.Label(root, text="Choose Directory: ").grid(row=1, column=0)
ttk.Entry(root, width=60, textvariable=folder_path).grid(row=1, column=1)
ttk.Button(root, text="Choose", command=update_entry).grid(row=1, column=2, padx=5)

ttk.Button(root, text="Install Viewer!", command=validate_path).grid(row=2, column=1, pady=7)


root.mainloop()


