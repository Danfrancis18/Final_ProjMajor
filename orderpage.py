
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import os
import database

customtkinter.set_appearance_mode("light")

DIRPATH = os.path.dirname(os.path.abspath(__file__))

themepath = os.path.join(DIRPATH, "red.json")

if os.path.exists(themepath):       
    customtkinter.set_default_color_theme(themepath)
else:
    customtkinter.set_default_color_theme("blue")

# configure window
self = customtkinter.CTk()
self.title("Employee Management")
self.geometry(f"1000x580+350+130")
self.bind("<1>", lambda event: event.widget.focus_set())
self.resizable(False, False)
        
self.grid_rowconfigure(0, weight=1)  # configure grid system
self.grid_columnconfigure(0, weight=1)

font1 = ('Arial', 25, 'bold')
font2 = ('Arial', 18, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 30, 'bold')
        
        #-------Current Page---------------------------------------------------------------------------------------------------------------------------------
def logout():
    response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if response == 1:
        self.destroy()
        os.system('python Login.py')
    else:
        return

def home():
    self.destroy()
    os.system('python adminpage.py')

def toggle_menu():
    def collapse_menu():
        self.my_frame.destroy()
        self.menuimg = customtkinter.CTkImage(light_image=Image.open(os.path.join("menu1.png")), dark_image=Image.open(os.path.join("menu.png")),size=(40,40))
        self.Image_label = customtkinter.CTkButton(self, text="", image=self.menuimg, fg_color="transparent", width=40, height=40, command=toggle_menu)
        self.Image_label.grid(row=0, column=0, padx=(0, 920), pady=(0,500))
                
    self.my_frame = customtkinter.CTkFrame(self, width=220, height=100, corner_radius=10, fg_color="white", bg_color="transparent")
    self.my_frame.grid(row=0, column=0, padx=(60, 700), pady=(20,490), sticky="ns")
    self.menuimg = customtkinter.CTkImage(light_image=Image.open(os.path.join("menu1.png")), dark_image=Image.open(os.path.join("menu.png")),size=(40,40))
    self.Image_label = customtkinter.CTkButton(self, text="", image=self.menuimg, fg_color="transparent", width=40, height=40, command=collapse_menu)
    self.Image_label.grid(row=0, column=0, padx=(0, 920), pady=(0,500))
        #----Menu----------------------------------------------------------------------------------------------------------------------------------------------------
            #----Employee Tab----------------------------------------------------------------------------------------------------------------------------------------------------------   
            
    self.lobutton = customtkinter.CTkButton(self.my_frame, text="Log out", fg_color="#9f1111", bg_color="transparent", text_color="white", font=customtkinter.CTkFont(size=14, weight="bold"), width=200, command=logout)
    self.lobutton.grid(row=0, column=0, padx=(5,5), pady=(5,100), sticky="ns")
    
    def pop():      
        self.passframe = customtkinter.CTkToplevel(self,fg_color="#333333")
        self.passframe.title("Change Password")
        self.passframe.geometry("180x260+462+235")
        self.passframe.grab_set()
        
        self.current = customtkinter.CTkLabel(self.passframe, font=('Microsoft YaHei UI Light', 10), text="Current Password: ", text_color="white", bg_color="transparent")
        self.current.place(x=20, y=10)
        self.cupass_entry = customtkinter.CTkEntry(self.passframe, font=('Microsoft YaHei UI Light', 10), text_color="#000", fg_color="White", border_color='#9F0000', border_width=0, width=140, height=20)
        self.cupass_entry.place(x=20, y=40)
        
        self.newp = customtkinter.CTkLabel(self.passframe, font=('Microsoft YaHei UI Light', 10), text="New Password: ", text_color="white", bg_color="transparent")
        self.newp.place(x=20, y=70)
        self.nupass_entry = customtkinter.CTkEntry(self.passframe, font=('Microsoft YaHei UI Light', 10), text_color="#000", fg_color="White", border_color='#9F0000', border_width=0, width=140, height=20)
        self.nupass_entry.place(x=20, y=100)
        
        self.conp = customtkinter.CTkLabel(self.passframe, font=('Microsoft YaHei UI Light', 10), text="Confirm Password: ", text_color="white", bg_color="transparent")
        self.conp.place(x=20, y=130)
        self.confirm_entry = customtkinter.CTkEntry(self.passframe, font=('Microsoft YaHei UI Light', 10), text_color="#000", fg_color="White", border_color='#9F0000', border_width=0, width=140, height=20)
        self.confirm_entry.place(x=20, y=160)
        
        changebutton = customtkinter.CTkButton(self.passframe, text="Change Password", bg_color="transparent", text_color="White", font=customtkinter.CTkFont('Microsoft YaHei UI', size=10, weight="bold"), command = None, fg_color="#9F0000")
        changebutton.place(x=20, y=215)
    
    self.chabutton = customtkinter.CTkButton(self.my_frame, text="Change Password", fg_color="#333333", bg_color="transparent", text_color="white", font=customtkinter.CTkFont('Microsoft YaHei UI', size=12, weight="bold"), width=160, height=8, command=pop)
    self.chabutton.grid(row=0, column=0, padx=(5,5), pady=(35,70), sticky="ns")
            
