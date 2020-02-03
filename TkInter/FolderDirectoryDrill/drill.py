import tkinter
from tkinter import *
# For some reason, I have to specify what has to be imported.
# The * doesn't seem to do anything
from tkinter import filedialog

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        # Centering the window
        windowWidth = 600
        windowHeight = 350
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        x = int((screenWidth/2) - (windowWidth/2))
        y = int((screenHeight/2) - (windowHeight/2))

        # Editing Master
        self.master = master
        self.master.geometry('{}x{}+{}+{}'.format(windowWidth,windowHeight,x,y))
        self.master.title("Check Files")
        self.master.config(bg="white")
        self.master.resizable(width=False, height=False)

        # Browse Button
        self.btnBrowse = Button(self.master, text="Pick a File ...", height=2, font=("monospace", 18), command=self.pickAFolder)
        self.btnBrowse.pack(fill=X, padx=(50,50), pady=(50,50))

        # Label
        self.pathText = StringVar()
        self.pathText.set("File Path will be here")
        # For some reason, the label only updates if I use textvariable, not text
        self.pathLabel = Label(self.master, textvariable=self.pathText, font=("Helvetica", 14), fg="green", bg='white')
        self.pathLabel.pack(padx=(10,10), pady=(50,20))

        
    def pickAFolder(self):
        self.folderPath = tkinter.filedialog.askdirectory()
        print(self.folderPath) # This is working
        self.pathText.set(self.folderPath)



if __name__ == "__main__":
    # Instantiating Tkinter
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
