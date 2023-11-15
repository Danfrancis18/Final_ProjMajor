import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="canteenmanagement"
)

mycursor = mydb.cursor()
    

class Employee:

    def __init__(self,EmpID,EmpLName,EmpFName,Birthday,Address,DateofEmplymnt,JobID):
        self.EmpID = EmpID
        self.EmpLName = EmpLName
        self.EmpFName = EmpFName
        self.Birthday = Birthday
        self.Address = Address
        self.DateofEmplymnt = DateofEmplymnt
        self.JobID = JobID

    def create(self):
        print(self.EmpID)
        print(self.EmpFName)
        print(self.EmpLName)
        print(self.Birthday)
        print(self.JobID)
        print(self.DateofEmplymnt)
        print(self.Address)
        mycursor.execute("INSERT INTO employeetbl (EmpID, EmpLName, EmpFName, Birthday, Address, DateofEmplymnt, JobID) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                 (self.EmpID, self.EmpLName, self.EmpFName, self.Birthday, self.Address, self.DateofEmplymnt, self.JobID))
        mydb.commit()


        messagebox.showinfo("Success", "Employee Added Successfully")