from tkinter import Text, ttk
import tkinter.messagebox
import customtkinter
from PIL import Image
import os
from tkcalendar import DateEntry
import mysql.connector

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
            import mainapp
        
        
        
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
                self.prodbutton = customtkinter.CTkButton(self.my_frame, text="Menu", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu2)
                self.prodbutton.grid(row=0, column=0, padx=(2,2), pady=(10,220))
                self.salesbutton = customtkinter.CTkButton(self.my_frame, text="Sales", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu3)
                self.salesbutton.grid(row=0, column=0, padx=(2,2), pady=(10,150))
                self.homebutton = customtkinter.CTkButton(self.my_frame, text="Home", fg_color="#9f1111", bg_color="transparent", text_color="white", font=customtkinter.CTkFont(size=14, weight="bold"), command=home)
                self.homebutton.grid(row=0, column=0, padx=(2,2), pady=(0,10))
            
            self.empbutton = customtkinter.CTkButton(self.my_frame, text="Employee", fg_color="#FFC3B4", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), corner_radius=0, command=togmenu1)
            self.empbutton.grid(row=0, column=0, padx=(0,0), pady=(10,290))
            #-----Menu Tab--------------------------------------------------------------------------------------------------------------------------------------------------
            def togmenu2():
                self.empbutton = customtkinter.CTkButton(self.my_frame, text="Employee", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu1)
                self.empbutton.grid(row=0, column=0, padx=(0,0), pady=(10,290))
                self.prodbutton = customtkinter.CTkButton(self.my_frame, text="Menu", fg_color="#FFC3B4", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), corner_radius=0, command=togmenu2)
                self.prodbutton.grid(row=0, column=0, padx=(2,2), pady=(10,220))
                self.salesbutton = customtkinter.CTkButton(self.my_frame, text="Sales", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu3)
                self.salesbutton.grid(row=0, column=0, padx=(2,2), pady=(10,150))
                self.homebutton = customtkinter.CTkButton(self.my_frame, text="Home", fg_color="#9f1111", bg_color="transparent", text_color="white", font=customtkinter.CTkFont(size=14, weight="bold"), command=home)
                self.homebutton.grid(row=0, column=0, padx=(2,2), pady=(0,10))

            self.prodbutton = customtkinter.CTkButton(self.my_frame, text="Menu", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu2)
            self.prodbutton.grid(row=0, column=0, padx=(2,2), pady=(10,220))
            #------Sales Tab--------------------------------------------------------------------------------------------------------------------------------------------------
            def togmenu3():
                self.empbutton = customtkinter.CTkButton(self.my_frame, text="Employee", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu1)
                self.empbutton.grid(row=0, column=0, padx=(0,0), pady=(10,290))
                self.prodbutton = customtkinter.CTkButton(self.my_frame, text="Menu", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu2)
                self.prodbutton.grid(row=0, column=0, padx=(2,2), pady=(10,220))
                self.salesbutton = customtkinter.CTkButton(self.my_frame, text="Sales", fg_color="#FFC3B4", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), corner_radius=0, command=togmenu3)
                self.salesbutton.grid(row=0, column=0, padx=(2,2), pady=(10,150))
                self.homebutton = customtkinter.CTkButton(self.my_frame, text="Home", fg_color="#9f1111", bg_color="transparent", text_color="white", font=customtkinter.CTkFont(size=14, weight="bold"), command=home)
                self.homebutton.grid(row=0, column=0, padx=(2,2), pady=(0,10))
                
            self.salesbutton = customtkinter.CTkButton(self.my_frame, text="Sales", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu3)
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
        
        def addfunc():
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
            self.ep = customtkinter.CTkLabel(self.viewframe1, text="Employee Type: ")
            self.ep.grid(row=0, column=0, padx=(60,675), pady=(110,5), sticky="nw")
            self.jd = customtkinter.CTkLabel(self.viewframe1, text="Job Description: ")
            self.jd.grid(row=0, column=0, padx=(60,680), pady=(190,5), sticky="nw")
            self.dh = customtkinter.CTkLabel(self.viewframe1, text="Date Hired: ")
            self.dh.grid(row=0, column=0, padx=(60,680), pady=(230,5), sticky="nw")
        
            self.lnentry = customtkinter.CTkEntry(self.viewframe1, placeholder_text="Enter last name...")
            self.lnentry.grid(row=0, column=0, padx=(140,20), pady=(30,265), sticky="nsew")
            self.fnentry = customtkinter.CTkEntry(self.viewframe1, placeholder_text="Enter first name...")
            self.fnentry.grid(row=0, column=0, padx=(140,20), pady=(70,225), sticky="nsew")
        
            self.ep_frame = customtkinter.CTkFrame(self.viewframe1)
            self.ep_frame.grid(row=0, column=0, padx=(170, 0), pady=(110,140), sticky="nsw")
            self.radio_var = tkinter.IntVar(value=0)
            self.radio_button_1 = customtkinter.CTkRadioButton(self.ep_frame, variable=self.radio_var, value=0, text="Full Time", border_color="#e86161")
            self.radio_button_1.grid(row=1, column=2, padx=(20,20), pady=(10,0), sticky="nw")
            self.radio_button_2 = customtkinter.CTkRadioButton(self.ep_frame, variable=self.radio_var, value=1, text="Part Time", border_color="#e86161")
            self.radio_button_2.grid(row=2, column=2, padx=(20,20), pady=(10,10), sticky="nw")
        
            self.jdchoose = customtkinter.CTkOptionMenu(self.viewframe1, dynamic_resizing=False, values=["Manager", "Cashier", "Delivery", "Dishwasher", "Cleaner", "Cook"], button_color="white", button_hover_color="#222222")
            self.jdchoose.grid(row=0, column=0, padx=(170,20), pady=(190, 110), sticky="nsew")
            self.jdchoose.set("-Choose-")
        
            self.cal = DateEntry(self.viewframe1, width=12, background='#222222',foreground='white', locale='en_US', date_pattern='yyyy/MM/dd')
            self.cal.grid(row=0, column=0, padx=(180,20), pady=(290,90), sticky="w")
            self.cal.bind("<<DateEntrySelected>>")
            
            self.add2button=customtkinter.CTkButton(self.viewframe1, text="Add Employee", bg_color="transparent", fg_color="#222222", text_color="white", font=customtkinter.CTkFont(size=14, weight="bold"), width=290)
            self.add2button.grid(row=0, column=0, padx=(240,200), pady=(280,20), sticky="ew")
        


            #employee code, last name, first name, employee type, date hired, job description
        
        #-----------Edit Tab-------------------------------------------------------------------
         
        
        self.addbutton = customtkinter.CTkButton(self.tabview, text="Add", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command = addfunc)
        self.addbutton.grid(row=0, column=0, padx=(780,0), pady=(0,320))
        
        def update_delete(): #di ko pa alam
            self.updtbutton = customtkinter.CTkButton(self.seg_button_1, text="Update", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), width=290)
            self.updtbutton.grid(row=0, column=0, padx=(0,0), pady=(5,5))
            self.delbutton = customtkinter.CTkButton(self.seg_button_1, text="Delete", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), width=290)
            self.delbutton.grid(row=0, column=0, padx=(0,0), pady=(20,20))
        
        
        
        
            
        
        
        #self.toggle_button = customtkinter.CTkButton

app = CIMOS_EmpPage()
app.mainloop()