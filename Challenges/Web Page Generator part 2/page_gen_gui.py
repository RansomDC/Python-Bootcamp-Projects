import tkinter
from tkinter import *

import page_gen_main
import page_gen_func


def load_gui(self):
    #labels
    self.lbl_filename = Label(self.master, text='Input your file name here!')
    self.lbl_filename.grid(row=0,column=0)

    self.lbl_content = Label(self.master, text='Input you web content here!')
    self.lbl_content.grid(row=1,column=0)

    #Entry/Inputs
    self.inp_filename = Entry(self.master, text='')
    self.inp_filename.grid(row=0,column=1)

    self.inp_content = Entry(self.master,text='')
    self.inp_content.grid(row=1,column=1)

    #Button
    self.btn_create = Button(self.master,text='Generate your webpage!',command=lambda: page_gen_func.generate(self))
    self.btn_create.grid(row=2,column=0,columnspan=2)





if __name__ == '__main__':
    pass
