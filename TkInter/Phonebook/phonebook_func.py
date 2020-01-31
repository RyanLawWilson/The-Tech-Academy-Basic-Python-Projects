import tkinter as tk
from tkinter import *
import os
import sqlite3

import phonebook_func
import phonebook_gui



# Centers the window using width and height
def center_window(self, w, h):
    scrW = self.master.winfo_screenwidth()
    scrH = self.master.winfo_screenheight()

    # Calculate the coordinate to position center
    x = int((scrW/2) - (w/2))
    y = int((scrH/2) - (h/2))

    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# When X is clicked, pull up window to confirm.
def ask_quit(self):
    if messagebox.askokcancel("Exit Program","Okay to exit application?"):
        self.master.destroy()
        os._exit(0) # Makes your program release the memory being used.


# Creating the DB
def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("\
            CREATE TABLE if not exists tbl_phonebook (\
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            col_fname TEXT,\
            col_lname TEXT,\
            col_fullname TEXT,\
            col_phone TEXT,\
            col_email TEXT\
            );")
        conn.commit()
    conn.close()
    first_run(self)


# Create a placeholder, dummy account just to populate the db a little
def first_run(self):
    data = ('John', 'Doe', 'John Doe', '111-11-1111', 'jdoe@gmail.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        # Insert placeholder if no records present
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", ('John','Doe','John Doe','111-111-1111','jdoe@email.com'))
            conn.commit()
    conn.close()


# Used to count the number of records in the phonebook.
def count_records(self):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count


#Select item in ListBox
def onSelect(self,event):
    #calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])


def addToList(self):
    # GET INFO FROM TEXTBOXES
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize the data to keep it consistent in the database
    var_fname = var_fname.strip() # Remove any blank spaces before and after the user's entry
    var_lname = var_lname.strip() # This will ensure that the first character in each word is capitalized
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname)) # combine our normailzed names into a fullname
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()

    # Additional input validation for the email
##    if not "@" or not "." in var_email:
##        print("Incorrect email format!!!")

    # If fields not empty, add their info to DB
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and(len(var_email) > 0): # enforce the user to provide both names
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cursor = conn.cursor()
            # Check the database for existance of the fullname, if so we will alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))#,(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if this is 0 then there is no existance of the fullname and we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                self.lstList1.insert(END, var_fullname) # update listbox with the new fullname
                onClear(self) # call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self) # call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")










    
