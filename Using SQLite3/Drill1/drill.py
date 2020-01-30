import sqlite3

fileList = ['information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']
conn = sqlite3.connect('drillDB.db')

# Get the text files with extension .txt
textFileNames = []
for i in fileList:
    fileName = i.split('.')[0]
    fileType = i.split('.')[1]
    if fileType == "txt":
        textFileNames.append(fileName)

with conn:
    cur = conn.cursor()
    # Apparently you can't put NOT NULL in the statement
    # Create the Table for the text file names
    cur.execute("\
        CREATE TABLE IF NOT EXISTS TextFiles (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        name VARCHAR\
        )")
    conn.commit()

    # Determine how many text files there are and add them to the table
    statement = "\
        INSERT INTO TextFiles\
        (name)\
        VALUES"
    
    if len(textFileNames) > 0:
        for i in textFileNames:
            if i == textFileNames[0]:
                statement += " (\'" + i + "\')"
            else:
                statement += ", (\'" + i + "\')"

    cur.execute(statement)
    conn.commit()

    #Printing the files to the console
    for i in textFileNames:
        print(i)
    
conn.close()
