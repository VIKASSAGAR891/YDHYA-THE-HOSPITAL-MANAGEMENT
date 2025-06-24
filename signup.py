from tkinter import *
from tkinter import messagebox
import mysql.connector as mc

#CONNECTION
mycon=mc.connect(host='localhost',user='root',passwd='murari123',database='siven_inc')
mycursor=mycon.cursor()

#######-------------------------
def signup():
    un=user.get()
    pd=code.get()
    cpd=codec.get()
    if un!="" or un!="Username" and cpd==pd:
        mycursor.execute("INSERT INTO CREDS VALUES ('%s','%s')"%(un,pd))
        mycon.commit()
        messagebox.showinfo("Successful","Sign Up Successful !!")
    elif un!="" and cpd!=pd:
        messagebox.showerror("Invalid","Both Passwords Don't Match !!!")
    elif un=="":
        messagebox.showerror("Invalid","Username is Must !!!")
    
   
    #######--------------------------
win=Tk()
win.title("Sign Up")
win.geometry("925x500+300+200")
win.config(bg="#fff")
win.resizable(False,False)
    ######---------------------------
img=PhotoImage(file="REC1.png")
Label(win,image=img,bg="white").place(x=50,y=100)

frame=Frame(win,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Sign Up",fg="#57a1f8",bg="white",font=('Microsoft YaHei UI Light',23,"bold"))
heading.place(x=100,y=5)
    ######------------------------------

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    ######------------------------------
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    ######------------------------------
def on_enter(e):
    codec.delete(0,'end')

def on_leave(e):
    name=codec.get()
    if name=='':
        codec.insert(0,'Confirm Password')

codec=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft YaHei UI Light',11))
codec.place(x=30,y=220)
codec.insert(0,'Confirm Password')
codec.bind('<FocusIn>',on_enter)
codec.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    ######--------------------------------


Button(frame,width=39,pady=7,text="Sign Up",bg="#57a1f8",fg='white',border=0,command=signup).place(x=35,y=280)
    #'''label=Label(frame,text="I have an Account ",fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
    #label.place(x=90,y=340)

    #sign_up=Button(frame,width=6,text="Sign In",bg='white',cursor='hand2',fg='#57a1f8')
    #sign_up.place(x=200,y=340)'''


win.mainloop()

