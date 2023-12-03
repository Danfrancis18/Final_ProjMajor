from tkinter import Text, ttk
import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image
import os
from tkcalendar import DateEntry
import mysql.connector
from objects import Employee
from objects import Login

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="canteenmanagement"
)

mycursor = mydb.cursor()


customtkinter.set_appearance_mode("light")

DIRPATH = os.path.dirname(os.path.abspath(__file__))

themepath = os.path.join(DIRPATH, "red.json")

if os.path.exists(themepath):       
    customtkinter.set_default_color_theme(themepath)
else:
    customtkinter.set_default_color_theme("blue")
    


class CIMOS_EmpPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Employee Management")
        self.geometry(f"1000x580+350+130")
        self.bind("<1>", lambda event: event.widget.focus_set())
        self.resizable(False, False)
        
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        
        def home():
            self.destroy()
            os.system('python adminpage.py')
        
        def menupage():
            self.destroy()
            os.system('python menu.py')

        def salespage():
            print('wala pa hehe')
        
        def toggle_menu():
            def collapse_menu():
                self.my_frame.destroy()
                self.menuimg = customtkinter.CTkImage(light_image=Image.open(os.path.join("menu1.png")), dark_image=Image.open(os.path.join("menu.png")),size=(40,40))
                self.Image_label = customtkinter.CTkButton(self, text="", image=self.menuimg, fg_color="transparent", width=40, height=40, command=toggle_menu)
                self.Image_label.grid(row=0, column=0, padx=(0, 920), pady=(0,500))
                
            self.my_frame = customtkinter.CTkFrame(self, width=220, height=40, corner_radius=10, fg_color="white", bg_color="transparent")
            self.my_frame.grid(row=0, column=0, padx=(0, 820), pady=(70,330), sticky="ns")
            self.menuimg = customtkinter.CTkImage(light_image=Image.open(os.path.join("menu1.png")), dark_image=Image.open(os.path.join("menu.png")),size=(40,40))
            self.Image_label = customtkinter.CTkButton(self, text="", image=self.menuimg, fg_color="transparent", width=40, height=40, command=collapse_menu)
            self.Image_label.grid(row=0, column=0, padx=(0, 920), pady=(0,500))
        #----Menu----------------------------------------------------------------------------------------------------------------------------------------------------
            #----Employee Tab----------------------------------------------------------------------------------------------------------------------------------------------------------
            def togmenu1():
                self.empbutton = customtkinter.CTkButton(self.my_frame, text="Employee", fg_color="#FFC3B4", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), corner_radius=0, command=togmenu1)
                self.empbutton.grid(row=0, column=0, padx=(0,0), pady=(10,290))
                self.prodbutton = customtkinter.CTkButton(self.my_frame, text="Menu", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=menupage)
                self.prodbutton.grid(row=0, column=0, padx=(2,2), pady=(10,220))
                self.salesbutton = customtkinter.CTkButton(self.my_frame, text="Sales", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=salespage)
                self.salesbutton.grid(row=0, column=0, padx=(2,2), pady=(10,150))
                self.homebutton = customtkinter.CTkButton(self.my_frame, text="Home", fg_color="#9f1111", bg_color="transparent", text_color="white", font=customtkinter.CTkFont(size=14, weight="bold"), command=home)
                self.homebutton.grid(row=0, column=0, padx=(2,2), pady=(0,10))
            
            self.empbutton = customtkinter.CTkButton(self.my_frame, text="Employee", fg_color="#FFC3B4", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), corner_radius=0, command=togmenu1)
            self.empbutton.grid(row=0, column=0, padx=(0,0), pady=(10,290))
            #-----Menu Tab--------------------------------------------------------------------------------------------------------------------------------------------------
            

            self.prodbutton = customtkinter.CTkButton(self.my_frame, text="Menu", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=menupage)
            self.prodbutton.grid(row=0, column=0, padx=(2,2), pady=(10,220))
            #------Sales Tab--------------------------------------------------------------------------------------------------------------------------------------------------

                
            self.salesbutton = customtkinter.CTkButton(self.my_frame, text="Sales", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=salespage)
            self.salesbutton.grid(row=0, column=0, padx=(2,2), pady=(10,150))
            
            self.homebutton = customtkinter.CTkButton(self.my_frame, text="Home", fg_color="#9f1111", bg_color="transparent", text_color="white", font=customtkinter.CTkFont(size=14, weight="bold"), command=home)
            self.homebutton.grid(row=0, column=0, padx=(2,2), pady=(0,10))
            
            #-----Home Button-----------------------------------------------------------------
        
        #-------Current Page---------------------------------------------------------------------------------------------------------------------------------
        self.menuimg = customtkinter.CTkImage(light_image=Image.open(os.path.join("menu1.png")), dark_image=Image.open(os.path.join("menu.png")),size=(40,40))
        self.Image_label = customtkinter.CTkButton(self, text="", image=self.menuimg, fg_color="transparent", width=40, height=40, command=toggle_menu)
        self.Image_label.grid(row=0, column=0, padx=(0, 920), pady=(0,500))
        self.logo_label = customtkinter.CTkLabel(self, text="Admin Controls - Employee", font=customtkinter.CTkFont("Harrington", size=26, weight="bold"), fg_color="transparent", text_color="White")
        self.logo_label.grid(row=0, column=0, padx=(0, 530), pady=(0,500))
        
        #-----------Tab-----------------------------------------------------------------------------------
        
        self.tabview = customtkinter.CTkFrame(self, width=250)
        self.tabview.grid(row=0, column=0, padx=(20, 20), pady=(100, 60), sticky="nsew")
        
        #-------------View------------------------------------------------------------------
            #-----------View Tab--------------
            #----dito ishoshow yung data, current employee, employee info-------------
        self.viewframe = customtkinter.CTkFrame(self.tabview, width=900, height=320, fg_color="white", corner_radius=6)
        self.viewframe.grid(row=0, column=0, padx=(30,10), pady=(65,0), sticky="nsew")
        
        style = ttk.Style(self.viewframe)
        style.theme_use('clam')
        style.configure('Treeview', font=('Arial', 12, 'bold'), foreground='#fff', background='#777777', fieldbackground='#222222', rowheight=38)
        style.map('Treeview', background=[('selected', '#9F0000')])

        tree = ttk.Treeview(self.viewframe, height=10)

        tree['columns'] = ('EmpID', 'Last Name', 'First Name', 'Birthday', 'Address', 'Position', 'Type of Employment', 'Date of Employment')

        tree.column('#0', width=0, stretch=tk.NO)
        tree.column('EmpID', anchor=tk.CENTER, width=80)
        tree.column('Last Name', anchor=tk.CENTER, width=140)
        tree.column('First Name', anchor=tk.CENTER, width=140)
        tree.column('Birthday', anchor=tk.CENTER, width=140)
        tree.column('Address', anchor=tk.CENTER, width=210)
        tree.column('Position', anchor=tk.CENTER, width=140)
        tree.column('Type of Employment', anchor=tk.CENTER, width=130)
        tree.column('Date of Employment', anchor=tk.CENTER, width=140)

        tree.heading('EmpID', text='EmpID')
        tree.heading('Last Name', text='Surname')
        tree.heading('First Name', text='First Name')
        tree.heading('Birthday', text='Birthday')
        tree.heading('Address', text='Address')
        tree.heading('Position', text='Job Description')
        tree.heading('Type of Employment', text='Type of Employment')
        tree.heading('Date of Employment', text='Date Hired')
        
        vsb = tk.Scrollbar(self.tabview, orient="vertical", command=tree.yview, width=16)
        vsb.place(x=1160, y=106, height=374)

        tree.configure(yscrollcommand=vsb.set)

        tree.place(x=0, y=0)

        def add_to_treeview():
            employees = Employee.fetch_employee()
            
            tree.delete(*tree.get_children())
            for employee in employees:
                tree.insert('', 'end', values=employee)

        def display_data(event):
            self.updtbutton.configure(state='normal')
            self.delbutton.configure(state='normal')
            item = tree.focus()
            if item:
                values = tree.item(item, 'values')
                global updEmpID
                updEmpID = values[0]
                global updEmpLName
                updEmpLName = values[1]
                global updEmpFName
                updEmpFName = values[2]
                global updBirthday
                updBirthday = values[3]
                global updAddress
                updAddress = values[4]
                global updJobDescription
                updJobDescription = values[5]
                global updTypeOfEmplymnt
                if values[6] == "Full-Time":
                    updTypeOfEmplymnt = 1
                else:
                    updTypeOfEmplymnt = 0
                global updDateOfEmplymnt
                updDateOfEmplymnt = values[7]

            else:
                pass

        

        


        
        
        def addfunc():
            self.updtbutton.configure(state='disabled')
            self.delbutton.configure(state='disabled')
            def collapse_menu1():
                self.viewframe1.destroy()
                self.addbutton = customtkinter.CTkButton(self.tabview, text="Add", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command = addfunc)
                self.addbutton.grid(row=0, column=0, padx=(780,0), pady=(0,320))
            
            self.viewframe1 = customtkinter.CTkFrame(self.tabview, width=900, height=320, fg_color="#9F0000", corner_radius=6)
            self.viewframe1.grid(row=0, column=0, padx=(30,10), pady=(65,0), sticky="nsew")
            self.addbutton2 = customtkinter.CTkButton(self.tabview, text="Close", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command = collapse_menu1)
            self.addbutton2.grid(row=0, column=0, padx=(780,0), pady=(0,320))
            self.ln = customtkinter.CTkLabel(self.viewframe1, text="Last Name: ")
            self.ln.grid(row=0, column=0, padx=(60,620), pady=(30,5), sticky="nw")#
            self.fn = customtkinter.CTkLabel(self.viewframe1, text="First Name: ")
            self.fn.grid(row=0, column=0, padx=(60,620), pady=(70,5), sticky="nw")
            self.ep = customtkinter.CTkLabel(self.viewframe1, text="Address: ")
            self.ep.grid(row=0, column=0, padx=(60,675), pady=(115,5), sticky="nw")
            self.bday = customtkinter.CTkLabel(self.viewframe1, text="Birthday: ")
            self.bday.grid(row=0, column=0, padx=(60,680), pady=(150,5), sticky="nw")
            self.jd = customtkinter.CTkLabel(self.viewframe1, text="Job Description: ")
            self.jd.grid(row=0, column=0, padx=(60,680), pady=(190,5), sticky="nw")
            self.dh = customtkinter.CTkLabel(self.viewframe1, text="Date Hired: ")
            self.dh.grid(row=0, column=0, padx=(60,680), pady=(230,5), sticky="nw")
        
            self.lnentry = customtkinter.CTkEntry(self.viewframe1, placeholder_text="Enter last name...")
            self.lnentry.grid(row=0, column=0, padx=(140,20), pady=(30,265), sticky="nsew")
            self.fnentry = customtkinter.CTkEntry(self.viewframe1, placeholder_text="Enter first name...")
            self.fnentry.grid(row=0, column=0, padx=(140,20), pady=(70,225), sticky="nsew")
            self.addentry = customtkinter.CTkEntry(self.viewframe1, placeholder_text="Enter Address...")
            self.addentry.grid(row=0, column=0, padx=(140,20), pady=(110,185), sticky="nsew")
        
            
            self.bdaycal = DateEntry(self.viewframe1, width=12, background='#222222',foreground='white', locale='en_US', date_pattern='yyyy/MM/dd')
            self.bdaycal.grid(row=0, column=0, padx=(180,20), pady=(190,190), sticky="nsw")
            self.bdaycal.bind("<<DateEntrySelected>>")
        

            self.jdchoose = customtkinter.CTkOptionMenu(self.viewframe1, dynamic_resizing=False, values=["Cashier", "Delivery", "Dishwasher", "Cleaner", "Cook"], button_color="white", button_hover_color="#222222")
            self.jdchoose.grid(row=0, column=0, padx=(170,20), pady=(190, 110), sticky="nsew")
            self.jdchoose.set("-Choose-")

            self.hiredcal = DateEntry(self.viewframe1, width=12, background='#222222',foreground='white', locale='en_US', date_pattern='yyyy/MM/dd')
            self.hiredcal.grid(row=0, column=0, padx=(180,20), pady=(290,90), sticky="nsw")
            self.hiredcal.bind("<<DateEntrySelected>>")

            mycursor.execute("SELECT EmpID FROM employeetbl ORDER BY EmpID DESC LIMIT 1")
            numEmployee = mycursor.fetchone()
            self.nextEmpID = numEmployee[0] + 1

            
            def submit():
            
                
                dumpEmpID = self.nextEmpID
                dumpEmpLName = self.lnentry.get()
                dumpEmpFName = self.fnentry.get()
                dumpBirthday = self.bdaycal.get()
                dumpAddress = self.addentry.get()
                dumpDateofEmplymnt = self.hiredcal.get()
                dumpJobDescription = self.jdchoose.get()
                if self.jdchoose.get() == "Cashier":
                    dumpJobID = 4
                elif self.jdchoose.get() == "Delivery":
                    dumpJobID = 6
                elif self.jdchoose.get() == "Dishwasher":
                    dumpJobID = 8
                elif self.jdchoose.get() == "Cleaner":
                    dumpJobID = 10
                elif self.jdchoose.get() == "Cook":
                    dumpJobID = 12
                elif self.jdchoose.get() == "-Choose-":
                    tkinter.messagebox.showerror("Error", "Please choose a job description")
                    return

                if dumpEmpLName == "" or dumpEmpFName == "" or dumpBirthday == "" or dumpAddress == "" or dumpDateofEmplymnt == "" or dumpJobID == "-Choose-":
                    tkinter.messagebox.showerror("Error", "Please fill up all fields")
                    return
                else:
                    new_employee = Employee(dumpEmpID, dumpEmpLName, dumpEmpFName, dumpBirthday, dumpAddress, dumpDateofEmplymnt, dumpJobID)

                new_employee.create()

                add_to_treeview()


            self.add2button=customtkinter.CTkButton(self.viewframe1, text="Add Employee", bg_color="transparent", fg_color="#222222", text_color="white", font=customtkinter.CTkFont(size=14, weight="bold"), width=290, command=submit)
            self.add2button.grid(row=0, column=0, padx=(240,200), pady=(280,20), sticky="ew")
        


            #employee code, last name, first name, employee type, date hired, job description
        
        #-----------Edit Tab-------------------------------------------------------------------
         
        
        self.addbutton = customtkinter.CTkButton(self.tabview, text="Add", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command = addfunc)
        self.addbutton.grid(row=0, column=0, padx=(780,0), pady=(0,320))
        
        #-----Update-------------------
        def updtfunc():

            self.addbutton.configure(state='disabled')




            def collapse_menu2():
                self.addbutton.configure(state='normal')
                self.viewframe2.destroy()
                self.updtbutton = customtkinter.CTkButton(self.tabview, text="Update", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=updtfunc)
                self.updtbutton.grid(row=0, column=0, padx=(460,0), pady=(0,320))
            
            self.viewframe2 = customtkinter.CTkFrame(self.tabview, width=900, height=320, fg_color="#9F0000", corner_radius=6)
            self.viewframe2.grid(row=0, column=0, padx=(30,10), pady=(65,0), sticky="nsew")
            self.updtbutton2 = customtkinter.CTkButton(self.tabview, text="Close", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command = collapse_menu2)
            self.updtbutton2.grid(row=0, column=0, padx=(460,0), pady=(0,320))
            self.ln = customtkinter.CTkLabel(self.viewframe2, text="Last Name: ")
            self.ln.grid(row=0, column=0, padx=(30,650), pady=(30,5), sticky="nw")
            self.fn = customtkinter.CTkLabel(self.viewframe2, text="First Name: ")
            self.fn.grid(row=0, column=0, padx=(30,650), pady=(70,5), sticky="nw")
            self.ep = customtkinter.CTkLabel(self.viewframe2, text="Address: ")
            self.ep.grid(row=0, column=0, padx=(30,705), pady=(115,5), sticky="nw")
            self.bday = customtkinter.CTkLabel(self.viewframe2, text="Birthday: ")
            self.bday.grid(row=0, column=0, padx=(30,105), pady=(115,5), sticky="ne")
            self.jd = customtkinter.CTkLabel(self.viewframe2, text="Job Description: ")
            self.jd.grid(row=0, column=0, padx=(30,710), pady=(180,5), sticky="nw")
            self.dh = customtkinter.CTkLabel(self.viewframe2, text="Date Hired: ")
            self.dh.grid(row=0, column=0, padx=(30,93), pady=(175,5), sticky="ne")
            self.temp = customtkinter.CTkLabel(self.viewframe2, text="Type of Employment: ")
            self.temp.grid(row=0, column=0, padx=(30,38), pady=(20,5), sticky="ne")
            
            self.ep_frame = customtkinter.CTkFrame(self.viewframe2)
            self.ep_frame.grid(row=0, column=0, padx=(30, 40), pady=(40,5), sticky="ne")
            self.radio_var = tkinter.IntVar(value=0)
            self.radio_button_1 = customtkinter.CTkRadioButton(self.ep_frame, variable=self.radio_var, value=0, text="Part Time", border_color="#e86161")
            self.radio_button_1.grid(row=1, column=2, padx=(20,20), pady=(10,0), sticky="nw")
            self.radio_button_2 = customtkinter.CTkRadioButton(self.ep_frame, variable=self.radio_var, value=1, text="Full Time", border_color="#e86161")
            self.radio_button_2.grid(row=2, column=2, padx=(20,20), pady=(10,10), sticky="nw")
        
            self.lnentry = customtkinter.CTkEntry(self.viewframe2)
            
            self.lnentry.grid(row=0, column=0, padx=(110,350), pady=(30,265), sticky="nsew")
            self.fnentry = customtkinter.CTkEntry(self.viewframe2)

            self.fnentry.grid(row=0, column=0, padx=(110,350), pady=(70,225), sticky="nsew")
            self.addentry = customtkinter.CTkEntry(self.viewframe2)

            self.addentry.grid(row=0, column=0, padx=(110,350), pady=(110,185), sticky="nsew")
            
            self.bdaycal = DateEntry(self.viewframe2, width=12, background='#222222',foreground='white', locale='en_US', date_pattern='yyyy/MM/dd')
            self.bdaycal.grid(row=0, column=0, padx=(0,100), pady=(180,190), sticky="ne")


            self.jdchoose = customtkinter.CTkOptionMenu(self.viewframe2, dynamic_resizing=False, values=["Manager","Cashier", "Delivery", "Dishwasher", "Cleaner", "Cook"], button_color="white", button_hover_color="#222222")
            self.jdchoose.grid(row=0, column=0, padx=(140,350), pady=(180, 120), sticky="nsew")


            self.hiredcal = DateEntry(self.viewframe2, width=12, background='#222222',foreground='white', locale='en_US', date_pattern='yyyy/MM/dd')
            self.hiredcal.grid(row=0, column=0, padx=(0,100), pady=(250,0), sticky="ne")

            self.lnentry.insert(0, updEmpLName)
            self.fnentry.insert(0, updEmpFName)
            self.addentry.insert(0, updAddress)
            self.bdaycal.set_date(updBirthday)
            self.hiredcal.set_date(updDateOfEmplymnt)
            self.jdchoose.set(updJobDescription)
            

            def update():
                dumpEmpLName = self.lnentry.get()
                dumpEmpFName = self.fnentry.get()
                dumpBirthday = self.bdaycal.get()
                dumpAddress = self.addentry.get()
                dumpDateofEmplymnt = self.hiredcal.get()
                dumpJobDescription = self.jdchoose.get()
                dumpTypeOfEmplymnt = self.radio_var.get()

                mycursor.execute("SELECT LoginID FROM logintbl ORDER BY LoginID DESC LIMIT 1")
                numLogin = mycursor.fetchone()
                self.nextLoginID = numLogin[0] + 1
                dumpLoginID = self.nextLoginID
                
                
                if dumpJobDescription == "Manager" and dumpTypeOfEmplymnt == 1:
                    dumpJobID = 2
                if dumpJobDescription == "Manager" and dumpTypeOfEmplymnt == 0:
                    dumpJobID = 2
                elif dumpJobDescription == "Cashier" and dumpTypeOfEmplymnt == 1:
                    dumpJobID = 3
                elif dumpJobDescription == "Cashier" and dumpTypeOfEmplymnt == 0:
                    dumpJobID = 4
                elif self.jdchoose.get() == "Delivery" and dumpTypeOfEmplymnt == 1:
                    dumpJobID = 5
                elif self.jdchoose.get() == "Delivery" and dumpTypeOfEmplymnt == 0:
                    dumpJobID = 6
                elif self.jdchoose.get() == "Dishwasher" and dumpTypeOfEmplymnt == 1:
                    dumpJobID = 7
                elif self.jdchoose.get() == "Dishwasher" and dumpTypeOfEmplymnt == 0:
                    dumpJobID = 8
                elif self.jdchoose.get() == "Cleaner" and dumpTypeOfEmplymnt == 1:
                    dumpJobID = 9
                elif self.jdchoose.get() == "Cleaner" and dumpTypeOfEmplymnt == 0:
                    dumpJobID = 10
                elif self.jdchoose.get() == "Cook" and dumpTypeOfEmplymnt == 1:
                    dumpJobID = 11
                elif self.jdchoose.get() == "Cook" and dumpTypeOfEmplymnt == 0:
                    dumpJobID = 12

                if dumpEmpLName == "" or dumpEmpFName == "" or dumpBirthday == "" or dumpAddress == "" or dumpDateofEmplymnt == "" or dumpJobID == "-Choose-":
                    tkinter.messagebox.showerror("Error", "Please fill up all fields")
                    return
                else:
                    new_employee = Employee(updEmpID, dumpEmpLName, dumpEmpFName, dumpBirthday, dumpAddress, dumpDateofEmplymnt, dumpJobID)
                
                def check_if_manager_exists(empID):
                    mycursor.execute("SELECT * FROM logintbl WHERE EmpID = %s", [empID])
                    result = mycursor.fetchone()
                    if result:
                        return True
                    else:
                        return False
                if dumpJobID == 2:
                    if check_if_manager_exists(updEmpID):
                        tkinter.messagebox.showerror("Error", "Manager already exists")
                        return
                        
                    else:
                        
                        new_login = Login(dumpLoginID, "Admin", updEmpID, dumpEmpLName+updEmpID, "password")
                        new_login.create_admin()

                
                else:
                    pass
                
                 
                new_employee.update_employee()



                add_to_treeview()

            

            self.updt2button=customtkinter.CTkButton(self.viewframe2, text="Update Employee", bg_color="transparent", fg_color="#222222", text_color="white", font=customtkinter.CTkFont(size=14, weight="bold"), width=290, command=update)
            self.updt2button.grid(row=0, column=0, padx=(240,200), pady=(280,20), sticky="ew")

            
        #-----Delete-------------------
        def delete_emp():
            delete_employee = Employee(updEmpID, updEmpLName, updEmpFName, updBirthday, updAddress, updDateOfEmplymnt, updJobDescription)
            delete_employee.delete_employee()
            add_to_treeview()    
        
        self.updtbutton = customtkinter.CTkButton(self.tabview, text="Update", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), state="disabled", command=updtfunc)
        self.updtbutton.grid(row=0, column=0, padx=(460,0), pady=(0,320))
        
        self.delbutton = customtkinter.CTkButton(self.tabview, text="Delete", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), state="disabled", command=delete_emp)
        self.delbutton.grid(row=0, column=0, padx=(140,0), pady=(0,320))
        


        
        
        tree.bind('<<TreeviewSelect>>', display_data)
        add_to_treeview()
            
        
        #self.toggle_button = customtkinter.CTkButton

app = CIMOS_EmpPage()
app.mainloop()