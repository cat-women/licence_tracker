from tkinter import *
from PIL import Image,ImageTk
from tkcalendar import Calendar, DateEntry 
import tkinter.messagebox as mb 
import tkinter as Tk 
import backend as bk
from tkinter import ttk

class Registration(Tk.Toplevel):
    def __init__(self, main):
        
        self.original_frame = main
        Tk.Toplevel.__init__(self)
        #self.geometry("600x600")
        self.title("Registration")
        self.iconbitmap('logo.jpg')

        self.config(background = "#ccffcc")   
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
            total = 1
            branch = branch_name.get()
            tname = traffic_name.get()
            dtype =     doc_type.get()      
            license = license_number.get()
            offence = offence_name.get()
            oname = owner.get()
            fine = fine_amt.get()
            date = date_name.get()
            vType= vecType.get()
            if(branch =='' and tname =='' and dtype =='' and license =='' and offence =='' and oname =='' and fine =='' and date =='' and vType == ''):
                mb.showinfo('Information','Cant fill empty form !')
                count+=1
                self.state()
                self.focus()
            else:
                if branch == '':
                    mb.showinfo('Information','Please enter your branch name')
                    count+=1
                    self.state()
                    self.focus()                   

                if tname == '':
                    mb.showinfo('Information','Please enter your  name')
                    count+=1
                    self.state()
                    self.focus()

                if dtype == '':
                    mb.showinfo('Information','Please enter your  name')
                    count+=1
                    self.state()
                    self.focus()
                    
                if license == '':
                    mb.showinfo('Information','Please enter licence number ')
                    count+=1              
                    self.focus()
                    
                if offence == '':
                    mb.showinfo('Information','Please enter offence')
                    count+=1
                    self.focus()

                if oname == '':
                    mb.showinfo('Information','Please enter offence')
                    count+=1
                    self.focus()
                
                if fine == '':
                    mb.showinfo('Information','Please enter fine')
                    count+=1
                    self.focus()

                if vType =='':                    
                    mb.showinfo('Information','Please enter fine')
                    count+=1
                    self.focus()


            if(count == 0):
                #db(self)
                bk.insert(branch,tname,dtype,license,oname,offence,fine,date,total,vType)
                mb.showinfo('Information','new data added succesfully ')
                self.destroy()
                return
            else:
                self.state()
                return
            

            
        

        title = Label(self, text="NEW REGISTRATION ",font=("Algerian",20), fg="#f763e1")
        title.place(x=150, y = 0)

        #branch 
        branch = Tk.Label(self, text="Branch",font="monotype")
        branch.place(x=60,y=60)
        branch_name = StringVar()

        in_branch = ttk.Combobox(self,textvariable=branch_name,font="Arial", justify="center",width=20)
        in_branch['values']=('Choose One',
                            'Metropolitan Traffic Police Office',
                            'Traffic Police Durbarg Marg',
                            'Baggi Khana Traffic Office',
                            'Traffic Division Office Thapathali',
                            'Nagdhunga Police Check Post'
                            )        
        in_branch.place(x = 250, y=60)
        in_branch.current(0)
    
        #traffic name
        trafficName = Tk.Label(self, text=" Traffic Name",font="Arial")
        trafficName.place(x=60,y=120)
        traffic_name = StringVar()
        in_traffic = Entry(self,textvariable=traffic_name,font="Arial", fg="Lime", justify="center",width=20)
        in_traffic.place(x = 250, y=120)

        #owner name
        ownerName = Tk.Label(self, text=" Owner Name",font="Arial")
        ownerName.place(x=60,y=180)
        owner = StringVar()
        in_owner = Entry(self,textvariable=owner,font="Arial", fg="Lime", justify="center",width=20)
        in_owner.place(x = 250, y=180)

        #document name 
        docType = Tk.Label(self, text=" Document Type",font="Arial")
        docType.place(x=60,y=240)
        doc_type = StringVar()
        in_doc = ttk.Combobox(self,textvariable=doc_type,font="Arial",justify="center",width=20)
        in_doc['values'] = ('Choose One',
                            'Blue book',
                            'License')
        in_doc.place(x = 250, y=240)
        in_doc.current(0)

        #license number 
        license_no = Tk.Label(self, text="License number",font="Arial")
        license_no.place(x=60,y=300)
        license_number = StringVar()
        in_license_no = Entry(self,textvariable=license_number,font="Arial", fg="Lime", justify="center",width=20)
        in_license_no.place(x = 250, y=300)

        #offence 
        offence = Tk.Label(self, text="Offence",font="Arial")
        offence.place(x=60,y=360)
        offence_name = StringVar()
        in_offence = Entry(self,textvariable=offence_name, font="Arial", fg="Lime", justify="center",width=20)
        in_offence.place(x = 250, y=360)

        #fine
        fine = Tk.Label(self, text="Fine",font="Arial")
        fine.place(x=60,y=420)
        fine_amt = StringVar()
        in_fine = Entry(self,textvariable=fine_amt, font="Arial", fg="Lime", justify="center",width=20)
        in_fine.place(x = 250, y=420)

        date = Tk.Label(self, text="Date",font="Arial")
        date.place(x=60,y=480)
        date_name = StringVar()
        in_date = DateEntry(self,textvariable=date_name, width=30, background='darkblue',foreground='white', borderwidth=2, year=2020,locale='en_US', date_pattern='y-mm-dd') 
        in_date.place(x = 250, y=480)

        vihicle_type = Tk.Label(self, text="Vehicle type",font="Arial")
        vihicle_type.place(x=60,y=540)
        vecType = StringVar()
        vechile_type = Entry(self,textvariable=vecType, font="Arial", fg="Lime", justify="center",width=20)
        vechile_type.place(x = 250, y=540)

        btn_submit = Tk.Button(self, text='submit', font="Arial", command=register)
        btn_submit.place(x = 250, y=600)

        
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
        subFrame = Registration(self)

if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    root.iconbitmap('logo.jpg')
    app = MyApp(root)
    root.mainloop()
    