
from tkinter import *  
from PIL import ImageTk,Image 
def showImage(imageFile):
    root = Tk()  
    canvas = Canvas(root, width = 300, height = 300)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open(imageFile))  
    canvas.create_image(20, 20, anchor=NW, image=img) 
    root.mainloop() 

import tkinter as tk
import os
from PIL import Image, ImageTk

root = tk.Tk()
tk.Label(root, text="this is the root window").pack()
root.geometry("200x200")

for i in range(1, 6):
    loc = os.getcwd() + '\pictures\pic%s.jpg'%(i)
    img = Image.open(loc)
    img.load()
    photoimg = ImageTk.PhotoImage(img)
    window = tk.Toplevel()
    window.geometry("200x200")
    tk.Label(window, text="this is window %s" % i).pack()
    tk.Label(window, image=photoimg).pack()

root.mainloop()