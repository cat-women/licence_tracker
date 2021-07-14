from logging import error
from tkinter import *
from PIL import Image,ImageTk
from tkcalendar import Calendar, DateEntry 
import tkinter.messagebox as mb 
import tkinter as Tk 
import backend as bk
from mysql.connector import Error


class AddAdmin(Tk.Toplevel):
    def __init__(self, main):        
        self.original_frame = main
        Tk.Toplevel.__init__(self)
        #self.geometry("600x600")
        self.title("Registration")
        self.config(background = "#f5f3b0")   
        self.iconbitmap('logo.jpg')

        sb = Scrollbar(self)  
        sb.pack(side = RIGHT, fill = Y)  
        width = 600
        height = 650
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.resizable(0, 0)
        #validation 
        def register():
            count = 0
            user = username.get()
            password = pwd.get()
            confirm = re.get()

            if(user =='' and password =='' and confirm ==''):
                mb.showinfo('Information','Cant fill empty form !')
                count+=1
                self.state()
                self.focus()
            else:               
                
                if user == '':
                    count+=1                   
                    mb.showinfo('Information','Please enter Username')
                    self.state()
                    self.focus()
                    

                elif password == '':
                    count+=1
                    mb.showinfo('Information','Please enter password')
                    self.state()
                    self.focus()

                elif re == password:
                    count+=1
                    mb.showinfo('Information','Password does not match')
                    self.state()
                    self.focus()
                    
            if(count == 0):
                #db(self)
                val = (user,password)
                db = bk.getConnection()
                try:
                    cursor = db.cursor()
                    sql = 'insert into login (username,password) values (%s,%s)'
                    cursor.execute(sql,val)
                    db.commit()  
                    print('New user added ')   
                    mb.showinfo('Information','New user added')

                except Error as e:
                    mb.showwarning("there is some error please try again")

                finally:
                    db.close()
                
                return
            else:
                self.state()
                return               

        branch = Label(self, text="Add new user",font=("Algerian",25),bg='#f5e5bf', fg="#f763e1")
        branch.place(x=70,y=10)
        #username 
        branch = Tk.Label(self, text="User Name ",font="monotype",bg="#FBDAB7")
        branch.place(x=60,y=60)
        username = StringVar()
        user = Entry(self,textvariable=username,font="Arial", fg="Lime", justify="center",width=20)
        user.place(x = 200, y=60)
    
        #password 
        password = Tk.Label(self, text="Password ",font="Arial",bg="#FBDAB7")
        password.place(x=60,y=120)
        pwd = StringVar()
        in_traffic = Entry(self,textvariable=pwd,font="Arial", fg="Lime", justify="center",width=20)
        in_traffic.place(x = 200, y=120)

        #confirm Password 
        confirm = Tk.Label(self, text="Re-Types Password  ",font="Arial",bg="#FBDAB7")
        confirm.place(x=60,y=180)
        re = StringVar()
        in_owner = Entry(self,textvariable=re,font="Arial", fg="Lime", justify="center",width=20)
        in_owner.place(x = 200, y=180)

        btn_submit = Tk.Button(self, text='submit', font="Arial",bg="#FBDAB7", command=register)
        btn_submit.place(x = 100, y=350)

        
class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
                
        btn = Tk.Button(self.frame, text="Open Frame", command=self.openFrame)
        btn.pack()

    def openFrame(self):
        """"""
        #self.hide()
        subFrame = AddAdmin(self)

if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()
    