import sqlite3

conn = sqlite3.Connection(':memory:')
with conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_People ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_name TEXT, \
            col_species TEXT, \
            col_IQ INT \
            )")
    firstPerson = ("Jean-Baptiste Zorg", "Human", 122)
    secondPerson = ("Korben Dallas", "Meat Popsicle", 100)
    thirdPerson = ("Ak'not", "Mangalore", -5)
    #each of these inserts a different set of data into the table
    cursor.execute("""INSERT INTO tbl_People(col_name,col_species,col_IQ) VALUES (?,?,?)""", ("Jean-Baptiste Zorg", "Human", 122))
    cursor.execute("""INSERT INTO tbl_People(col_name,col_species,col_IQ) VALUES (?,?,?)""", ("Korben Dallas", "Meat Popsicle", 100))
    cursor.execute("""INSERT INTO tbl_People(col_name,col_species,col_IQ) VALUES (?,?,?)""", ("Ak'not", "Mangalore", -5))
    check = cursor.execute("SELECT col_name,col_IQ FROM tbl_People WHERE col_species = 'Human'")
    data = cursor.fetchall()
    #first loop cycles through the list
    i = 0
    while i < len(data):
        c = 0
        #second loop prints each member of the tuple
        while c < len(data[i]):
            print(data[i][c])
            c = c+1
        i = i+1
        
    print("============")  #Viaually Separate outputs

    #update Korben Dallas to be a Human instead of meat poppopsicle
    cursor.execute("UPDATE tbl_People SET col_species='Human' WHERE col_name='Korben Dallas'")

    #Selects data from the table, Gets a list of tuples from that data with fetchall()
    check = cursor.execute("SELECT col_name,col_IQ FROM tbl_People WHERE col_species = 'Human'")
    data = cursor.fetchall()

    #first loop cycles through the list
    i = 0
    while i < len(data):
        c = 0
        #second loop prints each member of the tuple
        while c < len(data[i]):
            print(data[i][c])
            c = c+1
        i = i+1
          
    conn.commit()

    

    
conn.close()


