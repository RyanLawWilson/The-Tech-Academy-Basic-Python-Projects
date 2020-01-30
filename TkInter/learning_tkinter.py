import tkinter
from tkinter import *

class ParentWindow(Frame):
    # __init__ is like the constructor: it's the first function that is run
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter')
        self.master.config(bg = 'lightgray')

        self.varFName = StringVar()
        self.varLName = StringVar()

        # Making labels
        self.lblFName = Label(self.master, text="First Name: ", font=("Helvetica", 16), fg="black", bg="lightgray")
        self.lblFName.grid(row=0, column=0, padx=(30,10), pady=(30,0))
        self.lblLName = Label(self.master, text="Last Name: ", font=("Helvetica", 16), fg="black", bg="lightgray")
        self.lblLName.grid(row=1, column=0, padx=(30,10), pady=(30,0))
        self.lblDisplay = Label(self.master, font=("Helvetica", 16), fg="black", bg="lightgray")
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        # Building textboxs
        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16), fg="black", bg="lightblue")
        self.txtFName.grid(row=0, column=1, padx=(0,0), pady=(30,0)) # Place textbox on the frame
        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 16), fg="black", bg="lightblue")
        self.txtLName.grid(row=1, column=1, padx=(0,0), pady=(30,0))
        
        # Buttons
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit) # Don't put parenthesis after submit or cancel methods
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE) # Sticky is like text-align
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NW) # Sticky is like text-align

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        # Use config to change something while the program is running
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

    def cancel(self):
        self.master.destroy()   # Closes the window








if __name__ == "__main__":
    # Instantiating Tkinter
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()








    
