from tkinter import *
from tkinter import messagebox
#import main as mp 
import subprocess as sp
import mysql.connector as mc

#CONNECTION
mycon=mc.connect(host='localhost',user='root',passwd='murari123',database='siven_inc')
mycursor=mycon.cursor()


########------------------------
root=Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.config(bg="#fff")
root.resizable(False,False)

#######-------------------------
def sup():
    sp.run(["python","signup.py"],shell=False)


def signin():
    un=user.get()
    pd=code.get()
    mycursor.execute("SELECT * FROM CREDS")
    data=mycursor.fetchall()
    flag=0
    for i in data:
        if i[0]==un and i[1]==pd:
            flag=1
            
            
            sp.run(["python","main.py"],shell=False)
    if flag==0:
            messagebox.showerror("Invalid","Invalid Username Or Password")

    
#######--------------------------
img=PhotoImage(file="L11.png")
Label(root,image=img,bg="white").place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Login",fg="#57a1f8",bg="white",font=('Microsoft YaHei UI Light',23,"bold"))
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

Button(frame,width=39,pady=7,text="Sign In",bg="#57a1f8",fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an Account ?",fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
label.place(x=50,y=270)

sign_up=Button(frame,width=6,text="Sign Up",bg='white',cursor='hand2',fg='#57a1f8',command=sup)
sign_up.place(x=220,y=270)





root.mainloop()
