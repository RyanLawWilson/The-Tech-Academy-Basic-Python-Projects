
import tkinter as tk
from tkinter import *

import phonebook_func
import phonebook_gui

# ParentWindow is a tkinter frame - alows us to use tkinter objects
class ParentWindow(Frame)
    def __init__ (self, master, **args, **kwargs)
        Frame.__init__(self, master, **args, **kwargs)

        self.master = master
        self.master.title("Tkinter Phonebook")
        self.master.configure(bg="#F0F0F0")

        # Sets max / min size of window to same to jebait people.
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)

        # Center the screen
        phonebook_func.center_window(self, 500, 300)

        # When the user clicks the X, a window will show up to ask them to confirm.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))

        phonebook_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    # Prevents program from immediately dissapearing when run
    root.mainloop()


        
