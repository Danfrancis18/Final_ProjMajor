import tkinter as tk
from tkinter import messagebox
import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("Dark")

DIRPATH = os.path.dirname(os.path.abspath(__file__))

themepath = os.path.join(DIRPATH, "red.json")

if os.path.exists(themepath):       
    customtkinter.set_default_color_theme(themepath)
else:
    customtkinter.set_default_color_theme("blue")

class CIMOS_Admin(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        def goto_employee():
            self.destroy()
            import EmployeePage

        def goto_menu():
            self.destroy()
            import menu

        def goto_sales():
            print('placeholder command')
            return

        def logout():
            response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
            if response == 1:
                self.destroy()
                os.system('python Login.py')
            else:
                return


        # configure window class CIMOS_Admin
        self.title("CIMOS Admin")
        self.geometry(f"1000x580+350+130")
        self.bind("<1>", lambda event: event.widget.focus_set())
        self.resizable(False, False)
        
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.backg = customtkinter.CTkImage(Image.open(os.path.join("he.png")), size=(780,700))
        self.Image_label = customtkinter.CTkLabel(self, text="", image=self.backg, bg_color="transparent")
        self.Image_label.grid(row=0, column=0, padx=(220,0))

        #Admin Profile
        self.my_frame = customtkinter.CTkFrame(self, width=220, corner_radius=0)
        self.my_frame.grid(row=0, column=0, rowspan=4, columnspan=1 , sticky="nsw")
        self.profile = customtkinter.CTkImage(Image.open(os.path.join("user.ico")), size=(140,140))
        self.Image_label = customtkinter.CTkLabel(self.my_frame, text="", image=self.profile, bg_color="transparent")
        self.Image_label.grid(row=0, column=0, padx=(40,40), pady=(30,70))
        self.linedesprof1 = tk.Frame(self.my_frame, width=45, height=2, bg="#9F0000")
        self.linedesprof1.grid(row=0,column=0, padx=(0,230), pady=(200,0))
        self.linedesprof2 = tk.Frame(self.my_frame, width=45, height=2, bg="#9F0000")
        self.linedesprof2.grid(row=0,column=0, padx=(230,0), pady=(200,0))
        self.logo_label = customtkinter.CTkLabel(self.my_frame, text="Admin Profile", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=(0,0), pady=(160, 0))
        self.outbutton = customtkinter.CTkButton(self.my_frame, text="Log out", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=logout)
        self.outbutton.grid(row=1, column=0, padx=(10,10), pady=(300,0), sticky="ew")
        
        
        #Interface Title
        self.labelframe=customtkinter.CTkFrame(master=self, width=220, height=10, corner_radius=9)
        self.labelframe.grid(row=0, column=0, padx=(240,20), pady=(60,230), sticky="new")
        self.logo_label = customtkinter.CTkLabel(self.labelframe, text="Canteen Inventory Management and Ordering System", font=customtkinter.CTkFont("NEXA", size=24, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=70, pady=(10, 10))
        
        
        # choice
        self.choose_des1 = customtkinter.CTkFrame(self, height=200, fg_color="white")
        self.choose_des1.grid(row=0, column=0, columnspan=2, padx=(240,20) , pady=(140, 420), sticky="nsew")
        
        #------------------------------------------------------------------------------------------------------
        self.choose_frame = customtkinter.CTkFrame(self, height=200)
        self.choose_frame.grid(row=0, column=0, padx=(240,20) , pady=(170, 120), columnspan=3, sticky="nsew")
        self.buttonchoose = customtkinter.CTkFrame(self.choose_frame, width=700, height=35, fg_color="#666666")
        self.buttonchoose.grid(row=0, column=0, columnspan=3, padx=(20,20) , pady=(240, 40), sticky="nsew")
        self.empbutton = customtkinter.CTkButton(self.choose_frame, text="Employee", bg_color="#666666", font=customtkinter.CTkFont(size=14, weight="bold"), command=goto_employee)
        self.empbutton.grid(row=0, column=0, padx=(55,500), pady=(240,40))
        self.prodbutton = customtkinter.CTkButton(self.choose_frame, text="Menu", bg_color="#666666", font=customtkinter.CTkFont(size=14, weight="bold"), command=goto_menu)
        self.prodbutton.grid(row=0, column=0, padx=(30,0), pady=(240,40))
        self.salesbutton = customtkinter.CTkButton(self.choose_frame, text="Sales", bg_color="#666666", font=customtkinter.CTkFont(size=14, weight="bold"), command=goto_sales)
        self.salesbutton.grid(row=0, column=0, padx=(510,0), pady=(240,40))
        #------------------------------------------------------------------------------------------------------
        self.linedes = tk.Frame(self.choose_frame, width=2, height=220, bg='#555555')
        self.linedes.grid(row=0,column=0, padx=(0,260), pady=(0,100))
        self.linedes2 = tk.Frame(self.choose_frame, width=2, height=220, bg='#555555')
        self.linedes2.grid(row=0,column=0, padx=(340,0), pady=(0,100))
        self.choose_des2 = customtkinter.CTkFrame(self, height=200, fg_color="white")
        self.choose_des2.grid(row=0, column=0, columnspan=2, padx=(240,20) , pady=(470, 90), sticky="nsew")
        
        #Image Icons
        self.image1 = customtkinter.CTkImage(light_image=Image.open(os.path.join("management2.png")), dark_image=Image.open(os.path.join("management1.png")),size=(160,160))
        self.Image_label = customtkinter.CTkLabel(self.choose_frame, text="", image=self.image1, bg_color="transparent")
        self.Image_label.grid(row=0, column=0, padx=(0,450), pady=(0,70))
        self.image2 = customtkinter.CTkImage(Image.open(os.path.join("dish1.png")), dark_image=Image.open(os.path.join("dish (1).png")), size=(160,160))
        self.Image_label = customtkinter.CTkLabel(self.choose_frame, text="", image=self.image2, bg_color="transparent")
        self.Image_label.grid(row=0, column=0, padx=(35,0), pady=(0,70))
        self.image3 = customtkinter.CTkImage(Image.open(os.path.join("sales1.png")), dark_image=Image.open(os.path.join("sales.png")), size=(160,160))
        self.Image_label = customtkinter.CTkLabel(self.choose_frame, text="", image=self.image3, bg_color="transparent")
        self.Image_label.grid(row=0, column=0, padx=(540,0), pady=(0,70))


if __name__ == "__main__":
    app = CIMOS_Admin()
    app.mainloop()
        
        