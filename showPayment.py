import os
from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox  as mb
import backend as bk 
import registration
import message as ms
import tkinter as tk 
from PIL import Image,ImageTk
import cv2
import numpy as np
def show():
    result = bk.fetch_payment()
    root = Tk()
    root.geometry("600x300+300+150")
    root.resizable(width=True, height=True)


    def on_select(event):    
        sel_val = table.item(table.selection())
        
        img = cv2.imread(sel_val['values'][2])
        #define the screen resulation
        screen_res = 900, 400
        scale_width = screen_res[0] / img.shape[1]
        scale_height = screen_res[1] / img.shape[0]
        scale = min(scale_width, scale_height)

        window_width = int(img.shape[1] * scale)
        window_height = int(img.shape[0] * scale)

        cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Resized Window', window_width, window_height)
        cv2.imshow('Resized Window', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        ans = mb.askquestion('Confrim', 'Payment verified for %s ?'%sel_val['values'][0] )    
        if(ans == 'yes'):
            flag = 0
            db = bk.getConnection()
            cursor = db.cursor()
            cursor.execute('SELECT fine FROM document_detail WHERE docNumber = %s'%sel_val['values'][0])
            fine =cursor.fetchone()   

            #print("documetn number ",sel_val['values'][0])
            #print("documetn number ",fine[0])

            bk.verifyPayment(sel_val['values'][0],fine[0])


            #cursor.execute("UPDATE document_detail SET upload = 1 where docNumber = %s"%sel_val['values'][1])
            db.commit()
            cursor.close()
        else:
            flag  = 1
        # to update flag
        bk.verified(flag,sel_val['values'][1])
        

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
    lb_header = ['id','Document NO. ','Voucher .','Bill']

    #create trreeview 
    table = ttk.Treeview(root, columns=lb_header, show="headings", wrap=None)

    for col in lb_header:
        table.heading(col, text=col.title())

    for row in result:
        table.insert('', index='end', values=row)
        

    table.place(x = 10, y = 50)
    table.bind('<<TreeviewSelect>>', on_select)    

    Button(root, text="Quit", command=root.destroy).pack()
    root.mainloop()
