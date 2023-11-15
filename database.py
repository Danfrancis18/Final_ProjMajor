import mysql.connector

def fetch_menu():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="canteenmanagement"
    )
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM menutbl')
    Menu = mycursor.fetchall()
    mydb.close()
    return Menu

def fetch_ID():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="canteenmanagement"
    )
    mycursor = mydb.cursor()
    mycursor.execute('SELECT ProductID FROM menutbl')
    Menu = mycursor.fetchall()
    mydb.close()
    return Menu

def insert_menu(ProductName,Price):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="canteenmanagement"
    )
    mycursor = mydb.cursor()
    mycursor.execute('INSERT INTO menutbl (ProductName, Price) VALUES ( %s, %s )', (ProductName, Price))
    mydb.commit()
    mydb.close()
    
def delete_menu(ProductID):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="canteenmanagement"
    )
    mycursor = mydb.cursor()
    values = (ProductID,)

    sql = 'DELETE FROM menutbl WHERE ProductID = %s'
    mycursor.execute(sql, values)

    mydb.commit()
    mydb.close()
    
def update_menu(newname, newprice, ProductID):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="canteenmanagement"
    )
    mycursor = mydb.cursor()

    # Use placeholders for the values in the WHERE clause
    sql = 'UPDATE menutbl SET ProductName = %s, Price = %s WHERE ProductID = %s'
    
    # Pass a tuple with the values to be substituted into the placeholders
    values = (newname, newprice, ProductID)

    mycursor.execute(sql, values)
    
    mydb.commit()
    mydb.close()