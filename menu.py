
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

def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        self.name_entry.insert(0,row[1])
        self.price_entry.insert(0,row[2])
    else:
        pass

def add_to_treeview():
    menu = database.fetch_menu()  # Corrected: Added parentheses to call the function
    tree.delete(*tree.get_children())
    for me in menu:
        tree.insert('', END, values=me)

def upd_to_treeview():
    menu = database.fetch_ID()  # Corrected: Added parentheses to call the function
    tree.delete(*tree.get_children())
    for me in menu:
        tree.insert('', END, values=me)
        
def get_product_id_from_selected_item(selected_item):
    # Assuming that the product ID is stored in the first column (index 0) of the selected item
    item_values = tree.item(selected_item, 'values')
    
    if item_values:
        product_id = item_values[0]  # Adjust the index based on the actual column containing the product ID
        return product_id
    else:
        return None  # Handle the case where values are not found


def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    self.name_entry.delete(0, END)
    self.price_entry.delete(0,END)
    
def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Choose a Dish to Delete.')
    else:
        product_id = get_product_id_from_selected_item(selected_item)
        database.delete_menu(product_id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success', 'Data has been deleted.')
    
def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Choose a Dish to Update.')
    else:
        name = self.name_entry.get()
        pric = self.price_entry.get()
        product_id = get_product_id_from_selected_item(selected_item)
        database.update_menu(ProductID=product_id, newname=name, newprice=pric)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success', 'Data has been updated.')

def insert():
    name = self.name_entry.get()
    pric = self.price_entry.get()
    if not (name and pric):
        messagebox.showerror('Error', 'Enter all requirements.')
    else:
        try:
            database.insert_menu(ProductName=name, Price=int(pric))
            add_to_treeview()
            clear()
            messagebox.showinfo('Success', 'Dish added to the Menu!')
        except ValueError:
            messagebox. showerror('Error', 'Price should be an Integer!')
        
        #-------Current Page---------------------------------------------------------------------------------------------------------------------------------
def home():
    self.destroy()
    os.system('python adminpage.py')

def employeepage():
    self.destroy()
    os.system('python EmployeePage.py')

def salespage():
    print('wala pa')

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
            
    self.empbutton = customtkinter.CTkButton(self.my_frame, text="Employee", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), corner_radius=0, command=employeepage)
    self.empbutton.grid(row=0, column=0, padx=(0,0), pady=(10,290))
            #-----Menu Tab--------------------------------------------------------------------------------------------------------------------------------------------------
    def togmenu2():
        self.empbutton = customtkinter.CTkButton(self.my_frame, text="Employee", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=employeepage)
        self.empbutton.grid(row=0, column=0, padx=(0,0), pady=(10,290))
        self.prodbutton = customtkinter.CTkButton(self.my_frame, text="Menu", fg_color="#FFC3B4", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), corner_radius=0, command=togmenu2)
        self.prodbutton.grid(row=0, column=0, padx=(2,2), pady=(10,220))
        self.salesbutton = customtkinter.CTkButton(self.my_frame, text="Sales", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=salespage)
        self.salesbutton.grid(row=0, column=0, padx=(2,2), pady=(10,150))
        self.homebutton = customtkinter.CTkButton(self.my_frame, text="Home", fg_color="#9f1111", bg_color="transparent", text_color="white", font=customtkinter.CTkFont(size=14, weight="bold"), command=home)
        self.homebutton.grid(row=0, column=0, padx=(2,2), pady=(0,10))

    self.prodbutton = customtkinter.CTkButton(self.my_frame, text="Menu", fg_color="#FFC3B4", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=togmenu2)
    self.prodbutton.grid(row=0, column=0, padx=(2,2), pady=(10,220))
            #------Sales Tab--------------------------------------------------------------------------------------------------------------------------------------------------
                
    self.salesbutton = customtkinter.CTkButton(self.my_frame, text="Sales", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=salespage)
    self.salesbutton.grid(row=0, column=0, padx=(2,2), pady=(10,150))
            
    self.homebutton = customtkinter.CTkButton(self.my_frame, text="Home", fg_color="#9f1111", bg_color="transparent", text_color="white", font=customtkinter.CTkFont(size=14, weight="bold"), command=home)
    self.homebutton.grid(row=0, column=0, padx=(2,2), pady=(0,10))
            
