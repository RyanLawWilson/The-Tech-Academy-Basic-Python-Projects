import sqlite3

# Represents your connection to the database
conn = sqlite3.connect('test.db')

# While our connection is active...
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_fname TEXT,\
        col_lname TEXT,\
        col_email TEXT\
    )")
    conn.commit()
    
# This needs to be outside of the with statement for some reason
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons \
        (col_fname, col_lname, col_email)\
        VALUES\
        (?, ?, ?)",\
        ('Sarah', 'Jones', 'asdfa@gmail.com'))
    cur.execute("INSERT INTO tbl_persons \
        (col_fname, col_lname, col_email)\
        VALUES\
        (?, ?, ?)",\
        ('asads', 'ggg', '1234@gmail.com'))
    cur.execute("INSERT INTO tbl_persons \
        (col_fname, col_lname, col_email)\
        VALUES\
        (?, ?, ?)",\
        ('hello', 'pizza', 'kakakak@gmail.com'))
    conn.commit()
conn.close()




conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lname, col_email\
        FROM tbl_persons\
        WHERE col_fname = 'Sarah'")
    varPerson = cur.fetchall()

    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0], item[1], item[2])
    print(msg)

conn.close()
    









