from tkinter import *
import tkinter as tk

#importing our other modules
import student_main
import student_func

def load_gui(self):
    print("farts")

    #create the labels
    self.lbl_fname = tk.Label(self.master, text='First Name: ')
    self.lbl_fname.grid(row=0,column=0,sticky=W,padx=(5,10),pady=(10,0))
    self.lbl_lname = tk.Label(self.master, text='Last Name: ')
    self.lbl_lname.grid(row=2,column=0,sticky=W,padx=(5,10),pady=(10,0))
    self.lbl_phone = tk.Label(self.master, text='Phone Number: ')
    self.lbl_phone.grid(row=4,column=0,sticky=W,padx=(5,10),pady=(10,0))
    self.lbl_email = tk.Label(self.master, text='Email Address: ')
    self.lbl_email.grid(row=6,column=0,sticky=W,padx=(5,10),pady=(10,0))
    self.lbl_course = tk.Label(self.master, text='Current Course: ')
    self.lbl_course.grid(row=8,column=0,sticky=W,padx=(5,10),pady=(10,0))

    #Create the inputs
    self.txt_fname = tk.Entry(self.master, text='')
    self.txt_fname.grid(row=1,column=0,padx=(5,0))
    self.txt_lname = tk.Entry(self.master, text='')
    self.txt_lname.grid(row=3,column=0,padx=(5,0))
    self.txt_phone = tk.Entry(self.master, text='')
    self.txt_phone.grid(row=5,column=0,padx=(5,0))
    self.txt_email = tk.Entry(self.master, text='')
    self.txt_email.grid(row=7,column=0,padx=(5,0))
    self.txt_course = tk.Entry(self.master, text='')
    self.txt_course.grid(row=9,column=0,padx=(5,0))

    #Create Listbox
    self.lstList1 = Listbox(self.master,exportselection=0,width=20)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: student_func.onSelect(self,event))       #add event listener to selecting an item in the list
    self.lstList1.grid(row=1,column=1,rowspan=9,columnspan=1, sticky=N+S, padx=(10,10))

    #Create Outpus space that is changed when an item in the listbox is selected.
    self.text = tk.StringVar()
    self.text.set("")
    self.lbl_output = tk.Label(self.master,textvariable=self.text,width=20)     #,text='{} {}\n\n{}\n\n{}\n\n{}'.format('Brittany','Jobs','1234567891','Bjobs@email.com','health 069'),bg='lightgray'
    self.lbl_output.grid(row=1,column=3,rowspan=9, sticky=N+S+E+W)

    #Create buttons for adding and deleting new students
    self.btn_add = tk.Button(self.master,text='Add',command=lambda: student_func.addToList(self))
    self.btn_add.grid(row=10,column=0)
    self.btn_delete = tk.Button(self.master,text='Delete',command=lambda: student_func.onDelete(self))
    self.btn_delete.grid(row=10,column=1)

    student_func.create_db(self)
    student_func.onRefresh(self)


if __name__ == '__main__':
    pass