self.menuimg = customtkinter.CTkImage(light_image=Image.open(os.path.join("menu1.png")), dark_image=Image.open(os.path.join("menu.png")),size=(40,40))
self.Image_label = customtkinter.CTkButton(self, text="", image=self.menuimg, fg_color="transparent", width=40, height=40, command=toggle_menu)
self.Image_label.grid(row=0, column=0, padx=(0, 920), pady=(0,500))
self.logo_label = customtkinter.CTkLabel(self, text="Welcome *USER*!", font=customtkinter.CTkFont("Harrington", size=26, weight="bold"), fg_color="transparent", text_color="White")
self.logo_label.grid(row=0, column=0, padx=(0, 640), pady=(0,500))
        
        #-----------Tab-----------------------------------------------------------------------------------
        
self.tabview = customtkinter.CTkFrame(self, width=320)
self.tabview.grid(row=0, column=0, padx=(20, 640), pady=(100, 30), sticky="nsew")
self.viewframe = customtkinter.CTkFrame(self.tabview, width=300, height=500, fg_color="white", corner_radius=6)
self.viewframe.grid(row=0, column=0, padx=(20, 620), pady=(20,600), sticky="nsw")

self.logo1 = customtkinter.CTkImage(Image.open(os.path.join("logo2.png")), size=(260,60))
self.Image_logo1 = customtkinter.CTkLabel(self.viewframe, text="", image=self.logo1, bg_color="transparent")
self.Image_logo1.grid(row=0, column=0, padx=(20,20), pady=(10,280), sticky="nsew")

style = ttk.Style(self.viewframe)
style.theme_use('clam')
style.configure('Treeview', font=font3, foreground='#fff', background='#0a0b0c', fieldbackground='white', rowheight=30)
style.map('Treeview', background=[('selected', '#9F0000')])

tree = ttk.Treeview(self.viewframe, height=9)

tree['columns'] = ('OrderedQuantity', 'ProductName', 'Price')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('OrderedQuantity', anchor=tk.CENTER, width=122)
tree.column('ProductName', anchor=tk.CENTER, width=125)
tree.column('Price', anchor=tk.CENTER, width=125)

tree.heading('OrderedQuantity', text='Quantity')
tree.heading('ProductName', text='Name')
tree.heading('Price', text='Price')

tree.place(x=0, y=100)

vsb = ttk.Scrollbar(self.viewframe, orient="vertical", command=tree.yview)
vsb.place(x=360, y=126, height=273)

tree.configure(yscrollcommand=vsb.set)
self.name_label = customtkinter.CTkLabel(self.viewframe, font=('Arial', 12, 'bold'), text="Total Price                                    :", text_color="#222222", bg_color="#fff")
self.name_label.place(x=20, y=320)
self.name_entry = customtkinter.CTkEntry(self.viewframe, font=('Arial', 12, 'bold'), text_color="#222222", fg_color="White", border_color='white', border_width=2, width=90)
self.name_entry.place(x=200, y=320)
self.takeord = customtkinter.CTkButton(self.tabview, text="Take Orders", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), width=200)
self.takeord.place(x=70, y=400)

self.yumyum = customtkinter.CTkScrollableFrame(self, width=620, height=580, corner_radius=0, scrollbar_button_hover_color="white", scrollbar_fg_color="#9F0000", scrollbar_button_color="#9F0000")
self.yumyum.grid(row=0, column=0, padx=(380,0), pady=0)
self.ulam1 = customtkinter.CTkFrame(self.yumyum, width=150, height=150, corner_radius=12, fg_color="white")
self.ulam1.grid(row=0, column=0, padx=(55,30), pady=(120,20))
self.ulam2 = customtkinter.CTkFrame(self.yumyum, width=150, height=150, corner_radius=12, fg_color="white")
self.ulam2.grid(row=0, column=1, padx=0, pady=(120,20))
self.ulam3 = customtkinter.CTkFrame(self.yumyum, width=150, height=150, corner_radius=12, fg_color="white")
self.ulam3.grid(row=0, column=2, padx=30, pady=(120,20))

self.ulam4 = customtkinter.CTkFrame(self.yumyum, width=150, height=150, corner_radius=12, fg_color="white")
self.ulam4.grid(row=1, column=0, padx=(55,30), pady=(50,50))
self.ulam5 = customtkinter.CTkFrame(self.yumyum, width=150, height=150, corner_radius=12, fg_color="white")
self.ulam5.grid(row=1, column=1, padx=0, pady=(50,50))
self.ulam6 = customtkinter.CTkFrame(self.yumyum, width=150, height=150, corner_radius=12, fg_color="white")
self.ulam6.grid(row=1, column=2, padx=30, pady=(50,50))

#-------------wala lng to tira tira sa copy paste galing sa menu----------------------------------------------------------------

#self.price_label = customtkinter.CTkLabel(self.viewframe, font=font2, text="Price: ", text_color="#222222", bg_color="#fff")
#self.price_label.place(x=127, y=130)
#self.price_entry = customtkinter.CTkEntry(self.viewframe, font=font2, text_color="#000", fg_color="White", border_color='#9F0000', border_width=2, width=230)
#self.price_entry.place(x=35, y=160)

#self.clear = customtkinter.CTkButton(self.tabview,text="New", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="white", text_color="#9F0000", width=85, height=85)
#self.clear.place(x=20, y=345)
#self.updclick = customtkinter.CTkButton(self.tabview, text="Update", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="#0D347C", text_color="white", width=200, height=35, hover_color="#148824")
#self.updclick.place(x=120, y=345)
#self.delclick = customtkinter.CTkButton(self.tabview, text="Delete", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="#0D347C", text_color="white", width=200, height=35, hover_color="#570000")
#self.delclick.place(x=120, y=395)
      
self.mainloop()