import tkinter as tk
from pandastable import Table
import pandas as pd
import cx_Oracle
import config

class Receipts(tk.Frame):
    def getReceipt(self):
        try:
            connection = cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding)

            # show the version of the Oracle Database
            with connection.cursor() as cursor:
                cursor.execute('select * from borrowedbooks order by receiptid')
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        self.receiptlist.append(row)
                connection.commit()
        except cx_Oracle.Error as error:
            print(error)
            
    def makeTable(self):
        df = pd.DataFrame(self.receiptlist)
        df.columns = ['Receipt ID', 'Issued By', 'ISBN', 'Borrower ID', 'Borrower Date', 'Due Date', 'Return Date'] # Rename the column names
        df['Borrower Date'] = df['Borrower Date'].dt.strftime("%d/%m/%Y")
        df['Due Date'] = df['Due Date'].dt.strftime("%d/%m/%Y")
        df['Return Date'] = df['Return Date'].dt.strftime("%d/%m/%Y")
        pt = Table(self, dataframe=df)
        pt.show()
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.receiptlist = []
        
        self.getReceipt()
        self.makeTable()
        
        backBtn = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("Content"))
        backBtn.grid(row=2, column=0, pady=10)
        