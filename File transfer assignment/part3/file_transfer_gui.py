from tkinter import *
import tkinter
import tkinter.filedialog

import file_transfer_main
import file_transfer_func

def create_ui(self):
    #labels
    self.lbl_source = Label(self.master,text='File Source:')
    self.lbl_source.grid(row=0,column=1,pady=(15,0),sticky=W)

    self.lbl_destination = Label(self.master,text='File Destination:')
    self.lbl_destination.grid(row=2,column=1,sticky=W)
    
    #buttons
    self.btn_browse_source = Button(self.master, text='Browse...',command=lambda: file_transfer_func.selectSource(self))
    self.btn_browse_source.grid(row=1,column=0,sticky=E+W,padx=(10),pady=(0,10))     

    self.btn_browse_dest = Button(self.master, text='Browse...',command=lambda: file_transfer_func.selectDest(self))
    self.btn_browse_dest.grid(row=3,column=0,sticky=E+W,padx=(10),pady=(0,10))  

    self.btn_transfer = Button(self.master, text='Transfer Files...',command=lambda: file_transfer_func.transfer(self))
    self.btn_transfer.grid(row=4,column=0,sticky=E+W,padx=(10),pady=(20,10))    
    
    #Entries
    self.inp_source = Entry(self.master, text='',width=45)
    self.inp_source.grid(row=1,column=1,columnspan=2,sticky=E+W)
    
    self.inp_destination = Entry(self.master, text='')
    self.inp_destination.grid(row=3,column=1,columnspan=2,sticky=E+W)



if __name__ == '__main__':
    pass
