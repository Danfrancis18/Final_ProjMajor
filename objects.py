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
        mycursor.execute("INSERT INTO employeetbl (EmpID, EmpLName, EmpFName, Birthday, Address, DateofEmplymnt, JobID) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                 (self.EmpID, self.EmpLName, self.EmpFName, self.Birthday, self.Address, self.DateofEmplymnt, self.JobID))
        mydb.commit()


        messagebox.showinfo("Success", "Employee Added Successfully")

    def fetch_employee():
        mycursor.execute('SELECT EmpID,EmpLName,EmpFName,Birthday,Address,JobDescription,TypeOfEmplymnt,DateOfEmplymnt FROM employeetree')
        Employee = mycursor.fetchall()
        mydb.commit()
        return Employee

    def fetch_ID():
        mycursor.execute('SELECT EmpID FROM employeetbl')
        Employee = mycursor.fetchall()
        mydb.commit()
        return Employee

    def update_employee(self):
        mycursor.execute("UPDATE employeetbl SET EmpLName = %s, EmpFName = %s, Birthday = %s, Address = %s, DateofEmplymnt = %s, JobID = %s WHERE EmpID = %s",
                 (self.EmpLName, self.EmpFName, self.Birthday, self.Address, self.DateofEmplymnt, self.JobID, self.EmpID))
        mydb.commit()
        messagebox.showinfo("Success", "Employee Updated Successfully")

    def delete_employee(self):
        response = messagebox.askyesno("Delete", "Are you sure you want to delete this employee?")
        if response == 1:
            mycursor.execute("DELETE FROM employeetbl WHERE EmpID = %s", (self.EmpID,))
            mydb.commit()
            messagebox.showinfo("Success", "Employee Deleted Successfully")
        else:
            pass




    


