import tkinter as tk
import login

class Content(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(master=self, text="Welcome Back, Admin", font=("Roboto", 24))
        label.pack(pady=60, padx=10)
        
        bookBtn = tk.Button(self, text="Show Books List", command=lambda: self.controller.show_frame("BooksList"))
        bookBtn.pack(pady=12, padx=10)
        
        custBtn = tk.Button(self, text="Show Customer List")
        custBtn.pack(pady=12, padx=10)
        
        staffBtn = tk.Button(self, text="Show Staff List")
        staffBtn.pack(pady=12, padx=10)