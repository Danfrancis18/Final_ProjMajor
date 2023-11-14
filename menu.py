import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("light")

DIRPATH = os.path.dirname(os.path.abspath(__file__))

themepath = os.path.join(DIRPATH, "red.json")

if os.path.exists(themepath):       
    customtkinter.set_default_color_theme(themepath)
else:
    customtkinter.set_default_color_theme("blue")
    


class CIMOS_MenuPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Employee Management")
        self.geometry(f"1000x580+350+130")
        self.bind("<1>", lambda event: event.widget.focus_set())
        self.resizable(False, False)
        
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        
        #-------Current Page---------------------------------------------------------------------------------------------------------------------------------
        self.menuimg = customtkinter.CTkImage(light_image=Image.open(os.path.join("menu1.png")), dark_image=Image.open(os.path.join("menu.png")),size=(40,40))
        self.Image_label = customtkinter.CTkButton(self, text="", image=self.menuimg, fg_color="transparent", width=40, height=40)
        self.Image_label.grid(row=0, column=0, padx=(0, 920), pady=(0,500))
        self.logo_label = customtkinter.CTkLabel(self, text="Admin Controls - Menu", font=customtkinter.CTkFont("Harrington", size=26, weight="bold"), fg_color="transparent", text_color="White")
        self.logo_label.grid(row=0, column=0, padx=(0, 530), pady=(0,500))
        
        #-----------Tab-----------------------------------------------------------------------------------
        
        self.tabview = customtkinter.CTkFrame(self, width=250)
        self.tabview.grid(row=0, column=0, padx=(20, 20), pady=(100, 60), sticky="nsew")
        self.viewframe = customtkinter.CTkFrame(self.tabview, width=900, height=320, fg_color="white", corner_radius=6)
        self.viewframe.grid(row=0, column=0, padx=(30,10), pady=(65,0), sticky="nsew")
        
app = CIMOS_MenuPage()
app.mainloop()