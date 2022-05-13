import sqlite3

def createTableFromTuple():
    #The tuple that the following actions pull from
    fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

    #creates a table with a primary key column, and a column for the names of the files
    conn = sqlite3.connect('assignment.db')     #connects to the database
    with conn:
        cur = conn.cursor()     #creates a variable for the cursor
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileNames TEXT \
            )")
        conn.commit()
    conn.close()


    conn = sqlite3.connect('assignment.db')
    with conn:
        cur = conn.cursor()
        for element in fileList:        #For each item in the tuple fileList 
            if element.endswith('.txt'):        #determine if it ends with '.txt'
                cur.execute("INSERT INTO tbl_files(col_fileNames) VALUES(?)", (element,))   #if it does, insert it into the table
            conn.commit()       #commit the changes
    conn.close()        #close the database

    #select all files that are now in the database under the fileNames column inserts them into a tuple, and print them one at a time.
    conn = sqlite3.connect('assignment.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_fileNames FROM tbl_files")
        varfiles = cur.fetchall()
        for item in varfiles:
            print(str(item))
    conn.close()


if __name__ == '__main__':
    createTableFromTuple()
