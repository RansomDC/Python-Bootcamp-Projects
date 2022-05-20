import tkinter
from tkinter import *
import tkinter.filedialog

class parentWindow(Frame):
    def __init__(self, master):
        Frame.__init__ (self)
        self.master = master
        master.geometry('{}x{}'.format(400,200))
        self.master.title('Check files')


        #buttons
        self.btn_browse1 = Button(self.master, text='Browse...',command=lambda: test())
        self.btn_browse1.grid(row=0,column=0,sticky=E+W,padx=(10),pady=(30,10))     

        self.btn_browse2 = Button(self.master, text='Browse...')
        self.btn_browse2.grid(row=1,column=0,sticky=E+W,padx=(10),pady=(10))  

        self.btn_check = Button(self.master, text='Check for Files...')
        self.btn_check.grid(row=2,column=0,sticky=E+W,padx=(10),pady=(10))  

        self.btn_close = Button(self.master, text='Close Program')
        self.btn_close.grid(row=2,column=2,sticky=E,padx=(175,0))  
        
        #Entries
        self.inp_one = Entry(self.master, text='')
        self.inp_one.grid(row=0,column=1,columnspan=2,sticky=E+W,pady=(30,0))
        
        self.inp_two = Entry(self.master, text='')
        self.inp_two.grid(row=1,column=1,columnspan=2,sticky=E+W)


        def test():
            selDir = str(tkinter.filedialog.askdirectory())
            self.inp_one.insert(END,selDir)


if __name__ == '__main__':
    root = Tk()
    App = parentWindow(root)
    root.mainloop()
