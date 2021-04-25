from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox 
import backend as bk 
import registration
import message as ms
import tkinter as tk 

#For Graph 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import matplotlib.animation as animation
from matplotlib import style
import numpy as np
#Animation 
def show_animation():    
    fig = plt.figure()
    line = fig.add_subplot(1,1,1)
    def animate(i):
        graph_data = bk.line()
        xs2 = []
        ys2 = []
        for x in graph_data:
            xs2.append(x[0])
            ys2.append(x[1])
        
        line.clear()
        line.plot(xs2,ys2)

    ani = animation.FuncAnimation(fig, animate, interval= 1000)
    plt.show()
     
def try_login():               # this my login function
    if name_entry.get() == "" or password_entry.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        db = bk.getConnection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `login` WHERE `username` = %s AND `password` = %s", (name_entry.get(), password_entry.get()))
               
        if cursor.fetchone() is  None:
            lbl_text.config(text="Password and eamil doesn't match ", fg="red")
              
        else:                      
            messagebox.showinfo("LOGIN SUCCESSFULLY","WELCOME")
            log.destroy()  
            MAIN_WINDOW=Tk()      #after successful this main ui should appear
            MAIN_WINDOW.title("Admin")
            MAIN_WINDOW.config(background = "#f5f3b0")   
            MAIN_WINDOW.iconbitmap('logo.jpg')

            width = 900
            height = 650
            screen_width = MAIN_WINDOW.winfo_screenwidth()
            screen_height = MAIN_WINDOW.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            MAIN_WINDOW.geometry("%dx%d+%d+%d" % (width, height, x, y))
            # scroll bar here           
            frame=Frame(MAIN_WINDOW)
            frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
            hbar=Scrollbar(frame,orient=HORIZONTAL)
            hbar.pack(side=BOTTOM,fill=X)
            vbar=Scrollbar(frame,orient=VERTICAL)
            vbar.pack(side=RIGHT,fill=Y)

            def donothing():
                    exit() 

            def close():
                messagebox.WARNING('Information','Cant fill empty form !')
                exit()
                
            def register():
                registration.Registration(MAIN_WINDOW)

            def showMessage():
                ms.AddMessage(MAIN_WINDOW)
            def logout():
                resposnse = messagebox.askquestion("Log Out","Are you sure ?", icon = 'warning')
                if resposnse == 'yes':
                    MAIN_WINDOW.destroy()
                    import index


            #Admin menu 
            menubar = Menu(MAIN_WINDOW)
            MAIN_WINDOW.config(menu=menubar)
            add = Menu(menubar, tearoff=0)
            add.add_command(label="Register", command=register)
            add.add_command(label="Message...", command=showMessage)
            menubar.add_cascade(label="Add", menu=add)      


            menubar.add_command(label="Log out", command=logout)
            menubar.add_command(label="Close", command=close)



            #Body panel 
            global selected
            selected = []
            def on_select(self):
                sel_val = tree.item(self.tree.selection())
                messagebox.INFO('Information','click click !')
          
            title = Label(frame, text="LICENSE TRACKER",font=("Algerian",30),bg='#f5e5bf', fg="#f763e1")
            title.pack(expand=True,fill=BOTH)
            



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
            lb_header = ['Branch','Doc Type','DocNo.','offence','Fine','Date','Total','flag']

            #create trreeview 
            table = ttk.Treeview(frame, columns=lb_header, show="headings", wrap=None)

            for col in lb_header:
                table.heading(col, text=col.title())

            result = bk.fetch()
            for row in result:
                table.insert('', index='end', values=row)

            table.place(x = 0, y = 250)
            table.bind('<<TreeviewSelect>>', on_select)
            
            hbar.config(command=table.xview)
            vbar.config(command=table.yview)
            table.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
            table.pack(side=LEFT,expand=True,fill=BOTH)
            

            graph = tk.Frame(MAIN_WINDOW, bg='red').pack()    
            #Bar chart
            f = Figure(figsize=(5,8), dpi=100)
            barchart = tk.Frame(graph)
            barchart.pack(side=LEFT)
            ax = f.add_subplot(111)
            result = bk.bar()
            label =[]
            count =[]
            data = 0
            for i in result:
                label.append(i[0])
                count.append(i[1])
                data+=1
            ind = np.arange(data)  # the x locations for the groups
            width = .5
            rects1 = ax.bar(ind, count, width)
            ax.set_ylabel('No of crime')
            ax.set_title('No of crime in a branch ')
            #x label 
            x = np.arange(len(label))
            ax.set_xticks(x)
            ax.set_xticklabels(label)
            #ax.legend()
            canvas = FigureCanvasTkAgg(f, barchart)
            canvas.get_tk_widget().pack(expand=True,side= RIGHT)          
            #label(barchart,text='test').pack(side=BOTTOM)





            #line Graph
            info_frame = tk.Frame(master=graph,bg='green').pack(expand = True,side=RIGHT)
            Button(master=graph, text="Show Graph", command=show_animation,font=("Arial",20)).pack(expand = True)
            Label(master=graph, text= 'Total fund raise: Rs.'+str(bk.fund()),font=("Arial",20)).pack()
            #Button(master=graph, text="Show animation", command=show_animation).pack(expand = True)


            MAIN_WINDOW. mainloop()

    


def cancel_login():        # exit function
    log.destroy()
    import index
    
#this login ui
log=Tk()                   
log.title("ADMIN-LOGIN")
log.geometry("400x400+400+200")
log.resizable (width=FALSE,height=FALSE)

LABEL_1 = Label(log,text="USER NAME")
LABEL_1.place(x=50,y=100)
LABEL_2 = Label(log,text="PASSWORD")
LABEL_2.place(x=50,y=150)

lbl_text = Label(log)
lbl_text.place(x=50, y = 170)

BUTTON_1=ttk. Button(log,text="login",command=try_login)
BUTTON_1.place(x=50,y=200)
BUTTON_1=ttk. Button(log,text="cancel",command=cancel_login)
BUTTON_1.place(x=200,y=200)


name_entry=Entry(log,width=30)
name_entry.place(x=150,y=100)
password_entry=ttk. Entry(log,width=30,show="*")
password_entry.place(x=150,y=150)

log. mainloop()



