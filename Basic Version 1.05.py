##SQLite Database with Tkinter Backup - Basic Version 1.05##

from tkinter import *
from sqlite3 import *

class rootWindow:
    def __init__(self,parent):
        self.root = parent
        self.idLabel = None
        self.idEntry = None
        self.searchBtn = None
        self.notFoundLabel = None

        #Create UI
        self.createUI()
    def createUI(self):
        self.root.geometry("600x400")
        self.root.title("Retrive Student Details")
        
        self.idLabel = Label(self.root, text = "Enter Identification Number:")
        self.idLabel.grid(row = 0, column = 0)

        self.idEntry = Entry(self.root)
        self.idEntry.grid(row = 0, column = 1)

        self.searchBtn = Button(self.root, text = "Search", command = self.fetchRecords)
        self.searchBtn.grid(row=1, column = 1)

        self.notFoundLabel = Label(self.root, text = "")
        self.notFoundLabel.grid(row = 2, column = 0)

    def fetchRecords(self):
        searchItem = (int(self.idEntry.get()),)
        print(searchItem)
        #connect to the db
        con = connect(r"C:\Users\abhin\OneDrive\Documents\Python Programs\SQL\sqlite-tools-win32-x86-3430200\teacher.sqlite")
        query = "SELECT * FROM studentInfo WHERE id = ?;"
        cursor = con.cursor()
        cursor.execute(query, searchItem)
        results = cursor.fetchall()

        for line in results:
            print(line)

        if cursor.rowcount > 0:
            #record has been found
            idLabel = Label(self.root, width = 20, text = "ID Number:", bg="yellow")
            idLabel.grid(row = 3, column = 0)
            nameLabel = Label(self.root, width = 20, text = "Name:", bg="yellow")
            nameLabel.grid(row = 3, column = 1)
            ageLabel = Label(self.root, width = 20, text = "Age:", bg="yellow")
            ageLabel.grid(row = 3, column = 2)
            perLabel = Label(self.root, width = 20, text = "Total Marks Percentage:", bg="yellow")
            perLabel.grid(row = 3, column = 3)

            #display information
            i = 4
            for record in results:
                for j in range(0, len(record)):
                    l = Label(self.root, width = 20, text = record[j])
                    l.grid(row = i, column = j)
                i += 1
        else:
            self.notFoundLabel.configure(text = "RECORD NOT FOUND")
        con.close()

root = Tk()
mainwin = rootWindow(root)
root.mainloop()
