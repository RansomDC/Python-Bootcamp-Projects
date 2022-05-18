#Version:   Python 3.10.4
#
#Author:    Ransom Cadorette
#
#Description: A practice program for learning Python and creating a GUI with tkinter
#while using OOP and parent/child realationships. All code copied from the Tech
#Academy's curriculum.
#
#Tested OS: Windows 10
#


from tkinter import *
import tkinter as tk

#Other modules we wrote for this program
import phonebook_gui
import phonebook_func


#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)

        #define our master fram configuration
        self.master = master
        self.master.minsize(500,300) #(height, Width)
        self.master.maxsize(500,300)
        #This centerWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook practice")
        self.master.configure(bg="#F0F0F0")
        #This protocol method is a tkinter built-in method to catch if the
        #user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #load in the GUI widgets from a separate module.
        #keeping you code compartmentalized and clutter free
        phonebook_gui.load_gui(self)



if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
