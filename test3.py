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
        flag = FALSE
        bk.deletePayment(sel_val['values'][0])

    else:
        flag  = TRUE
    bk.verified(flag,sel_val['values'][1])

root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)


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


'''
canvas = Canvas(root, width = 100, height = 100)      
canvas.pack()      
img = ImageTk.PhotoImage(Image.open(result[10][2]))  
canvas.create_image(10,10, anchor=NW, image=img)  
'''
table.place(x = 0, y = 20)
table.bind('<<TreeviewSelect>>', on_select)
           

root.mainloop()