import tkinter as tk
from pandastable import Table
import pandas as pd
import cx_Oracle
import config

class Categories(tk.Frame):
    def getCat(self):
        try:
            connection = cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding)

            # show the version of the Oracle Database
            with connection.cursor() as cursor:
                cursor.execute('select * from category order by categoryid')
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        self.catlist.append(row)
                connection.commit()
        except cx_Oracle.Error as error:
            print(error)
            
    def makeTable(self):
        df = pd.DataFrame(self.catlist)
        df.columns = ['Category ID', 'Category Name'] # Rename the column names
        pt = Table(self, dataframe=df)
        pt.show()
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.catlist = []
        
        self.getCat()
        self.makeTable()
        
        backBtn = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("Content"))
        backBtn.grid(row=2, column=0, pady=10)
        