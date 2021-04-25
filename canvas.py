from tkinter import *
import mysql.connector 
from PIL import Image,ImageTk
from tkcalendar import Calendar, DateEntry 
import tkinter.messagebox as mb 
import backend as bk
import tkinter as Tk

        
class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
        


        #get row 
        def get_row(event):
            global selected_tuple
            index=list1.curselection()[0]
            selected_tuple=list1.get(index)

            
        #search bar 
        global search_key,list1
        search_key = StringVar()
        in_name = Tk.Entry(self.frame, textvariable=search_key, font=("Arial",20), fg="Lime", justify="center")
        in_name.pack()
        
        btn1 = Tk.Button(self.frame, text="search ", command=self.search)
        btn1.pack()

        #branch 
        branch = Tk.Label(self, text="Branch",font="monotype",bg="#FBDAB7")
        branch.pack()
        branch_name = StringVar()
        in_branch = Tk.Entry(self,textvariable=branch_name,font="Arial", fg="Lime", justify="center",width=20)
        in_branch.pack()


    def search(self):
        row = bk.search(search_key.get())
        for i in range(len(row)):
            print(row[i])
                 

if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()

    