self.menuimg = customtkinter.CTkImage(light_image=Image.open(os.path.join("menu1.png")), dark_image=Image.open(os.path.join("menu.png")),size=(40,40))
self.Image_label = customtkinter.CTkButton(self, text="", image=self.menuimg, fg_color="transparent", width=40, height=40, command=toggle_menu)
self.Image_label.grid(row=0, column=0, padx=(0, 920), pady=(0,500))
self.logo_label = customtkinter.CTkLabel(self, text="Admin Controls - Menu", font=customtkinter.CTkFont("Harrington", size=26, weight="bold"), fg_color="transparent", text_color="White")
self.logo_label.grid(row=0, column=0, padx=(0, 530), pady=(0,500))
        
        #-----------Tab-----------------------------------------------------------------------------------
        
self.tabview = customtkinter.CTkFrame(self, width=320)
self.tabview.grid(row=0, column=0, padx=(20, 640), pady=(100, 30), sticky="nsew")
self.viewframe = customtkinter.CTkFrame(self.tabview, width=300, height=320, fg_color="white", corner_radius=6)
self.viewframe.grid(row=0, column=0, padx=(20, 400), pady=(50,80), sticky="nsw")
self.menulabel = customtkinter.CTkLabel(self.tabview, text="Menu", font=customtkinter.CTkFont("Harrington", size=24, weight="bold"), fg_color="transparent", text_color="White")
self.menulabel.grid(row=0, column=0, padx=(20,405), pady=(10,370))

self.logo1 = customtkinter.CTkImage(Image.open(os.path.join("logo2.png")), size=(130,30))
self.Image_logo1 = customtkinter.CTkLabel(self.viewframe, text="", image=self.logo1, bg_color="transparent")
self.Image_logo1.grid(row=0, column=0, padx=(85,85), pady=(10,200), sticky="nsew")
self.name_label = customtkinter.CTkLabel(self.viewframe, font=font2, text="Dish Name: ", text_color="#222222", bg_color="#fff")
self.name_label.place(x=105, y=50)
self.name_entry = customtkinter.CTkEntry(self.viewframe, font=font2, text_color="#000", fg_color="White", border_color='#9F0000', border_width=2, width=230)
self.name_entry.place(x=35, y=80)

self.price_label = customtkinter.CTkLabel(self.viewframe, font=font2, text="Price: ", text_color="#222222", bg_color="#fff")
self.price_label.place(x=127, y=130)
self.price_entry = customtkinter.CTkEntry(self.viewframe, font=font2, text_color="#000", fg_color="White", border_color='#9F0000', border_width=2, width=230)
self.price_entry.place(x=35, y=160)
self.addmenu = customtkinter.CTkButton(self.viewframe, command=insert, text="Add to Menu", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="#9F0000", text_color="White", width=200)
self.addmenu.place(x=50, y=220)
self.clear = customtkinter.CTkButton(self.tabview, command =lambda:clear(True),text="New", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="white", text_color="#9F0000", width=85, height=85)
self.clear.place(x=20, y=345)
self.updclick = customtkinter.CTkButton(self.tabview, command=update, text="Update", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="#0D347C", text_color="white", width=200, height=35, hover_color="#148824")
self.updclick.place(x=120, y=345)
self.delclick = customtkinter.CTkButton(self.tabview, command=delete, text="Delete", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="#0D347C", text_color="white", width=200, height=35, hover_color="#570000")
self.delclick.place(x=120, y=395)

self.treeframe = customtkinter.CTkFrame(self, width=555, height=440)
self.treeframe.place(x=420, y=100)

style = ttk.Style(self.treeframe)
style.theme_use('clam')
style.configure('Treeview', font=font3, foreground='#fff', background='#0a0b0c', fieldbackground='#222222', rowheight=40)
style.map('Treeview', background=[('selected', '#9F0000')])

tree = ttk.Treeview(self.treeframe, height=13)

tree['columns'] = ('ProductID', 'ProductName', 'Price')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('ProductID', anchor=tk.CENTER, width=230)
tree.column('ProductName', anchor=tk.CENTER, width=230)
tree.column('Price', anchor=tk.CENTER, width=230)

tree.heading('ProductID', text='ProductID')
tree.heading('ProductName', text='Name')
tree.heading('Price', text='Price')

tree.place(x=0, y=0)

vsb = tk.Scrollbar(self.treeframe, orient="vertical", command=tree.yview, width=16)
vsb.place(x=678, y=2, height=545)  # Adjust height as needed

        # Configure the Treeview to use the scrollbar
tree.configure(yscrollcommand=vsb.set)

tree.bind('<ButtonRelease>', display_data)

add_to_treeview()
      
self.mainloop()