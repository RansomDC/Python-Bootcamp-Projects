import shutil
import os
import datetime as dt
import tkinter
from tkinter import *


import file_transfer_main
import file_transfer_gui

def transfer(self):
    today = dt.datetime.now().date()
    
    #Obtain the list of files that are in the starting folder
    source = os.listdir(self.inp_source.get())
    for file in source:
        filepath = (self.inp_source.get() + "/" + file)
        
        #fromtimestamp translates the getmtime which is the time since a file was edited
        #to a date useable by datetime.
        #(getmtime is represented by a floating point in seconds since a specific epoch)
        filetime = dt.datetime.fromtimestamp(os.path.getmtime(filepath))
        
        #convert filetime to the same format as the 'today' variable
        filetime_con = filetime.date()
        
        if filetime_con == today:
            #set the destination path to folder-B
            destination = self.inp_destination.get()

            #Move the current file
            shutil.move(filepath, destination)

#Gets the directory name from the explorer and outputs it to the source Entry element
def select(self, var):
    if var == 1:
        selDir = str(tkinter.filedialog.askdirectory())
        self.inp_source.insert(END,selDir)
    else:
        selDir = str(tkinter.filedialog.askdirectory())
        self.inp_destination.insert(END,selDir)



if __name__ == '__main__':
    pass
