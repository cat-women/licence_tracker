from tkinter import *
from tkinter import ttk as ttk

from PIL import Image,ImageTk

from tkinter import filedialog
from tkcalendar import Calendar, DateEntry 
import tkinter.messagebox as mb 
import tkinter as tk 
import registration
import backend as bk
import message as m 



## to display document detail 
def Display(key):  
        
        root = Tk()
        '''
        width = 700
        height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        root.iconbitmap('logo.jpg')
        '''
        global voucher
        data = []
        bill = []
        data.append(key)
        #defining variable for payment

        def openfn():
            filename = filedialog.askopenfilename(title='open')
            return filename
        def get_voucher(event):
            voucher = openfn()
            Label(root, text=voucher,font=("Arial")).grid(row=13, column=1, pady = 5, padx = 10)
            data.append(voucher)
            print(voucher)
            '''
                    img = Image.open(x)
                    img = img.resize((250, 250), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(root, image=img)
                    panel.image = img
                    panel.grid(row=13, column=1,columnspan=2, pady = 5, padx = 10)
            '''

        def get_bill(event):
            bill= openfn()
            Label(root, text=bill,font=("Arial")).grid(row=14, column=1, pady = 5, padx = 10)
            data.append(bill)
            print(bill)

        def add():
            print("call submit button ")
            print(data)
            bk.insert_payment(data)
            mb.showinfo('Information',"your payemnet will be verified soon !")
            root.destroy()




        def upload_pic():
            btn = Button(root, text='Upload voucher')
            btn.bind('<Button-1>',get_voucher)
            btn.grid(row=13,column=0)
            
            btn1 = Button(root, text='Upload bill')
            btn1.bind('<Button-1>',get_bill)
            btn1.grid(row=14,column=0)
            submit_btn = Button(root, text='submit', command=add)
            submit_btn.grid(row=15, column = 1)
        
        

            
        
        global name  
        #key = search_key.get()   
        if(key == ''):
            mb.showinfo()('Information','Must Enter any value')
            root.focus()
            return   

        row = bk.search(key)
        if(row == None):
            mb.showinfo()('Information','Data not found ')
            self.focus()
            return 
        root.wm_title("Document detail ")        
        Label(root,text="Document detail ",font=("Arial",25)).grid(row=0,column = 0,columnspan = 2)

        Label(root, text="Name",font=("Arial")).grid(row=1, column=0, pady = 5, padx = 10)
        e1 = Entry(root,font=("Arial"))
        e1.grid(row=1, column=1, pady = 5, padx =10)

    
        Label(root, text="Vehicle type",font=("Arial")).grid(row=2, column=0, pady = 5, padx = 10)
        e2 = Entry(root,font=("Arial"))
        e2.grid(row=2, column=1, pady = 5, padx = 10)

        Label(root, text="Document type",font=("Arial")).grid(row=3, column=0, pady = 5, padx = 10)
        e3 = Entry(root,font=("Arial"))
        e3.grid(row=3, column=1, pady = 5, padx = 10)

        Label(root, text="Document Number",font=("Arial")).grid(row=4, column=0, pady = 5, padx = 10)
        e4 = Entry(root,font=("Arial"))
        e4.grid(row=4, column=1, pady = 5, padx = 10)

        Label(root, text="Branch ",font=("Arial")).grid(row=5, column=0, pady = 5, padx = 10)
        e5 = Entry(root,font=("Arial"))
        e5.grid(row=5, column=1, pady = 5, padx = 10)

        Label(root, text="Traffic name ",font=("Arial")).grid(row=6, column=0, pady = 5, padx = 10)
        e6 = Entry(root,font=("Arial"))
        e6.grid(row=6, column=1, pady = 5, padx = 10)

        Label(root, text="offence",font=("Arial")).grid(row=7, column=0, pady = 5, padx = 10)
        e7 = Entry(root,font=("Arial"))
        e7.grid(row=7, column=1, pady = 5, padx = 10)


        Label(root, text="count",font=("Arial")).grid(row=8, column=0, pady = 5, padx = 10)
        e8 = Entry(root,font=("Arial"))
        e8.grid(row=8, column=1, pady = 5, padx = 10)


        Label(root, text="Fine",font=("Arial")).grid(row=9, column=0, pady = 5, padx = 10)
        e9 = Entry(root,font=("Arial"))
        e9.grid(row=9, column=1, pady = 5, padx = 10)

        btn = Button(root,text = "Close",command=lambda: root.destroy()).grid(row=10, column=0,columnspan=2, pady = 5, padx = 10)
        upload = Button(root,text = "Pay", command=upload_pic).grid(row=10, column=1,columnspan=2, pady = 5, padx = 10)
        #root.bind('<Button-1>', upload_pic)

        ##set text
        e1.insert(0,row[5])
        e1.config(state='disabled')

        e2.insert(0,row[10])
        e2.config(state = 'disabled')


        e3.insert(0,row[3])
        e3.config(state='disabled')

        e4.insert(0,row[4])
        e4.config(state = 'disabled')


        e5.insert(0,row[1])
        e5.config(state='disabled')

        e6.insert(0,row[2])
        e6.config(state = 'disabled')


        e7.insert(0,row[6])
        e7.config(state='disabled')

        e8.insert(0,row[9])
        e8.config(state = 'disabled') 


        e9.insert(0,row[7])
        e9.config(state = 'disabled') 
        
if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")
    app = Display(123)
    root.mainloop()
