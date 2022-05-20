import shutil
import os
import datetime as dt


def transfer():
    today = dt.datetime.now().date()
    
    #Obtain the list of files that are in the starting folder
    source = os.listdir('/Users/Ranso/OneDrive/Desktop/Folder-A')
    for file in source:
        filepath = ('/Users/Ranso/OneDrive/Desktop/Folder-A/' + file)
        
        #fromtimestamp translates the getmtime which is the time since a file was edited
        #to a date useable by datetime.
        #(getmtime is represented by a floating point in seconds since a specific epoch)
        filetime = dt.datetime.fromtimestamp(os.path.getmtime(filepath))
        
        #convert filetime to the same format as the 'today' variable
        filetime_con = filetime.date()
        
        if filetime_con == today:
            #set the destination path to folder-B
            destination = '/Users/Ranso/OneDrive/Desktop/Folder-B/'

            #Move the current file
            shutil.move(filepath, destination)




if __name__ == '__main__':
    transfer()
