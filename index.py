from tkinter import *
from tkinter import ttk as ttk

from PIL import Image,ImageTk
from tkcalendar import Calendar, DateEntry 
import tkinter.messagebox as mb 
import tkinter as tk 
import registration
import backend as bk
import display

class Window(Frame):
    global selected
    selected = []
    def on_select(self, event):
        sel_val = self.tree.item(self.tree.selection())
        sel_val = self.tree.item(self.tree.selection())      
        message = "Date : {} \n Message  : {} \n Why : {}\n Address : {}".format(sel_val['values'][0],sel_val['values'][2],sel_val['values'][3],sel_val['values'][4])
        mb.showinfo('Information', message )       


    def __init__(self, master = None):
        Frame.__init__(self,master)               
        self.master = master
        self.init_window()
    
    def init_window(self):
        self.master.title('licence tracker')
        self.pack(fill =BOTH, expand = 1)
        self.config(background = "#f5e5bf")         


        #menu function 
        def donothing():
            exit() 

        def close():
            exit()
        

        def getLogin():            
            root.destroy()
            import admin
            return


            
        #menu               
        menubar = Menu(self.master,font="Arial" )
        self.master.config(menu = menubar)

        #sign in/ out
        login = Menu(menubar, tearoff=0)
        menubar.add_command(label="Sign in", command=getLogin)
       
        #search 
        search = Menu(menubar, tearoff=0)
        search.add_command(label="Search ", command=donothing)
        #menubar.add_cascade(label="Edit", menu=search)

        #help
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)        
        
        #LOGO 
        branch = Label(self, text="LICENSE TRACKER",font=("Algerian",30),bg='#f5e5bf', fg="#f763e1")
        branch.place(x=120,y=30)

        #search bar
        global search_key 
        search_key = StringVar()
        self.in_name = Entry(self,textvariable=search_key,font=("Arial",20), fg="Lime", justify="center")
        self.in_name.place(x =120, y=120)
        
        btn_submit = tk.Button(self, text='submit', font="Arial",bg="#FBDAB7", command=lambda: display.Display(search_key.get()))
        btn_submit.place(x = 400, y=120)

        #show notification 
        Label(self, text="Notice",font=("Algerian",20),bg='#f5e5bf', fg="#f763e1").place(x=50,y=200) 
        
        #form to display notice            
        lb_header = ['date','title','msg']
        self.tree = ttk.Treeview(self,columns=lb_header, show="headings")
        self.tree.place(x = 50, y = 250)

        for col in lb_header:
            self.tree.heading(col, text=col.title())

        result = bk.fetchMsg()
        for row in result:
            self.tree.insert('', 'end', values=row)
            print(row)

        self.tree.bind('<<TreeviewSelect>>', self.on_select)
        

            
root = Tk()
width = 700
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.iconbitmap('logo.jpg')



app = Window(root)

root.mainloop()

#change font size and color of doc detail 
#scrolbar in messsage 