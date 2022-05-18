
from tkinter import *
import tkinter as tk

#Other modules we wrote for this program
import student_gui
import student_func

#Frame is the Tkinter fram class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)

        #define our master frame configuration
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        #Built in method to catch i fthe user click the upper corner "X"
        arg = self.master

        #load the GUI
        student_gui.load_gui(self)


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
 
