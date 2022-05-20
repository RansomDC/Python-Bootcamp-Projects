import sqlite3

#get personal data from user
##firstName = input("Enter your first name: ")
##lastName = input("Enter your last name: ")
##age = int(input("Enter your age: "))
##personData = (firstName, lastName, age)

#execute insert statement for supplied person data
##with sqlite3.connect('test_database.db') as connection:
##    cursor = connection.cursor()
##    cursor.execute("INSERT INTO People VALUES(?,?,?)",personData)
##    cursor.execute("UPDATE People SET col_age=? WHERE col_fname=? AND col_lname=?", (33, 'Ransom', 'Cadorette'))

with sqlite3.connect('test_database.db') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT col_fname, col_lname FROM People WHERE col_age > 30")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        print(row)
