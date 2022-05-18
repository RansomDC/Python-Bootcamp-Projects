import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

#importing our other modules
import student_main
import student_gui

#Creates a database with the necessary table for our data
def create_db(self):
    conn = sqlite3.connect('students.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        conn.commit
    conn.close()
    first_run(self)


#Enters our first set of data to prevent errors
def first_run(self):
    #the tuple that we use to add our first data to the table
    data = ('Branston', 'Badorette', '696-969-8008', 'Badoretteboy@email.com', 'How to be a dick 101')
    conn = sqlite3.connect('students.db')
    with conn:
        cur = conn.cursor()
        #counts the number of rows in the table
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        #fetchone() returns a single row from a table, it can return none if no rows are available
        count = cur.fetchone() [0]
        if count < 1:
            cur.execute("""INSERT INTO tbl_students(col_fname, col_lname, col_phone, col_email, col_course) VALUES (?,?,?,?,?)""",(data))
            conn.commit()
    conn.close()


def addToList(self):
    var_fname = self.txt_fname.get()    #pull the firstname from the text input area
    var_lname = self.txt_lname.get()
    #normalize the data
    var_fname = var_fname.strip()   #This will remove any blank spaces before and after the user's entry
    var_lname = var_lname.strip()
    var_fname = var_fname.lower().title()   #This will ensure that the first character in each word is capitalized
    var_lname = var_lname.lower().title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    if(len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0):
        conn = sqlite3.connect('students.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO tbl_students(col_fname,col_lname,col_phone,col_email,col_course) \
                    VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_phone,var_email,var_course))
            self.lstList1.insert(END, var_fullname)
            onClear(self)   #Clears all text boxes
        conn.commit()
        conn.close
    else:
        messagebox.showerror("Missing Text Error", "Please ensure that there is data in all four fields.")
    


#A function to clear all of the text inputs
def onClear(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)


def onSelect(self,event):
    varList = event.widget  #event.widget is whatever is triggering the event and we are setting that to varlist
    select = varList.curselection()[0]      #This then gets the selection (curselection) from varlist. Which is returned as a tuple (Which is why we indicated an index number [0]
    value = varList.get(select)     #This gets the value of the tuple in <select> location
    print(value)
    conn = sqlite3.connect('students.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_students WHERE col_fname = (?)""", [value])
        varBody = cursor.fetchall()
        print(varBody)
        self.text.set('{} {}\n\n{}\n\n{}\n\n{}'.format(varBody[0][0],varBody[0][1],varBody[0][2],varBody[0][3],varBody[0][4]))
        #This returns a tuple and we can slice it into 4 parts using data[] during the iteration
#        for data in varBody:
#            self.text.set('{} {}\n\n{}\n\n{}\n\n{}'.format(data[0],data[1],data[2],data[3],data[4],data[5]))

#populate the listbox from the database
def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('students.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
                cursor.execute("""SELECT col_fname FROM tbl_students""")
                varList = cursor.fetchall()[i]
                for item in varList:
                    self.lstList1.insert(0,str(item))
                    i = i + 1
    conn.close()
    

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) #Listbx's selected value
    conn = sqlite3.connect('students.db')
    with conn:
        cur = conn.cursor()
        #check count to ensure that this is not the last record in the database since you cannot delete the last record without an error
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permanently deleted from the database.\n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('students.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_students WHERE col_fname = '{}'""".format(var_select))
                onRefresh(self) #update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()
    
























if __name__ == '__main__':
    pass






