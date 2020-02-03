import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)


        # Centering the window
        windowWidth = 500
        windowHeight = 175
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        x = int((screenWidth/2) - (windowWidth/2))
        y = int((screenHeight/2) - (windowHeight/2))


        # Too lazy to type self.master
        ms = self.master
        ms = master
        ms.geometry('{}x{}+{}+{}'.format(windowWidth,windowHeight,x,y))
        ms.title("Check Files")
        ms.config(bg="white")
        ms.resizable(width=False, height=False)


        # ========== Buttons ==========
        # ===== Browse =====
        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse1.grid(row=0, column=0, pady=(50,5), padx=(10,15))
        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse2.grid(row=1, column=0, pady=(5,5), padx=(10,15))
        # ===== Check for Files =====
        self.chk4files = Button(self.master, text="Check for Files...", width=12, height=2)
        self.chk4files.grid(row=2, column=0, pady=(5,5), padx=(10,15))
        # ===== Close Program =====
        self.closeProgram = Button(self.master, text="Close Program", width=12, height=2)
        self.closeProgram.grid(row=2, column=1, pady=(5,5), padx=(10,15), sticky=NE)


        # ========== Text Boxes ==========
        self.textBox1_text = StringVar()
        self.textBox1 = Entry(self.master, text=self.textBox1_text, fg='black', width=60)
        self.textBox1.grid(row=0, column=1, padx=(5,10), pady=(50,5))
        self.textBox2_text = StringVar()
        self.textBox2 = Entry(self.master, text=self.textBox1_text, fg='black', width=60)
        self.textBox2.grid(row=1, column=1, padx=(5,10), pady=(5,5))



if __name__ == "__main__":
    # Instantiating Tkinter
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
