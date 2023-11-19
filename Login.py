import tkinter as tk
from tkinter import messagebox
import customtkinter
from PIL import Image
import os
import mysql.connector

#magcode ka na Dan!!

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="canteenmanagement"
)

mycursor = mydb.cursor()


customtkinter.set_appearance_mode("Dark")

DIRPATH = os.path.dirname(os.path.abspath(__file__))

themepath = os.path.join(DIRPATH, "red.json")

if os.path.exists(themepath):       
    customtkinter.set_default_color_theme(themepath)
else:
    customtkinter.set_default_color_theme("blue")

    
button_mode = True

class CIMOS_Login(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        # configure window class CIMOS_Admin
        self.title("CIMOS Admin")
        self.geometry(f"1000x580+350+130")
        self.bind("<1>", lambda event: event.widget.focus_set())
        self.resizable(False, False)
        
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.backg = customtkinter.CTkImage(Image.open(os.path.join("he.png")), size=(1100,900))
        self.Image_label = customtkinter.CTkLabel(self, text="", image=self.backg, bg_color="transparent")
        self.Image_label.grid(row=0, column=0, padx=(0,0))
        self.bgc = customtkinter.CTkFrame(self, width=250, corner_radius=0, fg_color="#222222")
        self.bgc.grid(row=0, column=0, padx=(0, 0), pady=(400, 0), sticky="nsew")
        self.bgc2 = customtkinter.CTkFrame(self, width=250, corner_radius=0, fg_color="#222222")
        self.bgc2.grid(row=0, column=0, padx=(0, 0), pady=(0, 440), sticky="nsew")
        self.tabview = customtkinter.CTkFrame(self, width=250, border_color="#222222", bg_color="#222222", corner_radius=20)
        self.tabview.grid(row=0, column=0, padx=(340, 340), pady=(80, 120), sticky="nsew")
        self.profile = customtkinter.CTkImage(Image.open(os.path.join("user.ico")), size=(140,140))
        self.Image_label = customtkinter.CTkLabel(self.tabview, text="", image=self.profile, bg_color="transparent")
        self.Image_label.grid(row=0, column=0, padx=(85,0), pady=(0,120), sticky="ew")
        
        self.logo1 = customtkinter.CTkImage(Image.open(os.path.join("logo2.png")), size=(160,40))
        self.Image_logo1 = customtkinter.CTkLabel(self.tabview, text="", image=self.logo1, bg_color="transparent")
        self.Image_logo1.grid(row=0, column=0, padx=(85,0), pady=(0,315), sticky="ew")
        
        def on_enter(e):
            user.delete(0,'end')

        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Username')

        user = tk.Entry(self.tabview, width = 25, fg = '#566D7E', border=0, bg='white',font=('Microsoft Yahei UI Light',12,'bold'))
        user.place(x=60, y=285)
        user.insert(0,'Username')
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)

        tk.Frame(self.tabview, width=290, height=2, bg='#9F0000').place(x=60,y=310)
        
        #-------------------------------------------------
        def on_enter(e):
            secret.config(show="●")
            secret.delete(0,'end')

        def on_leave(e):
            name=secret.get()
            if name=='':
                secret.insert(0,'Password')

        secret = tk.Entry(self.tabview, width = 25, fg = '#566D7E', border=0, bg='white',font=('Microsoft Yahei UI Light',12,'bold'))
        secret.place(x=60, y=325)
        secret.insert(0,'Password')
        secret.bind('<FocusIn>', on_enter)
        secret.bind('<FocusOut>', on_leave)
        tk.Frame(self.tabview, width=290, height=2, bg='#9F0000').place(x=60,y=350)
        
        
        
        def hide():
            global button_mode
    
            if button_mode:
                eyeButton.config(image=openeye,activebackground="white")
                secret.config(show="")
                button_mode=False
            else:
                eyeButton.config(image=closeeye,activebackground="white")
                secret.config(show="*")
                button_mode=True
                
        openeye=tk.PhotoImage(file="show1.png")
        closeeye=tk.PhotoImage(file="hide1.png")
        eyeButton=tk.Button(self.tabview,image=closeeye,border=0,bg="white",command=hide)
        eyeButton.place(x=320,y=330)

        def login():
            username = user.get()
            password = secret.get()
            if username != 'Username' and password != 'Password':
                mycursor.execute('SELECT password,LoginCredentials FROM logintbl WHERE username=%s', [username])
                result = mycursor.fetchone()
                print(result)
                if result:
                    if (password == result[0] and result[1] == "Admin"):
                        self.destroy()
                        os.system('python adminpage.py')
                    elif (password == result[0] and result[1] == "User"):
                        messagebox.showinfo('Success', 'User Logged in successfully.')
                    else:
                        messagebox.showerror('Error', 'Invalid password.')
                else:
                    messagebox.showerror('Error', 'Invalid Username.')
            else:
                messagebox.showerror('Error', 'Enter all data.')

        

        loginbutton = customtkinter.CTkButton(self.tabview, text="Log in", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command = login)
        loginbutton.grid(row=0, column=0, padx=(85,0), pady=(320,30))



        
        
if __name__ == "__main__":
    app = CIMOS_Login()
    app.mainloop()