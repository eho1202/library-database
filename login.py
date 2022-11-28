import tkinter as tk
from tkinter import StringVar, messagebox
import re
import cx_Oracle
import config

sql = 'select isbn, booktitle from book order by booktitle'

class Login(tk.Frame):
    def on_focus_in(self, entry):
        if 'Username' or 'Password' in entry.get():
            entry.delete(0, 'end')


    def on_focus_out(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            
    def updateConfig(self):
        self.username = self.userEntry.get()
        self.password = self.passEntry.get()
        with open("config.py", "r") as cf:
            lines = cf.readlines()
        with open("config.py", "w") as cf:
            for line in lines:
                line = re.sub('useruser', self.username, line)
                line = re.sub('passpass', self.password, line)
                cf.write(line)
            cf.close()
            
    def login(self):
            self.username = self.userEntry.get()
            self.password = self.passEntry.get()
            if ('Username' in self.userEntry.get() or "Password" in self.passEntry.get()):
                messagebox.showerror("Error", "Enter a valid username or password!")
            elif (not self.userEntry.get() or not self.passEntry.get()):
                messagebox.showerror("Error", "Enter your username or password!")
            else:
                self.updateConfig()
                self.controller.show_frame("Content")
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.username = StringVar()
        self.password = StringVar()

        label = tk.Label(self, text="Library Database", font=("Roboto", 24))
        label.pack(pady=72, padx=10)

        self.userEntry = tk.Entry(self, textvariable=self.username)
        self.userEntry.insert(0, "e10ho")
        self.userEntry.pack(pady=12, padx=10)
        
        user_focus_in = self.userEntry.bind('<Button-1>', lambda x: self.on_focus_in(self.userEntry))
        user_focus_out = self.userEntry.bind('<FocusOut>', lambda x: self.on_focus_out(self.userEntry, "Username"))

        self.passEntry = tk.Entry(self, show="*", textvariable=self.password)
        self.passEntry.insert(0, "12022253")
        self.passEntry.pack(pady=12, padx=10)
        
        pass_focus_in = self.passEntry.bind('<Button-1>', lambda x: self.on_focus_in(self.passEntry))
        pass_focus_out = self.passEntry.bind('<FocusOut>', lambda x: self.on_focus_out(self.passEntry, "Password"))

        loginBtn = tk.Button(self, text="Login", command=lambda: self.login())
        loginBtn.pack(pady=12, padx=10)

        # checkbox = tk.CTkCheckBox(master=frame, text="Remember Me")
        # checkbox.pack(pady=12, padx=10)
        
    