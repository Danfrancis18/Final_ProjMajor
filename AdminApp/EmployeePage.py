import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("Light")

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
        
        def toggle_menu():
            def collapse_menu():
                self.my_frame.destroy()
                self.menuimg = customtkinter.CTkImage(light_image=Image.open(os.path.join("menu1.png")), dark_image=Image.open(os.path.join("menu.png")),size=(40,40))
                self.Image_label = customtkinter.CTkButton(self, text="", image=self.menuimg, fg_color="transparent", width=40, height=40, command=toggle_menu)
                self.Image_label.grid(row=0, column=0, padx=(0, 920), pady=(0,500))
                
            self.my_frame = customtkinter.CTkFrame(self, width=220, height=40, corner_radius=10, fg_color="white", bg_color="transparent")
            self.my_frame.grid(row=0, column=0, padx=(0, 820), pady=(70,200), sticky="ns")
            self.menuimg = customtkinter.CTkImage(light_image=Image.open(os.path.join("menu1.png")), dark_image=Image.open(os.path.join("menu.png")),size=(40,40))
            self.Image_label = customtkinter.CTkButton(self, text="", image=self.menuimg, fg_color="transparent", width=40, height=40, command=collapse_menu)
            self.Image_label.grid(row=0, column=0, padx=(0, 920), pady=(0,500))
        #----Menu----------------------------------------------------------------------------------------------------------------------------------------------------
            #----Employee Tab----------------------------------------------------------------------------------------------------------------------------------------------------------
            def togmenu1():
                self.empbutton = customtkinter.CTkButton(self.my_frame, text="Employee", fg_color="#FFC3B4", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), corner_radius=0, command=togmenu1)
                self.empbutton.grid(row=0, column=0, padx=(0,0), pady=(20,100))
                self.prodbutton = customtkinter.CTkButton(self.my_frame, text="Product", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu2)
                self.prodbutton.grid(row=0, column=0, padx=(2,2), pady=(0,0))
                self.salesbutton = customtkinter.CTkButton(self.my_frame, text="Sales", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu3)
                self.salesbutton.grid(row=0, column=0, padx=(2,2), pady=(100,20))
            
            self.empbutton = customtkinter.CTkButton(self.my_frame, text="Employee", fg_color="#FFC3B4", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), corner_radius=0, command=togmenu1)
            self.empbutton.grid(row=0, column=0, padx=(0,0), pady=(20,100))
            #-----Product Tab--------------------------------------------------------------------------------------------------------------------------------------------------
            def togmenu2():
                self.empbutton = customtkinter.CTkButton(self.my_frame, text="Employee", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu1)
                self.empbutton.grid(row=0, column=0, padx=(0,0), pady=(20,100))
                self.prodbutton = customtkinter.CTkButton(self.my_frame, text="Product", fg_color="#FFC3B4", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), corner_radius=0, command=togmenu2)
                self.prodbutton.grid(row=0, column=0, padx=(2,2), pady=(0,0))
                self.salesbutton = customtkinter.CTkButton(self.my_frame, text="Sales", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu3)
                self.salesbutton.grid(row=0, column=0, padx=(2,2), pady=(100,20))

            self.prodbutton = customtkinter.CTkButton(self.my_frame, text="Product", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu2)
            self.prodbutton.grid(row=0, column=0, padx=(2,2), pady=(0,0))
            #------Sales Tab--------------------------------------------------------------------------------------------------------------------------------------------------
            def togmenu3():
                self.empbutton = customtkinter.CTkButton(self.my_frame, text="Employee", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu1)
                self.empbutton.grid(row=0, column=0, padx=(0,0), pady=(20,100))
                self.prodbutton = customtkinter.CTkButton(self.my_frame, text="Product", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu2)
                self.prodbutton.grid(row=0, column=0, padx=(2,2), pady=(0,0))
                self.salesbutton = customtkinter.CTkButton(self.my_frame, text="Sales", fg_color="#FFC3B4", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), corner_radius=0, command=togmenu3)
                self.salesbutton.grid(row=0, column=0, padx=(2,2), pady=(100,20))
                
            self.salesbutton = customtkinter.CTkButton(self.my_frame, text="Sales", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu3)
            self.salesbutton.grid(row=0, column=0, padx=(2,2), pady=(100,20))
        
        #-------Current Page---------------------------------------------------------------------------------------------------------------------------------
        self.menuimg = customtkinter.CTkImage(light_image=Image.open(os.path.join("menu1.png")), dark_image=Image.open(os.path.join("menu.png")),size=(40,40))
        self.Image_label = customtkinter.CTkButton(self, text="", image=self.menuimg, fg_color="transparent", width=40, height=40, command=toggle_menu)
        self.Image_label.grid(row=0, column=0, padx=(0, 920), pady=(0,500))
        self.logo_label = customtkinter.CTkLabel(self, text="Admin Controls - Employee", font=customtkinter.CTkFont("Harrington", size=26, weight="bold"), fg_color="transparent", text_color="White")
        self.logo_label.grid(row=0, column=0, padx=(0, 530), pady=(0,500))
        
        #-----------Tab-----------------------------------------------------------------------------------
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=0, padx=(20, 20), pady=(100, 60), sticky="nsew")
        self.tabview.add("View")
        self.tabview.add("Edit")
        self.tabview.tab("View").grid_columnconfigure(0, weight=1) # configure grid of individual tabs
        self.tabview.tab("Edit").grid_columnconfigure(0, weight=1)
        
        #-------------View------------------------------------------------------------------
        self.label_tab_1 = customtkinter.CTkFrame(self.tabview.tab("View"), height=150)
        self.label_tab_1.grid(row=0, column=0, padx=(5,0), pady=20)
            #-----------View Tab--------------
            #----dito ishoshow yung data, current employee, employee info-------------
        self.viewframe = customtkinter.CTkFrame(self.label_tab_1, width=900, height=320, fg_color="white", corner_radius=6)
        self.viewframe.grid(row=0, column=0, padx=(10,10), pady=(0,10), sticky="nsew")
    
        self.scrollbar = customtkinter.CTkScrollbar(self.tabview.tab("View"), height=300)
        self.scrollbar.grid(row=0, column=1, padx=5, pady=(16,25), sticky="nsew")
        
        self.scrollbar.set(0,0)
            #-------------------------------------------------------------------------------
        
        def addfunc():
            self.addbutton.configure(self.seg_button_1, text="Add", bg_color="transparent", fg_color="#e86161", font=customtkinter.CTkFont(size=14, weight="bold"), width=290, command = addfunc)
            self.addbutton.grid(row=0, column=0, padx=(10,650), pady=(5,5))
            self.ln = customtkinter.CTkLabel(self.tabview.tab("Edit"), text="Last Name: ")
            self.ln.grid(row=0, column=0, padx=(80,650), pady=(80,5), sticky="nw")
            self.fn = customtkinter.CTkLabel(self.tabview.tab("Edit"), text="First Name: ")
            self.fn.grid(row=0, column=0, padx=(80,650), pady=(120,5), sticky="nw")
            self.ep = customtkinter.CTkLabel(self.tabview.tab("Edit"), text="Employee Type: ")
            self.ep.grid(row=0, column=0, padx=(80,675), pady=(160,5), sticky="nw")
            self.jd = customtkinter.CTkLabel(self.tabview.tab("Edit"), text="Job Description: ")
            self.jd.grid(row=0, column=0, padx=(80,680), pady=(230,5), sticky="nw")
            self.dh = customtkinter.CTkLabel(self.tabview.tab("Edit"), text="Date Hired: ")
            self.dh.grid(row=0, column=0, padx=(80,680), pady=(270,5), sticky="nw")
        
            self.lnentry = customtkinter.CTkEntry(self.tabview.tab("Edit"), placeholder_text="Enter last name...")
            self.lnentry.grid(row=0, column=0, padx=(160,40), pady=(80,330), sticky="nsew")
            self.fnentry = customtkinter.CTkEntry(self.tabview.tab("Edit"), placeholder_text="Enter first name...")
            self.fnentry.grid(row=0, column=0, padx=(160,40), pady=(120,290), sticky="nsew")
        
            self.ep_frame = customtkinter.CTkFrame(self.tabview.tab("Edit"))
            self.ep_frame.grid(row=0, column=0, padx=(170, 0), pady=(155,85), sticky="nsw")
            self.radio_var = tkinter.IntVar(value=0)
            self.radio_button_1 = customtkinter.CTkRadioButton(self.ep_frame, variable=self.radio_var, value=0, text="Full Time", border_color="#e86161")
            self.radio_button_1.grid(row=1, column=2, padx=(20,20), pady=(10,0), sticky="nw")
            self.radio_button_2 = customtkinter.CTkRadioButton(self.ep_frame, variable=self.radio_var, value=1, text="Part Time", border_color="#e86161")
            self.radio_button_2.grid(row=2, column=2, padx=(20,20), pady=(10,10), sticky="nw")
        
            self.jdchoose = customtkinter.CTkOptionMenu(self.tabview.tab("Edit"), dynamic_resizing=False, values=["Manager", "Cashier", "Delivery", "Dishwasher", "Waiter"], button_color="white", button_hover_color="#222222")
            self.jdchoose.grid(row=0, column=0, padx=(180,40), pady=(230, 182), sticky="nsew")
            self.jdchoose.set("-Choose-")
        
            self.dhentry = customtkinter.CTkEntry(self.tabview.tab("Edit"), placeholder_text="YYYY/MM/DD...")
            self.dhentry.grid(row=0, column=0, padx=(160,40), pady=(270,145), sticky="nsew")
            
            self.add2button=customtkinter.CTkButton(self.tabview.tab("Edit"), text="Add Employee", bg_color="transparent", fg_color="#222222", text_color="white", font=customtkinter.CTkFont(size=14, weight="bold"), width=290)
            self.add2button.grid(row=0, column=0, padx=(100,100), pady=(220,0), sticky="ew")
        
            #employee code, last name, first name, employee type, date hired, job description
        
        #-----------Edit Tab-------------------------------------------------------------------  
        self.optionmenu = customtkinter.CTkFrame(self.tabview.tab("Edit"), height=150)
        self.optionmenu.grid(row=0, column=0, padx=(0,0), pady=(20, 10))
        self.seg_button_1 = customtkinter.CTkFrame(self.tabview.tab("Edit"), fg_color="white")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="new")
        self.addbutton = customtkinter.CTkButton(self.seg_button_1, text="Add", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), width=290, command = addfunc)
        self.addbutton.grid(row=0, column=0, padx=(10,650), pady=(5,5))
        self.updtbutton = customtkinter.CTkButton(self.seg_button_1, text="Update", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), width=290)
        self.updtbutton.grid(row=0, column=0, padx=(0,45), pady=(5,5))
        self.delbutton = customtkinter.CTkButton(self.seg_button_1, text="Delete", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), width=290)
        self.delbutton.grid(row=0, column=0, padx=(550,0), pady=(5,5))
        
        
        
        
            
        
        
        #self.toggle_button = customtkinter.CTkButton

app = CIMOS_EmpPage()
app.mainloop()