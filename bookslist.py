import tkinter as tk
from tkinter import Toplevel, StringVar, messagebox
from pandastable import Table
import pandas as pd
import cx_Oracle
import config
import login

class BooksList(tk.Frame):
    def on_focus_in(self, entry):
        if 'ISBN' or 'Book Title' or 'Author LastName' or 'Author FirstName' or 'Category ID' or 'Lanugage' in entry.get():
            entry.delete(0, 'end')
        elif entry.get():
            pass

    def on_focus_out(self, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)
            
    def getBooks(self):
        try:
            connection = cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding)

            # show the version of the Oracle Database
            with connection.cursor() as cursor:
                cursor.execute('select * from book order by booktitle')
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        self.bookslist.append(row)
                connection.commit()
                connection.close()
        except cx_Oracle.Error as error:
            print(error)
            
    def makeTable(self):
        df = pd.DataFrame(self.bookslist)
        df.columns = ['ISBN', 'Book Title', 'Author LastName', 'Author FirstName', 'Category ID', 'Language'] # Rename the column names
        pt = Table(self, dataframe=df)
        pt.show()
        
    def submitRow(self):
        self.isbn = self.isbnEntry.get()
        self.title = self.titleEntry.get()
        self.last = self.lNameEntry.get()
        self.first = self.fNameEntry.get()
        self.cat = self.catEntry.get()
        self.lang = self.langEntry.get()
        if ('ISBN' in self.isbnEntry.get() or 
            "Book Title" in self.titleEntry.get() or 
            "Author LastName" in self.lNameEntry.get() or 
            "Author FirstName" in self.fNameEntry.get() or 
            "Category ID" in self.catEntry.get() or 
            "Language" in self.langEntry.get()):
            messagebox.showerror("Error", "Enter a valid username or password!")
        elif (not self.isbnEntry.get() or not self.titleEntry.get() or not self.lNameEntry.get() or not self.fNameEntry.get() or not self.catEntry.get() or not self.langEntry.get()):
            messagebox.showerror("Error", "Enter your username or password!")
        else:
            try:
                connection = cx_Oracle.connect(
                    config.username,
                    config.password,
                    config.dsn,
                    encoding=config.encoding)

                # show the version of the Oracle Database
                with connection.cursor() as cursor:
                    cursor.execute("insert into book values (:1, :2, :3, :4, :5, :6)", (self.isbn, self.title, self.last, self.first, self.cat, self.lang))
                    cursor.close()
                    connection.commit()
                    connection.close()
                    print('Succuess!')
            except cx_Oracle.Error as error:
                print(error)
            self.insertWindow.destroy
            self.bookslist.clear()
            self.getBooks()
            self.makeTable()
    
    def addRow(self):
        self.insertWindow = Toplevel(self)
        self.insertWindow.title("Add Row")
        self.insertWindow.geometry("400x300")
        
        self.isbn = StringVar()
        self.title = StringVar()
        self.last = StringVar()
        self.first = StringVar()
        self.cat = StringVar()
        self.lang = StringVar()
        
        self.isbnEntry = tk.Entry(self.insertWindow, textvariable=self.isbn)
        self.isbnEntry.insert(0, "ISBN")
        self.isbnEntry.pack(pady=10, padx=10)
        isbn_focus_in = self.isbnEntry.bind('<Button-1>', lambda x: self.on_focus_in(self.isbnEntry))
        isbn_focus_out = self.isbnEntry.bind('<FocusOut>', lambda x: self.on_focus_out(self.isbnEntry, "ISBN"))
        
        self.titleEntry = tk.Entry(self.insertWindow, textvariable=self.title)
        self.titleEntry.insert(0, "Book Title")
        self.titleEntry.pack(pady=10, padx=10)
        title_focus_in = self.titleEntry.bind('<Button-1>', lambda x: self.on_focus_in(self.titleEntry))
        title_focus_out = self.titleEntry.bind('<FocusOut>', lambda x: self.on_focus_out(self.titleEntry, "Book Title"))
        
        self.lNameEntry = tk.Entry(self.insertWindow, textvariable=self.last)
        self.lNameEntry.insert(0, "Author LastName")
        self.lNameEntry.pack(pady=10, padx=10)
        lName_focus_in = self.lNameEntry.bind('<Button-1>', lambda x: self.on_focus_in(self.lNameEntry))
        lName_focus_out = self.lNameEntry.bind('<FocusOut>', lambda x: self.on_focus_out(self.lNameEntry, "Author LastName"))
        
        self.fNameEntry = tk.Entry(self.insertWindow, textvariable=self.first)
        self.fNameEntry.insert(0, "Author FirstName")
        self.fNameEntry.pack(pady=10, padx=10)
        fName_focus_in = self.fNameEntry.bind('<Button-1>', lambda x: self.on_focus_in(self.fNameEntry))
        fName_focus_out = self.fNameEntry.bind('<FocusOut>', lambda x: self.on_focus_out(self.fNameEntry, "Author FirstName"))
        
        self.catEntry = tk.Entry(self.insertWindow, textvariable=self.cat)
        self.catEntry.insert(0, "Category ID")
        self.catEntry.pack(pady=10, padx=10)
        cat_focus_in = self.catEntry.bind('<Button-1>', lambda x: self.on_focus_in(self.catEntry))
        cat_focus_out = self.catEntry.bind('<FocusOut>', lambda x: self.on_focus_out(self.catEntry, "Category ID"))
        
        self.langEntry = tk.Entry(self.insertWindow, textvariable=self.lang)
        self.langEntry.insert(0, "Language")
        self.langEntry.pack(pady=10, padx=10)
        lang_focus_in = self.langEntry.bind('<Button-1>', lambda x: self.on_focus_in(self.langEntry))
        lang_focus_out = self.langEntry.bind('<FocusOut>', lambda x: self.on_focus_out(self.langEntry, "Language"))
        
        submitBtn = tk.Button(self.insertWindow, text="Submit", command=lambda: self.submitRow())
        submitBtn.pack(pady=10, padx=10)
    
    def removeRow(self):
        removeWindow = Toplevel(self)
        removeWindow.title("Remove Row")
        removeWindow.geometry("400x300")
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bookslist = []
        
        self.getBooks()
        self.makeTable()
        
        backBtn = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("Content"))
        backBtn.grid(row=2, column=0)
        
        insertBtn = tk.Button(self, text="Add Row", command=lambda: self.addRow())
        insertBtn.grid(row=2, column=1)
        
        removeBtn = tk.Button(self, text="Remove Row", command=lambda: self.removeRow())
        removeBtn.grid(row=2, column=2)