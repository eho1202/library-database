import tkinter as tk
import login
import content
import bookslist
import client
import staff
import category
import shelf
import borrowedbooks

class App(tk.Tk):
    
    WIDTH = 1050
    HEIGHT = 700
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Library Database")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (login.Login, content.Content, bookslist.BooksList, client.Customers, staff.Staffs, category.Categories, shelf.Shelves, borrowedbooks.Receipts):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()