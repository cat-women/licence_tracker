from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox  as mb
import backend as bk 
import registration
import message as ms
import tkinter as tk 
from PIL import Image,ImageTk
result = bk.fetch_payment()

def on_select(event):
    sel_val = table.item(table.selection())

    ans = mb.askquestion('Confrim', 'verified ?' )    
    if(ans == 'yes'):
        flag = 0
        bk.deletePayment(sel_val['values'][1])

    else:
        flag  = 1
    # to update flag
    bk.verified(flag,sel_val['values'][1])

root = Tk()
root.geometry("600x300+300+150")
root.resizable(width=True, height=True)

Label(root,text = "payment detail ").place(x = 30, y = 20)

#form to display notice 
style = ttk.Style()

# style.theme_use('clam')
style.configure("Treeview",
                background = "white",
                foregound = "black",
                rowheight = 25,
                stretch = False      
            )
style.map('Treeview',
        background=[('selected','blue')]
            )
lb_header = ['id','Document it ','Voucher .','Bill']

#create trreeview 
table = ttk.Treeview(root, columns=lb_header, show="headings", wrap=None)

for col in lb_header:
    table.heading(col, text=col.title())

for row in result:
    table.insert('', index='end', values=row)
    
for i in result:
    print(i[2])

table.place(x = 10, y = 50)
table.bind('<<TreeviewSelect>>', on_select)
           

root.mainloop()