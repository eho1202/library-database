import tkinter as tk
from tkinter import END
from pandastable import Table, TableModel
import pandas as pd
import cx_Oracle
import config

query = 'select * from book order by booktitle'

class BooksList(tk.Frame):
    def getBooks(self):
        try:
            connection = cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding)

            # show the version of the Oracle Database
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        self.bookslist.append(row)
        except cx_Oracle.Error as error:
            print(error)
            
    def makeTable(self):
        df = pd.DataFrame(self.bookslist)
        df.columns = ['ISBN', 'Book Title', 'Author LastName', 'Author FirstName', 'Category ID', 'Language'] # Rename the column names
        pt = Table(self, dataframe=df)
        pt.show()
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bookslist = []
        
        self.getBooks()
        self.makeTable()
        
        backBtn = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("Content"))
        backBtn.grid(row=2, column=1)
        
        print(self.bookslist)
        
        
        