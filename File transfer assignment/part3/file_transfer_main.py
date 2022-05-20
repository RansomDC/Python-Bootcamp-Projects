import shutil
import os
import datetime as dt
from tkinter import *
import tkinter

import file_transfer_gui
import file_transfer_func

class parentWindow(Frame):
    def __init__(self, master):
        Frame.__init__ (self)
        self.master = master
        master.geometry('{}x{}'.format(400,200))
        self.master.title('Check files')

        file_transfer_gui.create_ui(self)


if __name__ == '__main__':
    root = Tk()
    App = parentWindow(root)
    root.mainloop()
