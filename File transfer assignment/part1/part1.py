import shutil
import os
import datetime as dt



#Transfering files
#set where the source of the files is
source = '/Users/Ranso/OneDrive/Desktop/Folder-A/'

#set the destination path to folder-B
destination = '/Users/Ranso/OneDrive/Desktop/Folder-B/'

files = os.listdir(source)

for i in files:
    #this is the command to move each file (represented with i) to the new destination
    shutil.move(source+i, destination)
