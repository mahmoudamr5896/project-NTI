import pyodbc

def connect_to_db():
    connection = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-DBCQQQ4;'  
        'DATABASE=InstituteDB;'     
        'Trusted_Connection=yes;'
    )
    return connection
