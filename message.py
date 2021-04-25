from tkinter import *
from PIL import Image,ImageTk
from tkcalendar import Calendar, DateEntry 
import tkinter.messagebox as mb 
import tkinter as Tk 
import backend as bk


class AddMessage(Tk.Toplevel):
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
            vartitle = title.get()
            varmsg = msg.get()
            varloc = loc.get()
            vardesc = desc.get()
            vardate = date_name.get()

            if(vartitle =='' and varmsg =='' and varloc =='' and vardesc =='' and vardate ==''):
                mb.showinfo('Information','Cant fill empty form !')
                count+=1
                self.state()
                self.focus()
            else:               
                
                if vartitle == '':
                    count+=1                   
                    mb.showinfo('Information','Please enter your title name')
                    self.state()
                    self.focus()
                    

                elif varloc == '':
                    count+=1
                    mb.showinfo('Information','Please enter location')
                    self.state()
                    self.focus()

                elif vardesc == '':
                    count+=1
                    mb.showinfo('Information','Please specify detail ')
                    self.state()
                    self.focus()
                    
                elif varmsg == '':
                    count+=1
                    mb.showinfo('Information','Please enter message  ')
                    self.focus()

            if(count == 0):
                #db(self)
                bk.insertMsg(vartitle,varmsg,vardesc,varloc,vardate)
                mb.showinfo('Information','new data added succesfully ')
                return
            else:
                self.state()
                return               

        branch = Label(self, text="Give New Message",font=("Algerian",25),bg='#f5e5bf', fg="#f763e1")
        branch.place(x=70,y=10)
        #branch 
        branch = Tk.Label(self, text="Title ",font="monotype",bg="#FBDAB7")
        branch.place(x=60,y=60)
        title = StringVar()
        in_branch = Entry(self,textvariable=title,font="Arial", fg="Lime", justify="center",width=20)
        in_branch.place(x = 200, y=60)
    
        #traffic name
        trafficName = Tk.Label(self, text="Message ",font="Arial",bg="#FBDAB7")
        trafficName.place(x=60,y=120)
        msg = StringVar()
        in_traffic = Entry(self,textvariable=msg,font="Arial", fg="Lime", justify="center",width=20)
        in_traffic.place(x = 200, y=120)

        #owner name
        ownerName = Tk.Label(self, text="Description ",font="Arial",bg="#FBDAB7")
        ownerName.place(x=60,y=180)
        desc = StringVar()
        in_owner = Entry(self,textvariable=desc,font="Arial", fg="Lime", justify="center",width=20)
        in_owner.place(x = 200, y=180)

        #document name 
        docType = Tk.Label(self, text=" Location",font="Arial",bg="#FBDAB7")
        docType.place(x=60,y=240)
        loc = StringVar()
        in_doc = Entry(self,textvariable=loc,font="Arial", fg="Lime", justify="center",width=20)
        in_doc.place(x = 200, y=240)

        date = Tk.Label(self, text="Date",font="Arial",bg="#FBDAB7")
        date.place(x=60,y=300)
        date_name = StringVar()
        in_date = DateEntry(self,textvariable=date_name, width=30, background='darkblue',foreground='white', borderwidth=2, year=2020,locale='en_US', date_pattern='y-mm-dd') 
        in_date.place(x = 200, y=300)

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
        subFrame = AddMessage(self)

if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()
    