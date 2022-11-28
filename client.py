import tkinter as tk
from pandastable import Table
import pandas as pd
import cx_Oracle
import config

class Customers(tk.Frame):
    def getClients(self):
        try:
            connection = cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding)

            # show the version of the Oracle Database
            with connection.cursor() as cursor:
                cursor.execute('select * from client order by clientid')
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        self.clientslist.append(row)
                connection.commit()
        except cx_Oracle.Error as error:
            print(error)
            
    def makeTable(self):
        df = pd.DataFrame(self.clientslist)
        df.columns = ['Client ID', 'Client LastName', 'Client FirstName'] # Rename the column names
        pt = Table(self, dataframe=df)
        pt.show()
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.clientslist = []
        
        self.getClients()
        self.makeTable()
        
        backBtn = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("Content"))
        backBtn.grid(row=2, column=0, pady=10)
        