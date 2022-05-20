
import tkinter
from tkinter import *

import page_gen_gui
import page_gen_func

#Define our maste frame config
class parentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__ (self)
        self.master = master
        master.geometry('{}x{}'.format(400,200))
        self.master.title('Create Web Page')
        
        page_gen_gui.load_gui(self)




if __name__ == '__main__':
    root = Tk()
    App = parentWindow(root)
    root.mainloop()
