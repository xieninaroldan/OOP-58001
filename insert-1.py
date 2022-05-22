import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Daniel\Downloads\Database1.accdb;')
    print("Connected to a Database")

    Inventor = "Group 4"
    Invention = "Connecting MS Access Database"
    DateofInvention = 2022
    Description = "Create a python program that connects Pycharm to MS Access Database."
    user_id = 11

    record = connect.cursor()
    record.execute('UPDATE tblInventor SET Inventor = ? WHERE id = ?', (Inventor, user_id))
    record.execute('UPDATE tblInventor SET Invention = ? WHERE id = ?', (Invention, user_id))
    record.execute('UPDATE tblInventor SET DateofInvention = ? WHERE id = ?', (DateofInvention, user_id))
    record.execute('UPDATE tblInventor SET Description = ? WHERE id = ?', (Description, user_id))
    record.commit()
    print("Data is inserted")

except pyodbc.Error as e:
    print("Error in Connection")