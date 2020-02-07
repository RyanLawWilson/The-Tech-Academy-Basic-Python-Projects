'''
    Requirements:
        - Two buttons to pick source and destination folder.
            + Show these paths in text fields
        - Execute button - Search for .txt in source, cut and paste in destination.
        - Record the files that were moved and time stamps in DB
        - Print text files and time stamps to the console.
'''

import os
import time
import re # regular expression to prevent bad input
import shutil  # For moving files
import tkinter
from tkinter import *
from tkinter import filedialog
import sqlite3

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
                
        # Centering the window
        windowWidth = 580
        windowHeight = 200
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        x = int((screenWidth/2) - (windowWidth/2))
        y = int((screenHeight/2) - (windowHeight/2))


        # Master Modifications
        self.master = master
        self.master.geometry('{}x{}+{}+{}'.format(windowWidth,windowHeight,x,y))
        self.master.title("Moving text files")
        self.master.config(bg="white")
        self.master.resizable(width=False, height=False)


        # ========== Buttons ==========
        # ===== Browse =====
        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1, command=self.pickSource)
        self.btnBrowse1.grid(row=0, column=0, pady=(50,5), padx=(10,15))
        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1, command=self.pickDestination)
        self.btnBrowse2.grid(row=1, column=0, pady=(5,5), padx=(10,15))
        # ===== Check for Files =====
        self.chk4files = Button(self.master, text="Check for Files...", width=12, height=2, command=self.moveTextFiles)
        self.chk4files.grid(row=2, column=0, pady=(5,5), padx=(10,15))
        # ===== Close Program =====
        self.closeProgram = Button(self.master, text="Close Program", width=12, height=2, command=self.closeProgram)
        self.closeProgram.grid(row=2, column=2, pady=(5,5), padx=(10,15), sticky=NE)


        # ========== Labels ==========
        self.sourceLabel = Label(self.master, text="Source", bg='white')
        self.sourceLabel.grid(row=0, column=1, pady=(50,5))
        self.destinationLabel = Label(self.master, text="Destination", bg='white')
        self.destinationLabel.grid(row=1, column=1)
        

        # ========== Text Boxes ==========
        self.strvar_sourcePath = StringVar()
        self.txtbox_source = Entry(self.master, text=self.strvar_sourcePath, fg='black', width=62)
        self.txtbox_source.grid(row=0, column=2, padx=(10,10), pady=(50,5))
        self.strvar_destinationPath = StringVar()
        self.txtbox_destination = Entry(self.master, text=self.strvar_destinationPath, fg='black', width=62)
        self.txtbox_destination.grid(row=1, column=2, padx=(10,10), pady=(5,5))

        
    def pickSource(self):
        self.strvar_sourcePath.set(tkinter.filedialog.askdirectory())
        

    
    def pickDestination(self):
        self.strvar_destinationPath.set(tkinter.filedialog.askdirectory())
        

    def closeProgram(self):
        self.master.destroy()
        os._exit(0) # Makes your program release the memory being used.


    # Cuts .txt files from source and pastes in destination
    def moveTextFiles(self):
        # Replaced / with \ for use with os
        sourceDir = self.strvar_sourcePath.get().replace('/','\\').strip()
        destinationDir = self.strvar_destinationPath.get().replace('/','\\').strip()

        numOfTxtFiles = 0
        numOfTxtFilesMoved = 0

        # Regex to check if sourceDir is correct format.  Test if path exists
        if (re.match(r"^[A-Z]:\\([A-z0-9-_ +]+\\)*([A-z0-9 ]*)$", sourceDir) and os.path.exists(sourceDir))\
            and (re.match(r"^[A-Z]:\\([A-z0-9-_ +]+\\)*([A-z0-9 ]*)$", destinationDir) and os.path.exists(destinationDir)):
            
            movedFilesList = [] # record what files were moved
            
            for i in os.listdir(sourceDir):
                absolutePath = os.path.join(sourceDir, i)
                
                # Only print if it's a text file
                if i.endswith("txt"):
                    numOfTxtFiles += 1
                    epochTime = os.path.getmtime(absolutePath) # os.path.getmtime() gets the seconds since January 1, 1970
                    modifiedTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epochTime)) # time.strftime() converts epoch time to readable time

                    # Move files and add them to DB
                    shutil.move(absolutePath, destinationDir)
                    addToDB(self, i, modifiedTime)
                    numOfTxtFilesMoved += 1
                    movedFilesList.append(i)

            # Show the 
            if numOfTxtFilesMoved > 0:
                showDBFiles(self, movedFilesList)
                movedFilesList.clear()
            
            # Prints text based on number of txt files in the folder.  Shows source and destination folders       
            if (numOfTxtFiles > 0):
                print("{} files moved from\n{}\nto\n{}".format(numOfTxtFilesMoved, sourceDir, destinationDir))
            else:
                print("There are no .txt files in {}!".format(sourceDir))
        else:
            print("The source path and destination path must be valid!")
        

# Create the Database table
def createDBTables():
    conn = sqlite3.connect("fileRecords.db")
    with conn:
        cur = conn.cursor()
        cur.execute("\
            CREATE TABLE IF NOT EXISTS TextFiles (\
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            fileName VARCHAR,\
            modificationDate VARCHAR\
            );")
        conn.commit()
    conn.close()


# Add a record to the DB if it's a new file
def addToDB(self, fileName, date):
    conn = sqlite3.connect("fileRecords.db")
    with conn:
        cur = conn.cursor()
        cur.execute("\
            SELECT COUNT(fileName) FROM TextFiles\
            WHERE fileName = '{}';".format(fileName))
        count = cur.fetchall()[0][0]
        if (count > 0):
            print("{} already exists in the database.".format(fileName))
        else:
            cur.execute("\
                INSERT INTO TextFiles \
                (fileName, modificationDate)\
                VALUES\
                (?,?);", (fileName, date))
            print("{} added to the database.".format(fileName))
        conn.commit()
    conn.close()


# Show the contents in the database of the files that moved
def showDBFiles(self, movedFilesList):
    print("===== List of moved files =====")
    
    conn = sqlite3.connect("fileRecords.db")
    with conn:
        cur = conn.cursor() 
        cur.execute("\
            SELECT fileName, modificationDate FROM TextFiles;")

        # Display the data if that file was moved
        for r in cur.fetchall():
            string = ""
            if r[0] in movedFilesList:
                for c in r:
                    string += "{} \t".format(c)
                print("{}\n".format(string))
                
        conn.commit()
    conn.close()


if __name__ == "__main__":
    createDBTables()    # Calling createDBTables
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    






