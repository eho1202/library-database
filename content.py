import tkinter as tk

class Content(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(master=self, text="Welcome Back, Admin", font=("Roboto", 24))
        label.pack(pady=60, padx=10)
        
        bookBtn = tk.Button(self, text="Show Books List", command=lambda: self.controller.show_frame("BooksList"))
        bookBtn.pack(pady=12, padx=10)
        
        receiptBtn = tk.Button(self, text="Show Receipt List", command=lambda: self.controller.show_frame("Receipts"))
        receiptBtn.pack(pady=12, padx=10)
        
        custBtn = tk.Button(self, text="Show Customer List", command=lambda: self.controller.show_frame("Customers"))
        custBtn.pack(pady=12, padx=10)
        
        staffBtn = tk.Button(self, text="Show Staff List", command=lambda: self.controller.show_frame("Staffs"))
        staffBtn.pack(pady=12, padx=10)
        
        categoryBtn = tk.Button(self, text="Show Category List", command=lambda: self.controller.show_frame("Categories"))
        categoryBtn.pack(pady=12, padx=10)
        
        shelfBtn = tk.Button(self, text="Show Shelf List", command=lambda: self.controller.show_frame("Shelves"))
        shelfBtn.pack(pady=12, padx=10)